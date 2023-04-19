import pandas as pd
import numpy as np
import seaborn as sb

numerical = ['year', 'achievements', 'price', 'est_owners', # general information
            'num_categories', 'num_genres',  # imputed information
            'positive_ratings', 'negative_ratings', 'ratings_ratio', # dependent information
            'median_playtime']

categorical = ['mac', 'linux', 'Multi-player', 'Steam Achievements', 'Steam Trading Cards',
               'Indie', 'Action', 'Casual', 'Strategy', 'Simulation', 'Free to Play', 'kid_friendly', 'mature']

columns = categorical + numerical

def catplot_ylabel(g: sb.axisgrid.FacetGrid, fmt='{0:.0f}') -> sb.axisgrid.FacetGrid:
    # extract the matplotlib axes_subplot objects from the FacetGrid
    ax = g.axes.flat[0]

    # iterate through the axes containers
    for c in ax.containers:
        labels = [fmt.format(v.get_width()) for v in c]
        ax.bar_label(c, labels=labels, label_type='edge', padding=3)
    
    return g

def catplot_xlabel(g: sb.axisgrid.FacetGrid, fmt='{0:.0f}') -> sb.axisgrid.FacetGrid:
    # extract the matplotlib axes_subplot objects from the FacetGrid
    ax = g.axes.flat[0]

    # iterate through the axes containers
    for c in ax.containers:
        labels = [fmt.format(v.get_height()) for v in c]
        ax.bar_label(c, labels=labels, label_type='edge', padding=3)
    
    return g

def catplot_xpercent(data: pd.DataFrame, var: str, fmt='{0:.1%}') -> sb.axisgrid.FacetGrid:
    d = data[var].value_counts() / len(data)
    return catplot_xpercent_raw(d, var, fmt)

def catplot_xpercent_raw(data: pd.Series, var: str, fmt='{0:.1%}') -> sb.axisgrid.FacetGrid:
    g = sb.catplot(data=data.to_frame('percentage').reset_index(names=var), x=var, y='percentage', kind='bar')
    return catplot_xlabel(g, fmt=fmt)

def catplot_ypercent(data: pd.DataFrame, var: str, fmt='{0:.1%}') -> sb.axisgrid.FacetGrid:
    d = data[var].value_counts() / len(data)
    return catplot_ypercent_raw(d, var, fmt)

def catplot_ypercent_raw(data: pd.Series, var: str, fmt='{0:.1%}') -> sb.axisgrid.FacetGrid:
    g = sb.catplot(data=data.to_frame('percentage').reset_index(names=var), y=var, x='percentage', kind='bar')
    return catplot_ylabel(g, fmt=fmt)

def significant_digits(df: "Union[pd.DataFrame, pd.Series]", 
                       significance: int, 
                       inplace: bool = False
                       ) -> "Union[pd.DataFrame, pd.Series, None]":
    
    # Create a positive data vector with a place holder for NaN / inf data
    data = df.values
    data_positive = np.where(np.isfinite(data) & (data != 0),
                             np.abs(data),
                             10**(significance-1))

    # Align data by magnitude, round, and scale back to original
    magnitude = 10 ** (significance - 1 - np.floor(np.log10(data_positive)))
    data_rounded = np.round(data * magnitude) / magnitude

    # Place back into Series or DataFrame
    if inplace:
        df.loc[:] = data_rounded
    else:
        if isinstance(df, pd.DataFrame):
            return pd.DataFrame(data=data_rounded,
                                index=df.index,
                                columns=df.columns)
        else:
            return pd.Series(data=data_rounded, index=df.index)
        
def shorten(number):
    if number >= 1_000_000:
        return f'{number / 1_000_000:.0f}M'
    elif number >= 1_000:
        return f'{number / 1_000:.0f}K'
    elif number == 0:
        return '0'
    else:
        return f'{number / 1_000:.2f}K'