##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "jpalominodevtest@gmail.com"
MY_PASSWORD = "kzepuvqvapcbfdxa"

# 2. Check if today matches a birthday in the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()
month_now = now.month
day_now = now.day


for index,row in birthdays.iterrows():
    if row["month"] == month_now and row["day"] == day_now:
        name = row["name"]
        email = row["email"]
        random_letter_number = random.randint(1,3)
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/letter_{random_letter_number}.txt") as data:
            letter = data.read()

        new_letter = letter.replace("[NAME]",name)

        print(f"\nHappy birthday {name}! Your email is : {email}")

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:Happy birthday {name}! \n\n {new_letter}"
            )
            print("Birthday card sent!")




