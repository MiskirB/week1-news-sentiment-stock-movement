# 📊 Tesla News Sentiment & Stock Movement Analysis

This project explores the relationship between **financial news sentiment** and **Tesla’s daily stock movements**, performed across 3 tasks:

1. **News Sentiment EDA**
2. **Technical Indicators (SMA, RSI)**
3. **Correlation Analysis between News Sentiment and Daily Stock Returns**

---

## 📁 Folder Structure

```
project-root/
│
├── data/
│   ├── raw_analyst_ratings.csv         # News headlines data
│   └── TSLA_historical_data.csv        # Historical TSLA stock prices
│
├── notebooks/
│   ├── 01_news_sentiment_eda.ipynb     # Task 1 notebook
│   ├── 02_technical_indicators.ipynb   # Task 2 notebook
│   └── 03_sentiment_vs_stock.ipynb     # Task 3 notebook
│
├── output/
│   ├── Articles Per Day.png
│   ├── Articles per Hour.png
│   ├── Headline Length Distribution.png
│   ├── RSI.png
│   ├── Tesla Close Price & SMA.png
│   ├── Avg Daily Sentiment and Stock Return.png
│   ├── Correlation Heatmap.png
│   └── Scatter Avg Sentiment and Stock Return.png
│
├── report/
│   └── final_report.docx               # Full report with visuals
│
├── README.md                           # This file
└── requirements.txt                    # Dependencies
```

---

## 📌 Task Summaries

### ✅ Task 1: News Sentiment Analysis

- Visualized article frequency per day and hour.
- Analyzed headline lengths and sentiment polarity.
- Extracted common keywords and publishers.
- Tools: `pandas`, `matplotlib`, `TextBlob`, `nltk`, `wordcloud`.

### ✅ Task 2: Technical Indicator Computation

- Calculated:
  - **Simple Moving Averages (SMA)**
  - **Relative Strength Index (RSI)**
- Overlayed indicators on TSLA price chart.
- Tools: `pandas_ta`, `matplotlib`, `seaborn`.

### ✅ Task 3: Sentiment vs Stock Return Correlation

- Conducted sentiment scoring of headlines.
- Calculated daily stock returns from closing prices.
- Correlation analyses:
  - Time-series plot
  - Pearson correlation coefficient: **0.0207**
  - P-Value: **0.3305** (statistically insignificant)
- Tools: `TextBlob`, `scikit-learn`, `scipy.stats`, `seaborn`.

---

## 📉 Conclusion

- Minimal correlation found between daily news sentiment and Tesla's daily returns.
- Suggests that either:
  - General sentiment models are not finance-specific enough.
  - Other factors (macroeconomics, fundamentals) dominate price action.

🔮 **Future work**:

- Explore FinBERT for financial sentiment.
- Include news volume, lag effects, and other stocks for broader analysis.

---

## ▶️ Setup Instructions

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🛠 Requirements

See `requirements.txt` for full versions.

- `pandas`, `numpy`
- `matplotlib`, `seaborn`
- `textblob`, `nltk`
- `pandas_ta`
- `scikit-learn`, `scipy`
- `wordcloud`, `jupyterlab`

---

## 📬 Author

- **Miskir Besir**
- Part of the **Nova Financial Modeling Challenge**
