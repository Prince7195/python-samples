import pandas
import folium

volcanos = pandas.read_excel("volcanos.xlsx", 0)

lat = list(volcanos["Latitude"])
log = list(volcanos["Longitude"])
title = list(volcanos["Volcano Name"] + ", " + volcanos["Country"])
elev = list(volcanos["Elevation"])

map = folium.Map(location=[13.08, 80.278], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanos")

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


for lt, lg, t, el in zip(lat, log, title, elev):
    fgv.add_child(folium.Marker(location=[lt, lg], popup=t, icon=folium.Icon(color=color_producer(el))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(
    folium.GeoJson(
        data=open("world.json", "r", encoding="utf-8-sig").read(),
        style_function=lambda x: { 
            "fillColor": "green" if x["properties"]["POP2005"] < 10000000 else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"
        }
    )
)

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Volcanos.html")