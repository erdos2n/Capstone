<p align = "center">
<img src = "https://cdn.geekwire.com/wp-content/uploads/2016/09/Galvanize-Logo-Text-Logo-png-4.png">
<img src = "https://theinfiniteagency.com/wp-content/themes/infiniteAgency/assets/dist/img/west.jpg">
</p>

# Ad Agency Capstone - Rafa
<h1> Part 1: Impression Model </h1>

Using attribution reports, I will run a multi-arm bandit to show which ads to run, how many times to run each ad and which order to run the ads.

1. Steps to Setup Multi-Arm Bandit

	a. Create win/loss lists for all ads
	
	b. Use Uniform Distributions
	
	c. Run Multi-Arm Bandit many times to get statistics

After I do this, I would like to create some dashboard using Flask that will read in the report, play the game and give the best outcomes

<h2> Data Description </h2>
My data is a collection of tables  with various rows and 4000 + columns.  The column lengths are equal across all tables, which is nice, because I can concatenate all of the tables...and by can, I mean, I did. 

<h3>Step 1: Clean the data </h3>

<p align = "center">
<img src = "http://tomba.co/analysis-consult/images/data-cleansing.jpg">
</p>

The **cleaning pipeline** does the following:

1. First I combine all of the tables into a large table (big_frame)

2. Then I drop all NaN columns (100% NaNs)

	a. That reduces the number of columns to 1000

3. After that I go through and convert all of the dates to datetime objects within the dataframe

4. I then go and filter out all of the impressions that the customer has seen and create a list of our them.

	a. Ex: [[ad1], [ad2, ad5, ad1], [ad2, ad5, ad5, ad9, ..., ad10], ...]

5. Three new columns are then created using that data:

	a. big_frame[hr] = the hour of the conversion, regardless of the day

	b. big_frame[path_length] = the number of ads that person has seen before they converted.

	c. big_frame[paths] = the actual ads they saw in order 

<center>
|  <td colspan=3> Big Frame      |
|....| hr | path_length | paths  |
|----|----|-------------|--------|
|....| 15 |     5       |[ad1,..]|
|....| 2  |     1       |[ad5]   |

</center>

<h3>Step 2: Analyze the data </h3>

<p align = "center">
<img src = "https://i.stack.imgur.com/T1Hep.png">
</p>


1. I then created histograms for the following data, to find relationships:

	a. Conversions by time of day 
	
	b. path lengths 

	c. ads seen 

2. Now, I'm going to use this data to create a count of wins and losses for each ad.  

	a. A win is if the ad is the last attribution in the path. (last node in the path) 

	b. A loss if it is anywhere else.

		i. Ex: ad1 = [0, 0, 0, 0,  1, 0, 0, 1, 0, 0, 1, 1, 1, 0]

	c. 0s are losses
	
	d. 1s are wins 

<h3>Step 3: Run the multi-arm bandit</h3>

<p align = "center">
<img src = "http://imgs.xkcd.com/comics/progeny.png">
</p>


<h4>Steps to create the multi-arm bandit:</h4>

1. I will create a uniform distribution across the ads

2. I will choose an ad and change that ads distribution accordingly. 

3. Then, we will pop off an element from that ads list [either a 0 or 1]. 
	a. If 1, we finish the game.
	b. If 0, we do this again.

4. Do step 3 thousands of times, finding a most common path.

5. This will become the impression model that needs to be used. 

<h3>Step 4: Host it in Flask</h3>

I would like an interface where a file can be uploaded (attribution report) and then a multi-arm bandit would begin, based on the given data in the attribution report. But that may not be possible, I don't really know at this point in time, given we haven't learned Flask....yet!


<h2>Part 2: Text Analysis</h2>
------------------------------
1. The company cannot get me enough reviews to train a model (they can only give me 60 statements, we can discuss if this is enough later).

2. I will create a sentiment analysis using gensem and textblob or maybe just gensem.  I'm not entirely sure of what gensem can do, so I need to look into it more.  Regardless, I plan on using scores to create a grading system from 1 to 10 or 1 to 5 (depending on the companies needs)

3. After I do this, I will create a dashboard for them to use on their own website.  I will work with their development team to do this and hopefully give HR and the CEO to have access to these grades. 
