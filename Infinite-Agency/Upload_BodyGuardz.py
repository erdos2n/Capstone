import os, sys
import glob
import pandas as pd
import numpy as np
import scipy.special
import operator
import glob
from collections import Counter, defaultdict
from time import time
import datetime
# import matplotlib.pyplot as plt
# import matplotlib
# import bokeh
# from bokeh.charts import Histogram, defaults, vplot, hplot, show, output_file


# font = {'family' : 'monospace',
#         'weight' : 'medium',
#         'size'   : 24}

# matplotlib.rc('font', **font)

today = str(datetime.date.today())

newpath = r'/home/rafa/github/For Businesses/Infinite-Agency/Results-From-{}/'.format(today)
if not os.path.exists(newpath):
    os.makedirs(newpath)

def make_big_frame():
    """
    big_frame is every .csv file stacked on top of one another from the directory
    
    path = full file path
    
    it also prints if the columns were of equal length
    """
    
    # pull each csv into a list
    dfs = []
    #insert path here
    #put in fullpath to file, and filetype = csv, txt, etc.
    path = "/home/rafa/github/For Businesses/Infinite-Agency/BG/*.csv" 
    count = 0
    for fname in glob.glob(path):
        count += 1
        print 'file number:{}'.format(count)
        dfs.append(pd.read_csv(fname, low_memory=False))
    
    # creates a set of their column lengths
    shape_set = set([df.shape[1] for df in dfs])
    big_frame = pd.concat(dfs, ignore_index = True, axis = 0)
    
    if len(shape_set) > 1:
        print 'Unequal Columns!'
    else:
        print 'Columns are equal length :)\n Shape = {}'.format(big_frame.shape)
 
	big_frame.dropna(axis = 1, how = 'all', inplace=True)
	drop_nonunique(big_frame)
	print 'concat is complete: shape = {}'.format(big_frame.shape)
	big_frame.drop_duplicates(inplace = True, subset = ['ConversionID'])
	big_frame.drop_duplicates(inplace = True, subset = ['ConversionID'])
	big_frame.reset_index(inplace=True)

	print 'Deleted duplicates and Reset Index, new shape = {}'.format(big_frame.shape)
	date_list = make_datelist(big_frame)
	big_frame = change_date(big_frame, date_list)
	big_frame = make_path_columns(big_frame)
	return big_frame





def make_datelist(big_frame):
    datelist = []
    for column in big_frame.columns:
        if 'Date' in column:
            datelist.append(column)
    return datelist

def change_date(big_frame, datelist):
    datelist = []
    for column in datelist:
        big_frame[column] = pd.to_datetime(big_frame[column], infer_datetime_format=False)
    return big_frame

def drop_nonConversions(big_frame, datelist):
    for column in datelist:
        if column != 'ConversionDate':
        	big_frame.drop(column, axis=1, inplace=True)


def drop_nonunique(big_frame):
    for column in big_frame.columns:
        if len(big_frame[column].unique()) == 1:
            big_frame.drop(column, axis=1, inplace=True)
    return big_frame


# def make_new_columns(big_frame):
# 	natural_list = []
# 	for column in big_frame.columns:
# 	    if 'atural' in column:
# 	        natural_list.append(column)

	
def make_path_columns(big_frame):
	time_list = []
	for datetimes in big_frame['ConversionDate']:
	    time_list.append(int(datetimes[11:13]))


	path_lst = []
	for column in big_frame.columns:
	    if 'PlacementID/SearchKeywordID' in column:
	        path_lst.append(column)

	paths_by_name = []
	for row in range(big_frame.shape[0]):
	    path_name = []
	    for item in range(len(path_lst)):
	        path_name.append(big_frame.loc[row, path_lst[item]])
	    paths_by_name.append(path_name)

	for index, path in enumerate(paths_by_name):
	    paths_by_name[index] = [int(node) for node in path if node <= 300000000]

	print 'Making Clean Paths File for {}'.format(today)
	clean_paths = open(newpath + 'clean_paths-{}.txt'.format(today), 'w')
	for i in paths_by_name:
	    clean_paths.write('%s \n' %i)
	print 'Clean Paths File Has Been Made!'


	path_lengths = [len(path) for path in paths_by_name]
	big_frame['path_lengths'] = path_lengths
	big_frame['paths_by_adname'] = paths_by_name
	big_frame['hour'] = time_list

	print 'Making big_frame file for {}'.format(today)
	big_frame.to_csv(newpath + 'big_frame-{}.csv'.format(today))

	return big_frame

