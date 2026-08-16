# Netflix Content Library Analysis

## Live Dashboard

[View the Interactive Streamlit Dashboard](https://netflixanalysis-9oujhdjb7w3rmbygblnrtt.streamlit.app/)

## GitHub Repository

This repository contains the complete analysis notebook, Streamlit dashboard,
dataset, and project documentation.

---

## 1. Project Overview

This project analyzes Netflix's publicly listed content catalog to understand
its content growth, content types, genres, and geographic distribution.

The analysis focuses on three key questions:

1. How has Netflix's content library changed over time?
2. What types and genres dominate Netflix's content library?
3. Which countries contribute the most titles?

---

## 2. Dataset

The project uses the **Netflix Movies and TV Shows** dataset available through
Kaggle.

The dataset contains information about Netflix titles, including:

- Title
- Content type
- Director
- Cast
- Country
- Date added
- Release year
- Rating
- Duration
- Genre/category
- Description

Dataset source:

https://www.kaggle.com/datasets/shivamb/netflix-shows

---

## 3. Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook / Google Colab

---

## 4. Data Cleaning

The following preprocessing steps were performed:

- Removed duplicate records.
- Converted `date_added` into datetime format.
- Created an `added_year` column for time-based analysis.
- Created an `added_month` column.
- Handled missing categorical values by replacing them with `Unknown`.
- Split multiple genres into individual categories for genre analysis.
- Split multiple countries into individual categories for geographic analysis.

These steps were performed to improve data consistency and make the dataset
suitable for exploratory analysis.

---

## 5. Analysis and Research Questions

### Question 1: How has Netflix's content library changed over time?

The number of titles added to Netflix was analyzed by year using the
`date_added` field.

**Key finding:**

The number of titles added varied across years, with the highest number of
titles added in **2019**. This indicates that Netflix's catalog expansion
was not uniform over time.

---

### Question 2: What types and genres dominate Netflix's content library?

The analysis compared Movies and TV Shows and examined the most frequently
listed genres.

**Key finding:**

Movies represented approximately **69.68%** of the catalog, while TV Shows
represented approximately **30.32**.

The most frequently listed genre was **International Movie**, followed by **Drama**
and **Comedies**.

These results indicate the genres with the strongest representation in the
publicly listed catalog.

---

### Question 3: Which countries contribute the most titles?

The `country` field was analyzed to identify the countries most frequently
associated with Netflix titles.

**Key finding:**

**united states** had the highest number of associated titles, followed by
**India** and **United kingdom**.

Because a single title can be associated with multiple countries, these
figures represent title-country associations rather than unique productions.

---

## 6. Overall Insights

The analysis shows that Netflix's publicly listed catalog has changed over
time and contains a substantial mix of Movies and TV Shows.

The catalog is also concentrated across several frequently represented
genres and countries, providing insight into the composition and geographic
distribution of Netflix's content.

However, catalog representation should not be interpreted as audience
preference or popularity because the dataset does not contain actual viewing
statistics.

---

## 7. Assumptions and Limitations

- The dataset represents Netflix's publicly listed catalog rather than actual
  viewing activity.
- The dataset does not contain streaming hours, revenue, subscriber behavior,
  or profitability data.
- A title can have multiple genres and countries, so these categories are not
  mutually exclusive.
- Missing information cannot always be reliably inferred and was therefore
  handled conservatively.
- The dataset represents a historical snapshot and may not reflect Netflix's
  current catalog.
- The analysis identifies patterns and associations but does not establish
  causation.

---

## 8. Project Structure

```text
netflix-content-analysis/
│
├── data/
│   └── netflix_titles.csv
│
├── notebooks/
│   └── netflix_analysis.ipynb
│
├── app.py
├── requirements.txt
└── README.md