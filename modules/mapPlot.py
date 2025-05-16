import folium

def plotClusters(df, labels):
    m = folium.Map(location=[20,0], zoom_start=2)
    colors = ['red', 'green', 'blue', 'purple', 'orange', 'darkred']

    for i, row in df.iterrows():
        label = labels[i]
        color = colors[label % len(colors)] if label != -1 else 'gray'
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius = 5,
            popup=f"{row['City']}, {row['Country']}",
            color=color,
            fill=True,
            fill_opacity=0.7,
        ).add_to(m)
    return m