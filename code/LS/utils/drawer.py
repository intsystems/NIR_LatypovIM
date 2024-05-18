import matplotlib.pyplot as plt
import numpy as np

def plot_ratios(ratios, gammas, max_budgets, x1, y1, l1, used_budgets = None, **kwargs):
    ratios = 1/ ratios
    ratios_stat = np.array([(np.mean(r), np.std(r)) for r in ratios]).T
    gm = (1 - np.array(gammas)) #1/(1 - np.array(gammas))

    fig, ax = plt.subplots(1,3, figsize = (16, 4))
    colors = np.linspace(0, 2., len(gm))
    ax[0].scatter(gm , ratios_stat[0], c = colors, ec = 'k')
    ax[0].fill_between(gm , ratios_stat[0] - ratios_stat[1], ratios_stat[0] + ratios_stat[1], alpha = 0.2)

    ax[0].set_xlabel(l1, fontsize = 15)
    ax[0].set_ylabel(y1, fontsize = 15)

    ax[1].scatter(max_budgets, ratios_stat[0], c = colors, ec = 'k')
    ax[1].fill_between(max_budgets, ratios_stat[0] - ratios_stat[1], ratios_stat[0] + ratios_stat[1], alpha = 0.2)
    
    if used_budgets is not None:
        ax[1].axvline(used_budgets.min(),linewidth=2, color='r')
        # ax[1].axvline(used_budgets.max(),linewidth=2, color='r')

    ax[1].set_xlabel(x1, fontsize = 14)
    ax[1].set_ylabel(y1, fontsize = 14)
    
    # ax[2].plot(max_costs, gammas)
    ax[2].scatter(max_budgets, gm , c= colors, ec='k')

    ax[2].set_xlabel(x1, fontsize = 15)
    ax[2].set_ylabel(l1, fontsize = 15)
    for i in range(3):
        ax[i].grid()
    return fig