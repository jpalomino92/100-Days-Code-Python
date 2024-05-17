import os
import requests
import smtplib
from datetime import date, timedelta, datetime
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
VANTAGE_KEY = os.environ.get("VANTAGE_KEY")
NEWS_KEY = os.environ.get("NEWS_KEY")
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

day_of_the_week = datetime.today()
today = date.today()
yesterday = str(today - timedelta(days=1))
day_before_str = str(today - timedelta(days=2))
stock_movement = 0


def get_stock_info():
    global stock_movement
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": VANTAGE_KEY
    }

    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    response.raise_for_status()
    stock_data = response.json()
    # TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
    yesterday_data = [(key, value) for key, value in stock_data['Time Series (Daily)'][yesterday].items()]
    # TODO 2. - Get the day before yesterday's closing stock price

    today_data = [(key, value) for key, value in stock_data['Time Series (Daily)'][day_before_str].items()]

    yesterday_closing_price = float(yesterday_data[3][1])
    day_before_closing_price = float(today_data[3][1])

    # TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
    stock_movement = ((yesterday_closing_price - day_before_closing_price) / day_before_closing_price) * 100

    # TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
    # TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
    # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


    if abs(stock_movement) >= 5:
        get_news()


def get_news():
    news_param = {
        "q": COMPANY_NAME,
        "from": yesterday,
        "sortBy": "popularity",
        "searchIn": "title",
        "apikey": NEWS_KEY
    }

    response = requests.get(NEWS_ENDPOINT, params=news_param)
    response.raise_for_status()
    news_data = response.json()
    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    new_articles = [{'title': item['title'], 'description': item['description']} for item in news_data["articles"][0:3]]
    send_alert(new_articles)


# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.


def send_alert(news):
    # TODO 9. - Send each article as a separate message via Twilio.
    for new in news:
        brief = new['description'].encode()
        headline = new['title'].encode()
        quote = f"""
            {STOCK_NAME}: {int(stock_movement)}%
            Headline: {headline}
            Brief:  {brief}
        
        """
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="jpalominodevtest@gmail.com",
                msg=f"Subject:Stock update {COMPANY_NAME} \n\n{quote}"
            )


# here we execute the function

if day_of_the_week.weekday() == 5 or day_of_the_week.weekday() == 6:
    print("is the weekend")
elif day_of_the_week == 1:
    yesterday = str(today - timedelta(days=3))
    day_before_str = str(today - timedelta(days=4))
    get_stock_info()
else:
    get_stock_info()

