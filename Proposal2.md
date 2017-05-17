<center>
![](images/galvanize-logo.jpg?raw=true){:height="200px" width="200px"}![](images/infinite-logo.jpeg?raw=true){:height="200px" width="200px"}
</center>

# Ad Agency Capstone - Rafa C
**Part 1: Impression Model**
------------------------------
* Using attribution reports, I will run a multi-arm bandit to show which ads to run, how many times to run each ad and which order to run the ads.
	* **Steps to Setup Multi-Arm Bandit**
		* Create W/L lists for all ads
		* Use Uniform Distributions
		* Run Multi-Arm Bandit many times to get statistics

* After I do this, I would like to create some dashboard using Flask that will read in the report, play the game and give the best outcomes


**Part 2: Text Analysis**
------------------------------
* The company cannot get me enough reviews to train a model (they can only give me 60 statements, we can discuss if this is enough later).

* I will create a sentiment analysis using gensem and textblob or maybe just gensem.  I'm not entirely sure of what gensem can do, so I need to look into it more.  Regardless, I plan on using scores to create a grading system from 1 to 10 or 1 to 5 (depending on the companies needs)

* After I do this, I will create a dashboard for them to use on their own website.  I will work with their development team to do this and hopefully give HR and the CEO to have access to these grades. 
