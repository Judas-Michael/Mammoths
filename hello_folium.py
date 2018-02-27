import folium

map_mn =  folium.Map(location = [45, -93.2], zoom_start = 13) #creates MN map + starts at zoom


folium.Marker([44.9729, -93.2831], popup='MCTC').add_to(map_mn) #adds marker to map and label

map_mn.save('map.html') #saves map as html file

map_us = folium.Map(location =[40, -120], zoom_start=3)

map_us.save('map_us.html')

