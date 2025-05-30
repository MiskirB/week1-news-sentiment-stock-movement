import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(df, n=20):
    tfidf = TfidfVectorizer(stop_words='english', max_features=n)
    matrix = tfidf.fit_transform(df['headline'].dropna())
    print("Top keywords:", tfidf.get_feature_names_out())

if __name__ == "__main__":
    df = pd.read_csv('../data/raw_analyst_ratings.csv')
    extract_keywords(df)
