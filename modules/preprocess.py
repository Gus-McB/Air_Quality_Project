from sklearn.preprocessing import StandardScaler

def preprocess(df):
    df = df.dropna(subset=['Longitude','Latitude','AQI Value','AQI Category','CO AQI Value','CO AQI Category','Ozone AQI Value','Ozone AQI Category','NO2 AQI Value','NO2 AQI Category','PM2.5 AQI Value','PM2.5 AQI Category'])
    features = ['AQI Value','CO AQI Value','Ozone AQI Value','NO2 AQI Value','PM2.5 AQI Value']
    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features])
    return df, df[features]