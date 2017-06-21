import numpy as np
import matplotlib.pyplot as plt
from bandits import Bandits
from banditstrategy import BanditStrategy
# Make plots look nice
plt.style.use('ggplot')


def sample_bandits(bandit_probs, choice_funcs, num_trials=1000, seed=42):
    ''' Sample bandits a give number of times with every choice function
    Print out the resulting number of wins for each choice strategy

    Parameters
    -----------
    bandit_probs : Array of floats (0 to 1)
        Indicates the underlying bandit probabilites
    choice_funcs : Array or List of str
        str indicating which choice functions to simulate
    num_trials : int (default=1000)
        Number of trials to conduct
    seed : int or None (default=42)
        Number to seed our BanditStrategy with for reproducibility
    '''
    print('True Bandit Probabilities: {}'.format(bandit_probs))
    for func in choice_funcs:
        bandits = Bandits(bandit_probs)
        strat = BanditStrategy(bandits, func, seed)
        strat.sample_bandits(num_trials)
        print("\t{} wins with {}".format(strat.wins.sum(), func))
    print('\n')


def regret(probabilities, choices):
    ''' Calculate the cumulative regret given an array of choices

    Parameters
    -----------
    probabilities : Array of floats (0 to 1)
        Indicating the underlying bandit probabilites
    choices : Array of int
        ints indicating which bandit was chosen at each round

    Returns
    --------
    Array of floats of the cumulative regret
    '''
    p_opt = np.max(probabilities)
    return np.cumsum(p_opt - probabilities[choices])


def plot_regret(bandit_probs, choice_funcs, num_trials=1000, seed=42):
    ''' Plots the cumulative regret for each choice function on single plot

    Parameters
    -----------
    bandit_probs : Array of floats (0 to 1)
        Indicates the underlying bandit probabilites
    choice_funcs : Array or List of str
        str indicating which choice functions to simulate
    num_trials : int (default=1000)
        Number of trials to conduct
    seed : int or None (default=42)
        Number to seed our BanditStrategy with for reproducibility

    Returns
    --------
    None
    Use plt.show() to view the resulting plot or plt.savefig() to save the plot
    '''
    # Create our figure object and axis
    fig, ax = plt.subplots(figsize=(10, 8))

    for func in choice_funcs:
        bandits = Bandits(bandit_probs)
        strat = BanditStrategy(bandits, func, seed)
        strat.sample_bandits(num_trials)
        bandit_regret = regret(bandit_probs, strat.choices.astype(int))
        ax.plot(bandit_regret, label=func)

    ax.legend(loc='best')
    ax.set_xlabel('Number of Trials')
    ax.set_ylabel('Regret')
    ax.set_title('Probabilities: {}, Seed: {}'.format(str(bandit_probs), seed))


def optimal_percent(probabilities, choices):
    ''' Calculate the percentage of optimal bandit choice over each iteration

    Parameters
    -----------
    probabilities : Array of floats (0 to 1)
        Indicating the underlying bandit probabilites
    choices : Array of int
        ints indicating which bandit was chosen at each round

    Returns
    --------
    Array of floats (0 to 1) indicating the percentage of optimal choice at any
        given choice iteration
    '''
    p_opt = np.max(probabilities)
    count_correct = np.cumsum(probabilities[choices] == p_opt)
    # Divide by the array [1, 2, ...] to get the average from the totals
    return count_correct / np.arange(1, len(choices) + 1).astype(float)


def plot_optimal_percent(bandit_probs, choice_funcs, num_trials=1000, seed=42):
    '''
    Plots the percentage of optimal bandit choice for each choice function on
    single plot

    Parameters
    -----------
    bandit_probs : Array of floats (0 to 1)
        Indicates the underlying bandit probabilites
    choice_funcs : Array or List of str
        str indicating which choice functions to simulate
    num_trials : int (default=1000)
        Number of trials to conduct
    seed : int or None (default=42)
        Number to seed our BanditStrategy with for reproducibility

    Returns
    --------
    None
    Use plt.show() to view the resulting plot or plt.savefig() to save the plot
    '''
    # Create our figure object and axis
    fig, ax = plt.subplots(figsize=(10, 8))

    for func in choice_funcs:
        bandits = Bandits(bandit_probs)
        strat = BanditStrategy(bandits, func, seed)
        strat.sample_bandits(num_trials)
        bandit_opt = optimal_percent(bandit_probs, strat.choices.astype(int))
        ax.plot(bandit_opt, label=func)

    ax.legend(loc='best')
    ax.set_xlabel('Number of Trials')
    ax.set_ylabel('Percent Correct')
    ax.set_title('Probabilities: {}, Seed: {}'.format(str(bandit_probs), seed))


if __name__ == '__main__':
    bandit_probs = [[0.1, 0.1, 0.1, 0.1, 0.9],
                    [0.1, 0.1, 0.1, 0.1, 0.12],
                    [0.1, 0.2, 0.3, 0.4, 0.5]]

    choice_functions = ['max_mean', 'random_choice',
                        'epsilon_greedy', 'softmax', 'ucb1', 'bayesian_bandit']

    ''' Question 2 '''
    for probs in bandit_probs:
        sample_bandits(probs, choice_functions)

    ''' Question 3 '''
    p_array = np.array([0.05, 0.03, 0.06])

    # Let's try with a variety of random seeds
    seeds = [1, 42, 360]
    for seed in seeds:
        plot_regret(p_array, choice_functions, seed=seed)
        plt.savefig('Question_3_seed_{}.png'.format(seed), dpi=300)
        plt.close()

    ''' Question 4 '''
    # Let's again plot using a variety of random seeds
    for seed in seeds:
        plot_optimal_percent(p_array, choice_functions, seed=seed)
        plt.savefig('Question_4_seed_{}.png'.format(seed), dpi=300)
        plt.close()
