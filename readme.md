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

# Feasibility and Risks

## Simplify data model: 
Tree model geo information formation. We use inverse geo searching to find the country, canton, city information of each user and build a tree to store them (top is country and the bottom is street). Then we can put the scope by our needs. For example, to avoid tracing the accurate flow for each user, we manage to put the scope on the level of city, which means that we obtain the city information of each user by inverse geo searching (from users’ latitude, longitude information to city name and their latitude and longitude).

## Visualization:
In a map, show the location city or canton of all users at certain time, then use a timeline to illustrate the flow of each users, the colour of the trajectory will represent the number of users that have the same mobility flow. 

## Relative packet and library:

- D3.js; 
- javascript;     
- leaflet;            

# Deliverables

Three webpages are delivered.Each function and conclusions are shown below:

## leaf_json.html: 
- Function: number of twitters in each state at a day are displayed in the map, the darker color illustrates more twitters. When we move mouse to each state, at the top right of the map will display the exact numebr of twitter in the specific states. On the top of the map, a slide bar allows us to select the date and the selected dates is shown as well.
- Conclusion: 
  1. There are extraordinary number of twitters at 2013/12/08 and 2014/01/02. 
  2. In switzerland, Geneva normally have the most twitters throughout the year and especially at 2014 and 2015; whereas Uri has the least post.
  
## times_series.html: 
- Function:
- Conclusion

## bubbleplot.html: 
- Function:
- Conclusion:
