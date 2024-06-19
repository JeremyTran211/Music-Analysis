# Import Libraries
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

music_chart = pd.read_csv('rym_clean1.csv')

#Gets the first 10 and last 10 element of the list 
first10_rating  = music_chart[['avg_rating']].head(10)
last10_rating = music_chart[['avg_rating']].tail(10)
first10_position  = music_chart[['position']].head(10)
last10_position  = music_chart[['position']].tail(10)

#Plots the first 10 values of 'position' and 'avg_rating')
plt.figure(1)
plt.scatter(x = first10_position, y = first10_rating, color = 'blue')
plt.xlabel('Chart Position')
plt.ylabel('Average Rating')
plt.title('Music Rating vs Chart Position of First 10')

#Plots the last 10 values of 'position' and 'avg_rating')
plt.figure(2)
plt.scatter(x = last10_position, y = last10_rating, color = 'red')
plt.xlabel('Chart Position')
plt.ylabel('Average Rating')
plt.title('Music Rating vs Chart Position of Last 10')
#plt.show()

#Finds Pop in the 'primary_genres' column. Then calculate the average of the 'avg_rating' and 'position'
#and rounded to 2 decimal spots
Pop_Data = music_chart[music_chart['primary_genres'].str.contains('Pop') == True]
Average_Pop_rating = np.round_(np.mean(Pop_Data['avg_rating']), 2)
Average_Pop_position = np.round_(np.mean(Pop_Data['position']), 2)

#Repeats the step above but now for Hip Hop and Rap. 
#The Hip Hop and Rap genres are combined for easier understanding since the site I'm using for top genres consider them the same 
Hip_Hop_Data = music_chart[music_chart['primary_genres'].str.contains('Rap | Hip Hop') == True]
Average_Hip_Hop_rating = np.round_(np.mean(Hip_Hop_Data['avg_rating']), 2)
Average_Hip_Hop_position = np.round_(np.mean(Hip_Hop_Data['position']), 2)

#Steps repeated for the last 7 of Top 10 Genres 
Rock_Data = music_chart[music_chart['primary_genres'].str.contains('Rock') == True]
Average_Rock_rating = np.round_(np.mean(Rock_Data['avg_rating']), 2)
Average_Rock_position = np.round_(np.mean(Rock_Data['position']), 2)

#Dance and electronic combined for the same reason as Hip hop and rap
Dance_Data = music_chart[music_chart['primary_genres'].str.contains('Dance | Electronic') == True]
Average_Dance_rating = np.round_(np.mean(Dance_Data['avg_rating']), 2)
Average_Dance_position = np.round_(np.mean(Dance_Data['position']), 2)

Latin_Data = music_chart[music_chart['primary_genres'].str.contains('Latin') == True]
Average_Latin_rating = np.round_(np.mean(Latin_Data['avg_rating']), 2)
Average_Latin_position = np.round_(np.mean(Latin_Data['position']), 2)

Indie_Data = music_chart[music_chart['primary_genres'].str.contains('Indie | Alternative') == True]
Average_Indie_rating = np.round_(np.mean(Indie_Data['avg_rating']), 2)
Average_Indie_position = np.round_(np.mean(Indie_Data['position']), 2)

Classical_Data = music_chart[music_chart['primary_genres'].str.contains('Classical') == True]
Average_Classical_rating = np.round_(np.mean(Classical_Data['avg_rating']), 2)
Average_Classical_position = np.round_(np.mean(Classical_Data['position']), 2)

K_Pop_Data = music_chart[music_chart['primary_genres'].str.contains('K-Pop') == True]
Average_K_Pop_rating = np.round_(np.mean(K_Pop_Data['avg_rating']),2)
Average_K_Pop_position = np.round_(np.mean(K_Pop_Data['position']), 2)

Country_Data = music_chart[music_chart['primary_genres'].str.contains('Country') == True]
Average_Country_rating = np.round_(np.mean(Country_Data['avg_rating']), 2)
Average_Country_position = np.round_(np.mean(Country_Data['position']), 2)

Metal_Data = music_chart[music_chart['primary_genres'].str.contains('Metal') == True]
Average_Metal_rating = np.round_(np.mean(Metal_Data['avg_rating']), 2)
Average_Metal_position = np.round_(np.mean(Metal_Data['position']), 2)

#Initialize color list 
color = ['red', 'blue', 'black', 'skyblue', 'purple', 'pink','green', 'orange', 'yellow', 'olive']

#Organizing all data collected from above into a list 
genres_rating = [Average_Pop_rating, Average_Hip_Hop_rating,Average_Rock_rating,Average_Dance_rating, Average_Latin_rating, Average_Indie_rating,
                Average_Classical_rating, Average_K_Pop_rating,  Average_Country_rating, Average_Metal_rating]

genres_avg_positions = [Average_Pop_position, Average_Hip_Hop_position,Average_Rock_position,Average_Dance_position,Average_Latin_position, Average_Indie_position,
                Average_Classical_position, Average_K_Pop_position,  Average_Country_position, Average_Metal_position]

#Plotting data of genres rating vs their position on chart 
plt.figure(3)
plt.scatter(x = genres_rating, y = genres_avg_positions, c = color)
plt.xlabel('Genres Average Rating ')
plt.ylabel('Genres Average Chart Position ')
plt.title('Genres Rating vs Chart Position')

plt.show()