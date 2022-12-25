import requests
from datetime import datetime
import math
import smtplib
import time

MY_LAT = 27.708317
MY_LONG = 85.3205817


def is_close_enough():
    response1 = requests.get(url='http://api.open-notify.org/iss-now.json')
    response1.raise_for_status()

    data = response1.json()

    iss_position = {
        "latitude": float(data['iss_position']['latitude']),
        "longitude": float(data['iss_position']['longitude']),
    }
    print(iss_position)

    if math.fabs(iss_position['latitude'] - MY_LAT) < 5 and math.fabs(iss_position['longitude'] - MY_LONG < 5):
        return True
    else:
        return False


def is_dark():
    now = datetime.now()
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    if now.hour in range(sunrise, sunset + 1):
        return False
    else:
        return True


over = False
while not over:
    if is_dark() and is_close_enough():
        print("Send a letter now")
        SENDER = 'Rammani'
        MY_EMAIL = 'ktmcodebrewery@gmail.com'
        RECEIVER = "ktmcodebrewery@yahoo.com"
        APP_PASSWORD = 'jcfboqrovkuvezdu'

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(MY_EMAIL, APP_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=RECEIVER,
                                msg="Subject:ISS Over Your Head\n\nLook outside, the International Space Station is right "
                                    "over your head. See if you can figure out which one is the ISS")

    time.sleep(60)