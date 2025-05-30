import pandas as pd
import matplotlib.pyplot as plt

def analyze_publishers(df):
    top_pubs = df['publisher'].value_counts().head(10)
    top_pubs.plot(kind='barh', title="Top Publishers")
    plt.xlabel("Number of Articles")
    plt.show()

    if '@' in str(df['publisher'].iloc[0]):
        df['domain'] = df['publisher'].apply(lambda x: x.split('@')[-1] if '@' in x else x)
        print(df['domain'].value_counts().head())

if __name__ == "__main__":
    df = pd.read_csv('../data/TSLA_historical_data.csv')
    analyze_publishers(df)
