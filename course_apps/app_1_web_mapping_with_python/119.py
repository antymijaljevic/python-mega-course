import folium, pandas

# data = pandas.read_csv("tenerife_spots.csv")

# lat = data["LATITUDE"]
# lon = list(data['LONGITUDE'])
# popup = list(data['POPUP'])
# icon = list(data['ICON'])

# map = folium.Map(location=[28.26, -16.63], tiles="Stamen Terrain")
# fg = folium.FeatureGroup(name="My Map")


# # zip function takes value from each list
# for a, b, c, d in zip(lat, lon, popup, icon):
#     fg.add_child(folium.Marker(location=[a,b], popup=c, icon=folium.Icon(color=d)))


# map.add_child(fg)
# map.save("tenerife.html")