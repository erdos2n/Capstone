<p align = "center">
![](https://cdn.geekwire.com/wp-content/uploads/2016/09/Galvanize-Logo-Text-Logo-png-4.png)
</p>
<p align = "center">
![](https://media.licdn.com/mpr/mpr/AAEAAQAAAAAAAAQeAAAAJGFkMjczOTIxLWZkNjUtNGMxZi1hZTIxLTAwMjBmODVjZTI0Ng.png)
</p>

# Ad Agency Capstone - Rafa
**Part 1: Impression Model**
------------------------------
* Using attribution reports, I will run a multi-arm bandit to show which ads to run, how many times to run each ad and which order to run the ads.
	* **Steps to Setup Multi-Arm Bandit**
		* Create W/L lists for all ads
		* Use Uniform Distributions
		* Run Multi-Arm Bandit many times to get statistics

* After I do this, I would like to create some dashboard using Flask that will read in the report, play the game and give the best outcomes
*

# Data Description
My data is a collection of tables  with various rows and 4000 + columns.  The column lengths are equal across all tables, which is nice, because I can concatenate all of the tables...and by can, I mean, I did. 

I created a **data cleaning pipeline** that works as follows:
* First I combine all of the tables into a large table (big_frame)
* Then I drop all NaN columns (100% NaNs)
* That reduces the number of columns to 1000
* After that I go through and convert all of the dates to datetime objects within the dataframe
* I then go and filter out all of the impressions that the customer has seen and create a list of our them.
    - Ex: [[ad1], [ad2, ad5, ad1], [ad2, ad5, ad5, ad9, ..., ad10], ...]
* Three new columns are then created using that data:
    - big_frame[hr] = the hour of the conversion, regardless of the day
    - big_frame[path_length] = the number of ads that person has seen before they converted.
    - big_frame[paths] = the actual ads they saw in order 
* I then created histograms for the following data, to find relationships:
    - Conversions by time of day 
    - path lengths 
    - ads seen 
* Now, I'm going to use this data to create a count of wins and losses for each ad.  
    - A win is if the ad is the last attribution in the path. (last node in the path) 
    - A loss if it is anywhere else.
    - Ex: ad1 = [0, 0, 0, 0,  1, 0, 0, 1, 0, 0, 1, 1, 1, 0]
        + 0s are losses
        + 1s are wins 
* I'm then going to run a bayesian multi-arm bandit using this information and find the optimal path length, iterating over each 'game'. 
* This will become the impression model that needs to be used. 


**Part 2: Text Analysis**
------------------------------
* The company cannot get me enough reviews to train a model (they can only give me 60 statements, we can discuss if this is enough later).

* I will create a sentiment analysis using gensem and textblob or maybe just gensem.  I'm not entirely sure of what gensem can do, so I need to look into it more.  Regardless, I plan on using scores to create a grading system from 1 to 10 or 1 to 5 (depending on the companies needs)

* After I do this, I will create a dashboard for them to use on their own website.  I will work with their development team to do this and hopefully give HR and the CEO to have access to these grades. 
