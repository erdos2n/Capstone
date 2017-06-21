import os, sys
import glob
import pandas as pd
import numpy as np
import scipy.special
import operator

from collections import Counter, defaultdict
from time import time
import datetime

import matplotlib.pyplot as plt
import matplotlib

from Upload_BodyGuardz import * 


font = {'family' : 'monospace',
        'weight' : 'medium',
        'size'   : 24}

matplotlib.rc('font', **font)

today = str(datetime.date.today())

newpath = r'/home/rafa/github/For Businesses/Infinite-Agency/Results-From-{}/'.format(today)
if not os.path.exists(newpath):
    os.makedirs(newpath)

def make_histogram_time_of_day(new_frame):
	fonts = 24
	f, (ax0) = plt.subplots(1, 1, figsize = (10, 10))

	ax0.grid(zorder = 0, linestyle = 'dashed', color = '#acaaa8')
	ax0.hist(new_frame['hour'], bins = 24, color = '#a7c059', zorder = 3, histtype='bar', ec='#383632')
	ax0.set_title('Conversions by Time of Day \nTotal Conversions = {}'.format(new_frame.shape[0]))
	ax0.set_xlabel('Time of Day', fontsize = fonts)
	ax0.set_ylabel('Conversions', fontsize = fonts)

	plt.tight_layout()
	plt.savefig(newpath + 'ConversionsTimeOfDay-{}.png'.format(today))
	plt.show()

	fig, ax = plt.subplots(figsize = (10, 10))
	plt.grid(zorder = 0, linestyle = 'dashed', color = '#acaaa8')

def make_ad_dict(optimal):
		ad_list = []
		for path_name in optimal['paths_by_adname']:
		    for ad in path_name:
		        if ad not in ad_list:
		            ad_list.append(ad)
		            
		vals = [0] * len(ad_list)
		ads = dict(zip(ad_list, vals))
		for different_paths in optimal['paths_by_adname']:
		    for ad in different_paths:
		        ads[ad] += 1
		        
		ads = sorted(ads.items(), key = operator.itemgetter(1))[::-1]
		xvalues = range(1, len(ads) + 1)
		yvalues = [ad[1] for ad in ads]
		names = [str(ad[0]) for ad in ads]

		sums = []
		for index in range(len(yvalues)):
		    sums.append(sum(yvalues[0:index]))
		    
		disp_avg = sum([ad[1] for ad in ads])/float(len(ads))
		return xvalues, yvalues, disp_avg, names

def make_impressions_hist(big_frame):
	xvalues, yvalues, disp_avg, names = make_ad_dict(big_frame)
	ax = plt.bar(xvalues, 
	             yvalues,
	             ec='#383632',
	             color='#a7c059', 
	             zorder = 3)

	plt.axhline(y = disp_avg, 
	            zorder = 3, 
	            color = '#383632', 
	            linestyle = 'dashed', 
	            label = 'Avg Impressions({})'.format(round(disp_avg, 0)))

	plt.ylabel('Number of Impressions')
	# plt.xlabel('Ad Type')

	plt.xticks(xvalues, 
	           names, 
	           rotation = 90)


	plt.legend()
	plt.savefig(newpath + 'AdImpressions-Conversions_TAGID-{}.png'.format(today))
	plt.show()

if __name__ == '__main__':
	big_frame_path = r'/home/rafa/github/For Businesses/Infinite-Agency/Results-From-{}/big_frame-{}.csv'.format(today, today)
	if not os.path.exists(big_frame_path):
		big_frame = make_big_frame()
	else:
		big_frame = pd.read_csv(big_frame_path, low_memory = False)
	
	make_histogram_time_of_day(big_frame)
	make_impressions_hist(big_frame)