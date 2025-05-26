import folium
from folium.plugins import FloatImage

def getAqiColour(aqi):
    if aqi <= 50:
        return 'green'
    elif aqi <= 100:
        return 'yellow'
    elif aqi <= 150:
        return 'orange'
    elif aqi <= 200:
        return 'red'
    elif aqi <= 300:
        return 'purple'
    else:
        return 'maroon'

def createAQIMap(df, aqi_col, title="AQI Map"):
    # Start the map centered around the mean lat/lon
    m = folium.Map(
        location=[df['OrigLatitude'].mean(), df['OrigLongitude'].mean()],
        zoom_start=2,
        control_scale=True
    )

    # Add points
    for _, row in df.iterrows():
        color = getAqiColour(row[aqi_col])
        folium.CircleMarker(
            location=(row['OrigLatitude'], row['OrigLongitude']),
            radius=6,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.7,
            popup=f"{title}<br>{row[aqi_col]:.1f}"
        ).add_to(m)

    # Add AQI Legend (custom image or HTML)
    legend_html = '''
     <div style="
         position: fixed;
         bottom: 50px; left: 50px; width: 230px; height: 160px;
         background-color: white;
         border:2px solid grey; z-index:9999;
         font-size:14px;
         padding: 10px;
     ">
     <b>AQI Category Legend</b><br>
     <i style="background:green;color:green">....</i> Good (0–50)<br>
     <i style="background:yellow;color:yellow">....</i> Moderate (51–100)<br>
     <i style="background:orange;color:orange">....</i> Unhealthy for SG (101–150)<br>
     <i style="background:red;color:red">....</i> Unhealthy (151–200)<br>
     <i style="background:purple;color:purple">....</i> Very Unhealthy (201–300)<br>
     <i style="background:maroon;color:maroon">....</i> Hazardous (301+)<br>
     </div>
     '''
    m.get_root().html.add_child(folium.Element(legend_html))

    return m
