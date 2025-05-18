import pandas as pd
from pathlib import Path
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim

def geocodeLocations(df, cityCol='City', countryCol='Country', cachePath=Path("./cache/cachedData.csv")):
    cachePath = Path(cachePath)
    cachePath.parent.mkdir(parents=True, exist_ok=True)

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
                print(location.latitude, location.longitude)
        except Exception as e:
            print(f"Error geocoding {row[cityCol]}, {row[countryCol]}: {e}")

    updatedCache = merged.dropna(subset=['Latitude', 'Longitude'])
    updatedCache.to_csv(cachePath, index=False)
    print(f"Saved {len(updatedCache)} geocoded entries to {cachePath}")
    print(f"Saved {len(updatedCache)} geocoded entries to {cachePath.resolve()}")

    df = df.merge(updatedCache, on=[cityCol, countryCol], how='left')
    return df
