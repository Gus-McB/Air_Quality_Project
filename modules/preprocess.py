from sklearn.preprocessing import StandardScaler

def five_number_summary(df, features):
    summary = {}
    for feature in features:
        summary[feature] = {
            'Min': df[feature].min(),
            'Q1': df[feature].quantile(0.25),
            'Median': df[feature].median(),
            'Q3': df[feature].quantile(0.75),
            'Max': df[feature].max()
        }
    return summary

def preprocess(df):
    df = df.dropna(subset=[
        'Longitude', 'Latitude',
        'AQI Value', 'AQI Category',
        'CO AQI Value', 'CO AQI Category',
        'Ozone AQI Value', 'Ozone AQI Category',
        'NO2 AQI Value', 'NO2 AQI Category',
        'PM2.5 AQI Value', 'PM2.5 AQI Category'
    ])

    df['OrigLongitude'] = df['Longitude']
    df['OrigLatitude'] = df['Latitude']

    features = ['CO AQI Value', 'Ozone AQI Value', 'NO2 AQI Value', 'PM2.5 AQI Value', 'Longitude', 'Latitude']

    print("Five-number summary after scaling:")
    summary = five_number_summary(df, features)
    for feature, stats in summary.items():
        print(f"\n{feature}:")
        for stat, value in stats.items():
            print(f"  {stat}: {value:.4f}")

    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features])

    X = df[features]
    y = df['AQI Value']

    return df, X, y
