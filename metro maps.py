import folium
import pandas
data=pandas.read_csv("asg2.csv")
lat=list(data["lat"])
lon=list(data["lon"])
color=list(data["color"])
name=list(data["Cityname"])
map=folium.Map(location=(12.58,77.47),zoom_start=6)
fg=folium.FeatureGroup(name="bangloremap")
for lt,ll,n,c in zip(lat,lon,name,color):
    fg.add_child(folium.Marker(location=(lt,ll),popup='c',icon=folium.Icon(color=c)))
map.add_child(fg)
map.save('bmap1.html')

