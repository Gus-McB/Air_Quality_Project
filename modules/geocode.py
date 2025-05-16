import pandas as pd
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim

def geocode_locations(df, cityCol='City', countryCol='Country', cache_path='../cache/geocodedCache.csv'):
    geolocator = Nominatim(user_agent="airQualityMapper")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

    try:
        cache = pd.read_csv(cache_path)
    except:
        cache = pd.DataFrame(columns=[cityCol, countryCol, 'Latitude', 'Longitude'])
    
    merged = df[[cityCol, countryCol]].drop_duplicates()
    merged = merged.merge(columns=[cityCol, countryCol, 'Latitude', 'Longitude'])

    missing = merged[merged['Latitude'].isna()]
    for i, row in missing.iterrows():
        location = geocode(f"{row[cityCol]}, {row[countryCol]}")
        if location:
            merged.at[i, 'Latitude'] = location.latitude
            merged.at[i, 'Longitude'] = location.longitude
    
    updatedCache = merged.dropna(subset=['Latitude', 'Longitude'])
    updatedCache.to_csv(cache_path, index=False)

    df = df.merge(updatedCache, on=[cityCol, countryCol], how='left')
    return df