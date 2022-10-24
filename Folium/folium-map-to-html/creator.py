# pip install folium

import folium
from folium.plugins import MarkerCluster

import random

# initialize folium map
Mapobj = folium.Map([24.21, 81.08], zoom_start=4)

# adding marker clusters
mClustser = MarkerCluster(name='Marker example').add_to(Mapobj)

# making random latitude and longitude
markerLocations = [ [random.uniform(18, 29), random.uniform(73, 85)] for x in range(100) ]
# print(markerLocations)

# initialize marker pointers
for mark in markerLocations:
    folium.Marker(location=[mark[0], mark[1]], popup="mark - {0}, {1}".format(mark[0], mark[1])).add_to(mClustser)

# adding marker pointers to map
folium.LayerControl().add_to(Mapobj)

# saving map as html format
Mapobj.save('folium-map-to-html\converted-map.html')