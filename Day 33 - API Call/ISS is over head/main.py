import smtplib

import requests
from datetime import datetime

MY_LAT = -34.538640 # Your latitude
MY_LONG = -58.515850 # Your longitude
MY_EMAIL = "jpalominodevtest@gmail.com"
MY_PASSWORD = "kzepuvqvapcbfdxa"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour


# If the ISS is close to my current position
if iss_latitude == (MY_LAT - 5) or iss_latitude == (MY_LAT + 5) and iss_longitude == (MY_LONG - 5) or iss_longitude == (MY_LONG + 5):
    # and it is currently dark
    if time_now >= sunset or time_now <= sunrise:
        # Then send me an email to tell me to look up.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Look up the sky! \n\n is time to look up the ISS is here!"
            )
            print("Birthday card sent!")