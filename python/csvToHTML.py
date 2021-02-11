import pandas as pd

df = pd.read_csv('cities.csv')
print(df.head())

# create dataframe


# render dataframe as html
html = df.to_html()

with open('csv.html', 'w') as file:
    for i in html:
        file.write(i)