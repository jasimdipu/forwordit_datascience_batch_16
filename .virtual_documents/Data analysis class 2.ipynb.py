import pandas as pd


df = pd.read_csv("googleplaystore.csv")
df.head()


df.shape


df.dtypes


df.isna().sum()


df.info()


df.duplicated().sum()


df['App'].value_counts()


# drop app feature
df.drop("App", axis=1, inplace=True)


df.head()


# drop duplicates item
df.drop_duplicates(inplace=True)


df.duplicated().sum()


df['Category'].head()


df['Category'].tail()


df['Category'].value_counts()


df['Category'].unique()


df[df['Category'] == "1.9"]


df.drop(10472, axis=0, inplace=True)


df.loc[10470:10475]


sorted(df['Category'].unique())


len(df['Category'].unique())


# Label Encoding  # one hot encoding -> male 0 
                                    # female 1 
                                    # third


from sklearn.preprocessing import LabelEncoder


lb = LabelEncoder()


df['Category'] = lb.fit_transform(df['Category'])


df.head()


df.tail()


df['Category'].dtype


sorted(df['Category'].unique())


df['Rating'].head()


# check mean and median value
df["Rating"].mean()


df['Rating'].median()


df['Rating'].fillna(df["Rating"].mean(), inplace=True)


df['Rating'].isna().sum()


df["Rating"].mean()


df['Rating'].median()


df['Size'].head()


df['Size'].dtype


# for i in df['Size']:
#     if i[-1] == 'M':


df['Size'].str.strip().str[-1].unique()


# Installs
df['Installs'].head()


df['Installs'] = df['Installs'].apply(lambda x: x.replace("+", "") if x[-1] == '+' else x)
df['Installs'] = df['Installs'].apply(lambda x: x.replace(",", ""))


df['Installs'].head()


df['Installs'].dtype


df['Installs'] = df['Installs'].apply(lambda x: int(x))
df['Installs'].head()


df.columns


df['Type'].unique()


df['Type'].value_counts()


# One hot encoding
types = pd.get_dummies(df['Type'], prefix="Type", drop_first=True)


types.head()


df = pd.concat((df, types), axis=1)


df.head()


df['Price'][df['Price'] == "0"].count()


df['Price'][df['Price'] get_ipython().getoutput("= "0"]")


df['Content Rating'].unique()


# df.replace({'Content Rating' : {'Mature 17+': 'Everyone'}}, inplace=True)
df.replace({'Content Rating' : {'Everyone 10+': 'Teen'}}, inplace=True)


df['Content Rating'].unique()


df['Genres'].value_counts()


pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)


data_genres = df['Genres'].value_counts()


data_genres


data_genres_min = data_genres[data_genres < 21]


data_genres_min


df['Genres'] = df['Genres'].apply(lambda x: "other" if x in data_genres_min else x)


df['Genres'].value_counts()


len(df['Genres'].unique())


df.head()


df['Last Updated App'] = pd.to_datetime(df['Last Updated'])


df.head()


19m [-1] if == 'M" rem int(19*1024) x 
