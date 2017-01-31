# *Mobility patterns in Switzerland with Twitter*
Project Member: Fan Zhang, Wenyuan Lv, Lie He

# Abstract
Can we reconstruct mobility flows of the users from their Twitter post? Recently, the study of user mobility gains more interests. We would like to analysis the mobility habit of Twitter users in Switzerland among past 7 years. 

# Data description 
We need that following data:

- Twitter user ID, post time, post location, twitter tag
- Topojson file for Switzerland at canton level.
- Geojson file for Germany, France, Italy and Austria.
- Twitter time span: data from the past 10 years.

# Files
| filename | functionality|
|:---:|:----:|
|AnalysePeopleCrossBorder.ipynb| Compute and store the number of people across border|
|GenerateData.ipynb| Preprocess data and extract useful information|
|HashtagPostprocessing.ipynb| Investigate the relation between hashtag and time/Location|
|Leaf_json data.ipynb| Generate data for leaflet plotting|
|process data.ipynb| Data preprocessing for the large data|
|text_tag.ipynb| Extract Tag from the twitter content|
|UserPeriodicalAnalysis.ipynb| Investigate the periodical behaviof of user during a period of time|
|web/leaf_json.html|display the general information of twitter information|
|web/bubbleplot.html| Display the relation between hashtag and time/geo information|


# Feasibility and Risks
## Simplify data model: 
Tree model geo information formation. We use inverse geo searching to find the country, canton, city information of each user and build a tree to store them (top is country and the bottom is street). Then we can put the scope by our needs. For example, to avoid tracing the accurate flow for each user, we manage to put the scope on the level of city, which means that we obtain the city information of each user by inverse geo searching (from users’ latitude, longitude information to city name and their latitude and longitude).         

# Deliverables

Three webpages are delivered.Each function and conclusions are shown below:

## leaf_json.html: 
- Function: number of twitters in each state at a day are displayed in the map, the darker color illustrates more twitters. When we move mouse to each state, at the top right of the map will display the exact numebr of twitter in the specific states. On the top of the map, a slide bar allows us to select the date and the selected dates is shown as well.
- Conclusion: 
  1. There are extraordinary number of twitters at 2013/12/08 and 2014/01/02. 
  2. In switzerland, Geneva normally have the most twitters throughout the year and especially at 2014 and 2015; whereas Uri has the least post.
  
## times_series.html: 
- Function: In this html, we present the overall information of the dataset,   including:

    1. The number of twitters evolve over time.
    2. The net input of people to Switzerland.
    3. The portion of people who have crossed border and eventually return to their home country
    4. The portion of people who has crossed the country.

- Conclusion: The missing values and non uniform twitter sampling makes the dataset more biased. We need to pay attention to the details if we need use its information.

## bubbleplot.html: 
- Function: in bubbleplot.html:  we look into Day 2014/Jan/2 and find the most tags is `#newyearrocks`. The distribution of the data is presented in a bubble plot with changes overtime. The evolution of number of `#newyearrocks` in each place is also presented as an orbit in an aster plot.

- Conclusion: Apart from big cities like Geneva, Lucerne, we also observe small cities have large `#newyearrocks` number. We may guess that there are some events happen to those area.
 
## Relative packet and library:
- D3;  
- leaflet;   
