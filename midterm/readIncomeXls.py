import pandas as pd

def readIncomeXls(url):
    return pd.read_excel(url, header=3, index_col="ZIP\ncode [1]")

# Even after reading it in with this function 
# this file requires some serious wrangling. 
# The zipcode is going to be read in as the index, but not all indeces are valid zipcodes.
# Transform the zipcode to a number by using pd.to_numeric(... errors='coerce')
# zipcs = ...
# then you can extract the valid rows as: 
# zipcs = zipcs[~np.isnan(zipcs)].astype(int)
# and to remove duplicate entries as list(set(zipcs))
