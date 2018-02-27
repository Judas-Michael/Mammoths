import folium
from folium import plugins
import csv

mammoth_colors = {'Mammuthus columbi' : 'green',
'Mammuthus primigenius' : 'blue',
'Mammuthus hayi' : 'purple',
'Mammuthus exilis' : 'red',
'Mammuthus': 'orange'}

mammoth_map = folium.Map(location=[40,-120], zoom_start=3,tiles = 'Stamen Terrain') # terrain tiles map

lat_lng = []

with open('mammoth_data.txt','r') as mammoth_csv:
	reader = csv.reader(mammoth_csv, quoting=csv.QUOTE_NONNUMERIC)
	firstline = reader.__next__() #ignores title columns
	for line in reader: 
		lat = line[3]
		lon = line[4]
		lat_lng.append([lat,lon]) #adds lat/long
		marker_text = '%s found in %s, %s. %s.' % (line[0], line[6], line[5], line[7])
		if line[1]:
			marker_text += ' %s %s ' % (line[1], line[2])
			
		color = mammoth_colors[line[0]] #checks species for colour
			
		marker = folium.Marker([lat, lon], popup = marker_text, icon = folium.Icon(color=color))#creates coloured marker
		marker.add_to(mammoth_map)
		
mammoth_map.save('mammoth_map.html')

heatmap = folium.Map(location=[40, -120], zoom_start=3) #adds heatmap
heatmap.add_children(plugins.HeatMap(lat_lng))
heatmap.save('mammoth_heatmap.html')