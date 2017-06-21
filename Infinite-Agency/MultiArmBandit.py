import numpy as np
from Bandits import Bandits
from BayesianBandit import Bayesian_Bandit
from Create_Dictionary import Ad_Dictionary
from plot_bar import plot_dictionaries
from BayesianBandit import regret
import matplotlib.pyplot as plt


thresholds = [100]
myGame = Ad_Dictionary()
results = []

for threshold in thresholds:
	myGame.make_dictionary(assists = False, passes = False, threshold = threshold)
	bandits = Bandits(_dict = myGame.ad_dict)
	strat = Bayesian_Bandit(bandits)
	strat.sample_bandits(100)
	# print("Number of trials: ", strat.trials)
	# print("Number of wins: ", strat.wins)
	# print("Conversion rates: ", strat.wins / strat.trials)
	# print("A total of %d wins of %d trials." %(strat.wins.sum(), strat.trials.sum())), '\n\n'

	result_dict = dict(zip(myGame.ad_dict.keys(), strat.wins))
	results.append(result_dict)
	for path in strat.used_paths:
		print path
	print regret(strat.final_probabilities, np.array(strat.choices))
	# xvals = range(len(strat.regret_list))
	# plt.plot(xvals, strat.regret_list)
	# plt.show()
	# for key, prob in zip(myGame.ad_dict.keys() ,strat.final_probabilities):
	# 	print key, '\t', prob
	# print '\n\n'

	# for path in strat.used_paths:
	# 	print path
	# print '\n\n'
	# print len(result_dict.keys())
	# for keys, values in result_dict.iteritems():
	# 	print keys, values

	# print '\n\n'
# plot_dictionaries(dicts = results, labels = thresholds)
