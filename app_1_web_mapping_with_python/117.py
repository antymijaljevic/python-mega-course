import folium
from folium.map import Icon

map = folium.Map(location=[28.100519757025573, -16.754787470388955], tiles="Stamen Terrain") # zoom_start=15,

fg = folium.FeatureGroup(name="My Map")

for cordinates in [[28.108133508088347, -16.760627585378163], [28.105133508088347, -16.765627585378163], [28.10213508088347, -16.762627585378163]]:
    fg.add_child(folium.Marker(location=cordinates, popup="Good locations!", icon=folium.Icon(color='green')))

# fg.add_child(folium.Marker(location=[28.108133508088347, -16.760627585378163], popup="Playa Buena!", icon=folium.Icon(color='green')))

# fg.add_child(folium.Marker(location=[28.208133508088347, -16.360627585378163], popup="Aha Buena!", icon=folium.Icon(color='red')))


map.add_child(fg)

map.save("map1.html")