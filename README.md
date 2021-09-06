# Sentiment Analysis of Customer Reviews On [Etsy.com](https://www.etsy.com)

## Run this app locally
- Install all dependencies listed in `requirements.txt`. 
- Run `app.py` to launch a local Dash server to host the Dash app. The Dash app opens in your default browser at [http://127.0.0.1:8050](http://127.0.0.1:8050).

## About the project
- The objective of this project is to build a machine learning model that analyses sentiment of reviews entered by customers on e-commerce website Etsy.
- **Data gathering & pre-processing:** A random sample of 792,000 reviews normally distributed across review ratings were selected out of 7 million reviews from [Amazon Review Dataset (2018)](https://nijianmo.github.io/amazon/) as raw data to train and examine on using different machine learning models and their performances.
- **Model Training:** The training sets were prepared using two different vectorization methods; Count Vectorization & TF-IDF Vectorization. And logistic regression was used to train the input data. Stop-words from English, Spanish & French languages were removed from the training set (based on frequency of said languages in the target dataset). 
- The TF-IDF Vectorized regression model had a test accuracy of 90.22%, which was used in this project.
- A total of 53,000 reviews were scraped from Etsy (Jewellery & Accessories section) using Python libraries Selenium & BeautifulSoup.
- `scrapeEtsyReviews.py` contains code used to scrape customer reviews from Etsy website (recommended to run the the file on Google Colab).
- Created an interactive web application using [Plotly Dash](https://plotly.com/dash/), HTML5 & CSS3.

### Application deployed on Heroku can be found [here](https://etsysentimentanalysis.herokuapp.com/).