# def get_subset(big_frame):
# 	state_list = big_frame['State-Region'].unique()
# 	new_frame = big_frame[['ConversionID','BrowserType', 'OperatingSystemType', 'DeviceType','path_lengths', 'paths_by_adname', 'State-Region', 'hour']]
# 	smaller_frames = []
# 	for states in state_list:
# 	    smaller_frames.append(new_frame[new_frame['State-Region'] == states])
	    
# 	after_hours = new_frame[(new_frame['hour'] < 10) | (new_frame['hour'] > 22)].sort_values(by = ['path_lengths'])
# 	during_hours = new_frame[(new_frame['hour'] > 10) & (new_frame['hour'] < 22)].sort_values(by = ['path_lengths'])

# 	new_frame['hour'].count()

# 	return new_frame



# def make_histogram_ad_impressions(new_frame):
# 	ad_list = []
# 	for path_name in optimal['paths_by_adname']:
# 	    for ad in path_name:
# 	        if ad not in ad_list:
# 	            ad_list.append(ad)
	            
# 	vals = [0] * len(ad_list)
# 	ads = dict(zip(ad_list, vals))
# 	for different_paths in optimal['paths_by_adname']:
# 	    for ad in different_paths:
# 	        ads[ad] += 1
	        
# 	ads = sorted(ads.items(), key = operator.itemgetter(1))[::-1]
# 	xvalues = range(1, len(ads) + 1)
# 	yvalues = [ad[1] for ad in ads]


# 	fig, ax = plt.subplots(figsize = (10, 10))
# 	plt.grid(zorder = 0, linestyle = 'dashed', color = '#acaaa8')


# 	ax = plt.bar(xvalues, 
# 	             yvalues,
# 	             ec='#383632',
# 	             color='#a7c059', 
# 	             zorder = 3)

# 	plt.axhline(y = disp_avg, 
# 	            zorder = 3, 
# 	            color = '#383632', 
# 	            linestyle = 'dashed', 
# 	            label = 'Avg Impressions({})'.format(round(disp_avg, 0)))

# 	plt.ylabel('Number of Impressions')
# 	# plt.xlabel('Ad Type')

# 	plt.xticks(xvalues, 
# 	           names, 
# 	           rotation = 90)


# 	plt.legend()
# 	plt.savefig(newpath + 'AdImpressions-Conversions_TAGID-{}.png'.format(today))
# 	plt.show()

# def make_histogram_path_length(big_frame):
# 	f, (ax0) = plt.subplots(1, 1, figsize = (10, 10))

# 	ax0.grid(zorder = 0, linestyle = 'dashed', color = '#acaaa8')
# 	ax0.hist(big_frame['path_lengths'], 
# 	         bins = 30, 
# 	         color = '#a7c059', 
# 	         zorder = 3, 
# 	         histtype='bar', 
# 	         ec='#383632', 
# 	         label = '')


# 	ax0.set_title('Histogram \n Number of Paths')
# 	ax0.set_xlabel('Path Length', fontsize = fonts)
# 	ax0.set_ylabel('Number of People', fontsize = fonts)


# 	plt.axhline(y = big_frame['path_lengths'].mean(), 
# 	            zorder = 3, 
# 	            color = '#383632', 
# 	            linestyle = 'dashed', 
# 	            label = 'Avg Length = {}'.format(round(big_frame['path_lengths'].mean(), 0)))

# 	plt.legend()
# 	plt.savefig(newpath + 'PathLengths-{}.png'.format(today))

if __name__ == '__main__':
	big_frame = make_big_frame()
