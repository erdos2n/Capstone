from bandits import Bandits
from banditstrategy import BanditStrategy

# bandits = Bandits([0.1, 0.1, 0.1, 0.1, 0.9])
# strat = BanditStrategy(bandits, 'ucb1')
# strat.sample_bandits(1000)
# print("Number of trials: ", strat.trials)
# print("Number of wins: ", strat.wins)
# print("Conversion rates: ", strat.wins / strat.trials)
# print("A total of %d wins of %d trials." % \
#     (strat.wins.sum(), strat.trials.sum()))
import numpy as np

choice_dict = ['max_mean', 'random_choice', 'epsilon_greedy', 'softmax',\
               'ucb1','bayesian_bandit']
def regret(probabilities, choices):
    '''
    INPUT: array of floats (0 to 1), array of ints
    OUTPUT: array of floats

    Take an array of the true probabilities for each machine and an
    array of the indices of the machine played at each round.
    Return an array giving the total regret after each round.
    '''
    p_opt = np.max(probabilities)
    return np.cumsum(p_opt - probabilities[choices])

for i in choice_dict:
    print i + '\n\n'
    bandits = Bandits([0.1, 0.1, 0.1, 0.1, 0.9])
    strat = BanditStrategy(bandits, i)
    strat.sample_bandits(1000)
    print("Number of trials: ", strat.trials)
    print("Number of wins: ", strat.wins)
    print("Conversion rates: ", strat.wins / strat.trials)
    print("A total of %d wins of %d trials." % \
        (strat.wins.sum(), strat.trials.sum()))

    print 'THIS IS THE REGRET' ,regret(strat.bandits, np.array(strat.choices))
