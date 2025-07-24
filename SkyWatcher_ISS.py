import requests
from datetime import datetime
import time
import smtplib

Email = #Write your email here
Password = #Write the app pasword here

MY_LAT = #Your latitude
MY_LONG = #Your longitude

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 1, 
}

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour 
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False

while True:
    time.sleep(60)
    if is_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=Email, password=Password)
            connection.sendmail(
                from_addr=Email,
                to_addrs=#Your receiving Email,
                msg="Subject:Look Up\n\nThe ISS is just overhead."
            )