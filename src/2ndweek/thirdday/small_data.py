import pandas as pd

url = "https://en.wikipedia.org/w/index.php?title=World_population&oldid=948301297"
dfs = pd.read_html(url)
print(dfs[12].head())