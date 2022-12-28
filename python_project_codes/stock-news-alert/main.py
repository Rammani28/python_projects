import requests
import datetime
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
daily_data = response.json()["Time Series (Daily)"]

prices = []
i = 0
for date in daily_data:
    prices.append(daily_data[date]["4. close"])
    i += 1
    if i == 2:
        break

yesterday_price = float(prices[0])
before_yesterday = float(prices[1])
percent = round((yesterday_price - before_yesterday) / before_yesterday * 100, 2)
if percent < 0:
    percent *= -1

if percent >= 5:
    print(f"yesterday's close: ${yesterday_price}")
    print(f"percent change: {percent}%\n")

    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": "Tesla",
        "searchin": "title"
    }
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    articles = response.json()['articles'][:4]

    messages = [f"Headline: {article['title']}.\nBrief: {article['description']}\n" for article in articles]
    for message in messages:
        print(message)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number.
    #HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

