import numpy as np
import random


class Bandits(object):
    ''' This class represent n bandit machines.
    Methods
    --------
    pull(i) : Sample from the ith bandit
    Attributes
    -----------
    p_array : Array of probabilities (probability of conversion)
    _dict    : dictionary of ads (bandits) and their wins/loss array
    optimal : Index of the optimal bandit
    '''

    def __init__(self, _dict):
        '''
        Parameters
        -----------
        p_array : Array of probabilities to initialize bandits with
        '''
        self._dict = _dict

    def pull(self, i):
        ''' Sample from a given bandit
        Parameters
        -----------
        i : int indicating the index of a bandit
        Returns
        --------
        bool indicating whether the bandit returned a reward or not
        '''
        key = self._dict.keys()[i]
        num = random.choice(self._dict[key])
        return num

    def get_bandit_list(self, indices = []):
        """
        Input: list of indices for bandits used in the conversion process

        Returns: those keys in a list
        """
        bandit_list = []
        for index in indices:
            bandit_list.append(self._dict.keys()[index])
        return bandit_list

    def __len__(self):
     	return len(self._dict.keys())

