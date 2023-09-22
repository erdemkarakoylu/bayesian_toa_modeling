from pandas import DataFrame
import matplotlib.pyplot as pl

def plot_stats(dframe:DataFrame, name:str, ax=None):
    """Expects a stat description"""
    x = dframe.columns.to_list()
    if ax is None:
        f, ax = pl.subplots(nrows=2, figsize=(12, 10), sharex=True)
    else: f = None
    ax[0].plot(x, dframe.loc['mean', :], label='mean ' + name)
    ax[0].legend(fontsize=18)
    ax[0].set_title(name)
    ax[1].plot(x, dframe.loc['std', :], label='st. dev. ' + name)
    ax[1].legend(fontsize=18)
    ax[1].set_xticks('')
    return f, ax

def plot_together(dframes:tuple, names:tuple, ax=None):
    if ax is None:
        f, ax = pl.subplots(nrows=2, figsize=(12, 10), sharex=True)
    else: f = None
    for df, name in zip(dframes, names):
        f, ax = plot_stats(df.describe(), name=name, ax=ax)
    return f, ax
    