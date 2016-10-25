import pandas as pd

def readIncomeXls(url):
    return pd.read_excel(url, header=3, index_col="ZIP\ncode [1]")

