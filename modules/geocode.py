import pandas as pd
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim

def geocodeLocations(df, cityCol='City', countryCol='Country', cachePath='../cache/geocodedCache.csv'):
    geolocator = Nominatim(user_agent="airQualityMapper")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

    try:
        cache = pd.read_csv(cachePath)
    except FileNotFoundError:
        cache = pd.DataFrame(columns=[cityCol, countryCol, 'Latitude', 'Longitude'])
    
    merged = df[[cityCol, countryCol]].drop_duplicates()
    merged = merged.merge(cache, on=[cityCol, countryCol], how='left')

    missing = merged[merged['Latitude'].isna()]
    for i, row in missing.iterrows():
        try:
            location = geocode(f"{row[cityCol]}, {row[countryCol]}")
            if location:
                merged.at[i, 'Latitude'] = location.latitude
                merged.at[i, 'Longitude'] = location.longitude
                merged.dropna(subset=['Latitude', 'Longitude']).to_csv(cachePath, index=False)
        except Exception as e:
            print(f"Error geocoding {row[cityCol]}, {row[countryCol]}: {e}")

    
    updatedCache = merged.dropna(subset=['Latitude', 'Longitude'])
    df = df.merge(updatedCache, on=[cityCol, countryCol], how='left')
    return df