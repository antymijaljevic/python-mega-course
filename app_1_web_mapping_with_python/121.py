import folium
import pandas
 
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
 
def color_alt(el):
    if el > 2000:
        return "red"
    elif 1000 <= el <= 2000:
        return "purple"
    else:
        return "green"
 
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name = "My Map")
 
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+" m", icon = folium.Icon(color = color_alt(el))))
 
 
map.add_child(fg)
map.save("map_color.html")
