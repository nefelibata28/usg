import pandas as pd
import numpy as np

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