from bs4 import BeautifulSoup
import pandas as pd


df = pd.read_csv(r"world_companies.csv")
print(df.head())
print(df.shape)
print(df.info())
