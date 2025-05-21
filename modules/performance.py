import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

def performance(df, predictedCol, trueCol='AQI Category'):
    df = df.copy()

    trueLabels = df[trueCol]
    predictedLabels = df[predictedCol]

    # Get all unique labels from true and predicted, exclude Noise if not present in classification
    labels = sorted(set(trueLabels.unique()).union(set(predictedLabels.unique())))
    if 'Noise' in labels:  # Remove 'Noise' for classification since it's not a label here
        labels.remove('Noise')

    # Confusion Matrix
    cm = confusion_matrix(trueLabels, predictedLabels, labels=labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    disp.plot(cmap=plt.cm.Blues)
    plt.title("Confusion Matrix")
    plt.xticks(rotation=45)
    plt.tight_layout(w_pad=5)
    plt.show()

    # Classification Report
    report = classification_report(trueLabels, predictedLabels, labels=labels, output_dict=True, zero_division=0)
    print("Classification Report:\n")
    print(classification_report(trueLabels, predictedLabels, labels=labels, zero_division=0))

    # Bar Chart: Precision, Recall, F1-score
    metrics_df = pd.DataFrame(report).transpose()
    # Filter only the classes (ignore 'accuracy', 'macro avg', 'weighted avg')
    metrics_df = metrics_df.loc[labels, ['precision', 'recall', 'f1-score']]

    metrics_df.plot(kind='bar', figsize=(10, 6), ylim=(0, 1), colormap='tab10')
    plt.title("Precision, Recall, and F1-score per Class")
    plt.ylabel("Score")
    plt.xticks(rotation=45)
    plt.grid(True, axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

    # Support per Class (True label counts)
    support_counts = df[trueCol].value_counts().reindex(labels, fill_value=0)
    support_counts.plot(kind='bar', color='skyblue', edgecolor='black', figsize=(10, 5))
    plt.title("Support (Samples per True AQI Category)")
    plt.ylabel("Number of Samples")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
