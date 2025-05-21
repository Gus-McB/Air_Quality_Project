import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def performance(df, predictedCol='PredictedAQICategory', trueCol='AQI Category'):
    df = df.copy()
    
    trueLabels = df[trueCol]
    predictedLabels = df[predictedCol]

    labels = sorted(list(set(trueLabels.unique()) | set(predictedLabels.unique())))

    cm = confusion_matrix(trueLabels, predictedLabels, labels=labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    disp.plot(cmap=plt.cm.Blues)
    plt.title("Confusion Matrix")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    print("Classification Report:\n")
    print(classification_report(trueLabels, predictedLabels, labels=labels, zero_division=0))
