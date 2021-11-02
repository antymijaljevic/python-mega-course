import folium
from folium.map import Icon

map = folium.Map(location=[28.100519757025573, -16.754787470388955], tiles="Stamen Terrain") # zoom_start=15,

fg = folium.FeatureGroup(name="My Map")

fg.add_child(folium.Marker(location=[28.108133508088347, -16.760627585378163], popup="Playa Buena!", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("map1.html")