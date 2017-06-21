import numpy as np
import pandas as pd
import random
from math import log, isnan
from collections import Counter, defaultdict


class Ad_Dictionary():
	"""
	Class that instantiates a dictionary class
	dataframe = Sizmek Data Frame Attribution Report

	functions:
		get_path_lst: will create the path list for each conversion
		make_diciontary: creates the dictionary of ads and lists
	"""

	def __init__(self):
		self.dataframe = pd.read_csv('Results-From-2017-06-01/big_frame-2017-06-01.csv')
		self.path_list = self.get_path_list()
		self.original_paths = []


	def get_path_list(self):
		path_lst = []
		for column in self.dataframe.columns:
			if 'PlacementID' in column:
				path_lst.append(column)

		paths_by_name = []
		for row in range(self.dataframe.shape[0]):
			path_name = []
			for item in range(len(path_lst)):
				if not isnan(self.dataframe.loc[row, path_lst[item]]):
					path_name.append(int(self.dataframe.loc[row, path_lst[item]]))
			paths_by_name.append(path_name)

		# for index, lst in enumerate(paths_by_name):
		# 	paths_by_name[index] = [value for value in lst if not isnan(value)]

		return paths_by_name

	def make_dictionary(self, passes = False, assists = False, points = True, threshold = 0):
		if passes and assists and points:
			ad_count_list = defaultdict(list)
			for ad_list in self.path_list:
				for index, ad in enumerate(ad_list):
					if index == len(ad_list) - 1:
						ad_count_list[ad].append(1)

					elif index == len(ad_list) - 2:
						ad_count_list[ad].append(0.8)   #assists = 0.2
					
					else:
						ad_count_list[ad].append(0.10) #assists = 0.0

		elif assists and points:
			ad_count_list = defaultdict(list)
			for ad_list in self.path_list:
				for index, ad in enumerate(ad_list):
					if index == len(ad_list) - 1:
						ad_count_list[ad].append(1)

					elif index == len(ad_list) - 2:
						ad_count_list[ad].append(0.2)   #self.assists = 0.2
					
					else:
						ad_count_list[ad].append(0) #assists = 0.3

		elif points:
			ad_count_list = defaultdict(list)
			for ad_list in self.path_list:
				for index, ad in enumerate(ad_list):
					if index == len(ad_list) - 1:
						ad_count_list[ad].append(1)
					else:
						ad_count_list[ad].append(0) 

		new_ad_list = defaultdict(list)
		for key, value in ad_count_list.iteritems():
			if len(value) > threshold:
				new_ad_list[key] = value

		self.ad_dict = new_ad_list
