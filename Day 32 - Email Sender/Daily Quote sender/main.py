import smtplib
import datetime as dt
import random

MY_EMAIL = "jpalominodevtest@gmail.com"
MY_PASSWORD = "kzepuvqvapcbfdxa"
now = dt.datetime.now()
day = now.weekday()

if day == 2:
    with open("quotes.txt","r") as file:
        data = file.readlines()
        quote = random.choice(data)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="jpalominodevtest@outlook.com",
            msg=f"Subject:Monday Motivation \n\n{quote}"
        )




