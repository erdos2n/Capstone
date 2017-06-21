import matplotlib.pyplot as plt 
import matplotlib


font = {'family' : 'monospace',
        'weight' : 'medium',
        'size'   : 14}

matplotlib.rc('font', **font)


def plot_dictionaries(dicts = None, labels = None):
	fig, ax = plt.subplots(nrows=2, ncols=2, figsize = (10, 10))
	


	index = 0
	for row in ax:
	    for col in row:
	    	col.grid(zorder = 0, linestyle = 'dashed', color = '#acaaa8')
	    	xvalues = range(len(dicts[index].keys()))
	    	yvalues = dicts[index].values()
	    	names   = [str(ad) for ad in dicts[index].keys()]
	        col.bar(xvalues, yvalues, ec='#383632', color='#a7c059', zorder = 3)
	        col.set_xticks(xvalues)
	        col.set_xticklabels(names, rotation = 90)
	        col.set_ylabel('Wins')
	        col.set_xlabel('Ads')
	        if labels:
	            col.set_title('threshold = {}'.format(labels[index]))

	        index += 1
	# ads = sorted(ads.items(), key = operator.itemgetter(1))[::-1]
	# xvalues = range(1, len(ads) + 1)
	# yvalues = [ad[1] for ad in ads]
	# names = [str(ad[0]) for ad in ads]
	plt.tight_layout()
	plt.show()