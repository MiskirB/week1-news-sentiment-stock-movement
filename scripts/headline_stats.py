import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def headline_length_analysis(file_path):
    df = pd.read_csv(file_path)
    df['headline_length'] = df['headline'].apply(len)
    print(df['headline_length'].describe())

    plt.figure(figsize=(10, 5))
    sns.histplot(df['headline_length'], bins=30, kde=True)
    plt.title("Headline Length Distribution")
    plt.xlabel("Characters")
    plt.ylabel("Frequency")
    plt.show()

def price_distribution_analysis(file_path):
    df = pd.read_csv(file_path)
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df.dropna(subset=['Close'], inplace=True)

    plt.figure(figsize=(10, 5))
    sns.histplot(df['Close'], bins=30, kde=True)
    plt.title("Close Price Distribution")
    plt.xlabel("Price ($)")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    headline_length_analysis('../data/raw_analyst_ratings.csv')

