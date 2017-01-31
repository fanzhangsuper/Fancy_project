# *Mobility patterns in Switzerland with Twitter*
Project Member: Fan Zhang, Wenyuan Lv, Lie He

# Abstract
Can we reconstruct mobility flows of the users from their Twitter post? Recently, the study of user mobility gains more interests. We would like to analysis the mobility habit of Twitter users in Switzerland among past 10 years. 

# Data description 
We need that following data:

- Twitter user ID, 
- GPS information, 
- post time, 
- Twitter content (tag, emotion, sentence, etc.) (Translate to English for all content if possible)
- Topojson file for Switzerland at city level.
- Twitter time span: data from the past 10 years.

# Files
| filename | functionality|
|:---:|:----:|
|AnalysePeopleCrossBorder.ipynb| Compute and store the number of people across border|
|GenerateData.ipynb| Preprocess data and extract useful information|
|HashtagPostprocessing.ipynb| Investigate the relation between hashtag and time/Location|
|Leaf_json data.ipynb| Generate data for leaflet plotting|
|otherdayscount.ipynb| |
|postanalysis.ipynb| |
|text_tag.ipynb| Extract Tag from the twitter content|
|UserPeriodicalAnalysis.ipynb| Investigate the periodical behaviof of user during a period of time|
|web/leaf_json.html|display the general information of twitter information|
|web/bubbleplot.html| Display the relation between hashtag and time/geo information|


# Feasibility and Risks
## Simplify data model: 
Tree model geo information formation. We use inverse geo searching to find the country, canton, city information of each user and build a tree to store them (top is country and the bottom is street). Then we can put the scope by our needs. For example, to avoid tracing the accurate flow for each user, we manage to put the scope on the level of city, which means that we obtain the city information of each user by inverse geo searching (from users’ latitude, longitude information to city name and their latitude and longitude).

## Relative packet and library:

- D3.js; 
- Leaflet.js;

## Risks:
- The unpredictable of the user posting habit will affect the trajectory building. For example, if user A travel from P1 to P2 and then go to P3, but he did not post anything at P2, then we will simply assume that the trajectory will be from P1 to P3 and omit the existence of P2. 
- Event detection will be a risk and if time allows, we will implement the event detection for certain large event.

# Deliverables
Reconstructing mobility flows of the users:
In a map, show the location city or canton of all users at certain time, then use a timeline to illustrate the flow of each users, the colour of the trajectory will represent the number of users that have the same mobility flow. 


time_series.html : In this html, we present the overall information of the dataset, including:

1. The number of twitters evolve over time.
2. The net input of people to Switzerland.
3. The portion of people who have crossed border and eventually return to their home country
4. The portion of people who has crossed the country.

in bubbleplot.html:  we look into Day 2014/Jan/2 and find the most tags is `#newyearrocks`. The distribution of the data is presented in a bubble plot with changes overtime. The evolution of number of `#newyearrocks` in each place is also presented as an orbit in an aster plot.






