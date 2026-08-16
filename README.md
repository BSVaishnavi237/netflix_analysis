\# Netflix Content Library Analysis



\## Project Overview



This project analyzes Netflix's publicly listed content catalog to understand

content growth, content types, genres, and geographic distribution.



\## Research Questions



1\. How has Netflix's content library changed over time?

2\. What types and genres dominate Netflix's content library?

3\. Which countries contribute the most titles?



\## Dataset



The project uses the Netflix Movies and TV Shows dataset.



\## Tools Used



\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Streamlit

\- Google Colab / Jupyter Notebook



\## Data Cleaning



The dataset was cleaned by:



\- Removing duplicate records

\- Converting `date_added` into datetime format

\- Creating an `added_year` column

\- Handling missing categorical values using `Unknown`



\## Analysis



\### Question 1: Content Growth



Analyzed how the number of titles added to Netflix changed over time.



\### Question 2: Content Types and Genres



Compared Movies and TV Shows and identified the top genres.



\### Question 3: Geographic Distribution



Identified the countries most frequently associated with Netflix titles.



\## Key Findings



\- The number of Netflix titles added varied across the years. The highest

number of titles was added in 2019, while other years showed lower

levels of content additions. This indicates that Netflix's catalog

expansion was not uniform over time.

\- Movies represent 69.62% of the Netflix catalog, while TV Shows represent 30.38%. This shows that Movies/TV Shows form the larger share of the publicly listed catalog.Among the genres,       	International Movies is the most frequently listed category, followed by 	Dramas and Comedies. These genres therefore have a strong presence in Netflix's catalog.

However, genre frequency should not be interpreted as popularity because the dataset does not contain viewer or streaming data.

\- United Staes has the highest number of titles associated with it, followed by India and United kingdom. This indicates that Netflix's catalog has a strong geographic contribution from 	these countries.

However, a title can be associated with multiple countries, so these counts represent title-country associations rather than unique productions.

.



\## Limitations



\- The dataset represents catalog information rather than actual viewing data.

\- It does not contain revenue, subscriber or profitability information.

\- A title can be associated with multiple countries and genres.

\- The dataset represents a historical snapshot and may not reflect the current

 Netflix catalog.



\## How to Run the Dashboard



Install the required packages:



```bash

pip install -r requirements.txt







