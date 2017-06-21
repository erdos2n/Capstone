import numpy as np
import random
from scipy.stats import beta 

class Bayesian_Bandit(object):
    '''
    Implements an online learning strategy to solve the Multi-Armed Bandit
      problem.
    Methods
    --------
    sample_bandits(n): sample and train on n pulls.
    Attributes
    -----------
    N : the cumulative number of samples
    choices : the historical choices as a (N,) array
    bb_score: the historical score as a (N,) array
    '''

    def __init__(self, bandits, seed=None, **kwargs):
        '''
        Initializes the BanditStrategy given an instance of the Bandits class
          and a choice function.
        Parameters
        -----------
        bandits : a Bandits object with a .pull method
        seed : int setting the random seed or None to not seed the random
            number generator
        Also supports passing keyword args which can be used in a
            particular choice function.  Namely 'epsilon_greedy' accepts
            epsilon=float and 'softmax' accepts tau=float
            e.g. strat = BanditStrategy(bandits, 'epsilon_greedy',
              epsilon=0.1)
        '''
        self.bandits = bandits
        n_bandits = len(self.bandits)
        self.wins = np.zeros(n_bandits)
        self.trials = np.ones(n_bandits)
        self.N = 1
        self.choices = []
        self.score = []
        self.used_paths = []
        self.seed = seed
        self.final_probabilties = []
        self.regret_list = []

    def sample_bandits(self, n=1):
        ''' Simulate n rounds of running the bandit machine
        Parameters
        -----------
        n : int number of rounds
        '''
        score = np.zeros(n)
        choices = np.zeros(n)

        # seed the random number generators so you get the same results every
        # time.
        if self.seed:
            np.random.seed(self.seed)
            random.seed(self.seed)

        attribution_paths = []
        bandit_list = []
        for k in range(n):
            #choose a bandit index according to the choice function
            choice = self._bayesian_bandit()

            #sample the chosen bandit
            result = self.bandits.pull(choice)
            bandit_list.append(choice)
            if result == 1:
                used_ads = self.bandits.get_bandit_list(bandit_list) 
                attribution_paths.append(used_ads)
                bandit_list = []

            #update priors and score
            self.wins[choice]   += result
            self.trials[choice] += 1
            score[k] = result
            self.N += 1
            choices[k] = choice
            probs = [round(i, 10) for i in self.wins / self.trials]
            reg   = regret(probs, np.array(choices))
            self.regret_list.append(reg)

        self.score = np.r_[self.score, score]
        self.choices = np.r_[self.choices, choices]
        self.used_paths = attribution_paths
        self.final_probabilities = [round(i, 3) for i in self.wins / self.trials]

    def _bayesian_bandit(self):
        '''
        Randomly sample from a beta distribution for each bandit and pick
        the one with the largest value
        Returns
        --------
        int : index of the winning bandit
        '''
        current_max = 0
        for i in range(len(self.wins)):
            alpha = 1 + self.wins[i]
            beta = 1 + (self.trials[i]-self.wins[i])
            betas = np.random.beta(alpha,beta)
            if np.max(betas) > current_max:
                current_max = np.max(betas)
                ix = i
        return ix

def regret(probabilities, choices):
    '''
    INPUT: array of floats (0 to 1), array of ints
    OUTPUT: array of floats
    Take an array of the true probabilities for each machine and an
    array of the indices of the machine played at each round.
    Return an array giving the total regret after each round.
    '''
    p_opt = np.max(probabilities)
    choices = [int(i) for i in choices]
    return sum([p_opt - probabilities[choice] for choice in choices])