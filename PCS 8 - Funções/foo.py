import numpy as np
import pandas as pd

price = pd.read_pickle("C:\\Users\\ricar\\Downloads\\yahoo_price.pkl")
returns = price.pct_change()
print(returns.tail())
