import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def time_series(df):
    df['date'] = pd.to_datetime(df['date'])
    df['hour'] = df['date'].dt.hour

    df['date'].dt.date.value_counts().sort_index().plot(figsize=(14, 4))
    plt.title("Articles Per Day")
    plt.show()

    sns.countplot(x='hour', data=df)
    plt.title("Articles by Hour")
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('../data/TSLA_historical_data.csv')
    time_series(df)
