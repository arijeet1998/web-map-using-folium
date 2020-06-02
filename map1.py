import folium
import pandas
def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000<= elevation <=3000:
        return "red"
    else:
        return "blue"
map=folium.Map([14.716677, -17.467686],zoom_start=2.6) 

#markers on top of the base map
fg=folium.FeatureGroup(name="My Map")
data=pandas.read_csv("volcano.csv",encoding="ISO-8859-1")
LAT=list(data["Latitude"])
LON=list(data["Longitude"])
NAME=list(data["Volcano Name"])
ELEV=list(data["Elev"])
fg.add_child(folium.GeoJson(open("world.json",encoding = "utf-8-sig").read(),style_function=lambda x: {'fillColor':'' 
if x["properties"]["POP2005"] <10000000 else 'yellow'
if 10000000<= x["properties"]["POP2005"] <=200000000 else 'red'}))
for lat,lon,name,elev in zip(LAT,LON,NAME,ELEV):
    fg.add_child(folium.CircleMarker(location=[lat,lon],radius=6,popup=str(name)+" "+str(elev)+" m",fill_color=color_producer(elev)
    ,fill=True,color='grey',fill_opacity=0.7))
map.add_child(fg)
map.save("Map1.html")
