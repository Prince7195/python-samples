import folium

map = folium.Map(location=[13.08, 80.278], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="Chennai Map")
fg.add_child(folium.Marker(location=[13.08, 80.278], popup="Chennai", icon=folium.Icon(color="red")))
fg.add_child(folium.Marker(location=[11.40,  76.69], popup="Ooty", icon=folium.Icon(color="green")))
fg.add_child(folium.Marker(location=[10.44, 77.52], popup="Palani", icon=folium.Icon(color="blue")))
map.add_child(fg)

map.save("Chennai-Map.html")