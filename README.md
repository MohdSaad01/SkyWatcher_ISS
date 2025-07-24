# SkyWatcher_ISS
This project checks the current position of the ISS using the Open Notify API, compares it to your location, and checks if it’s nighttime at your coordinates using the Sunrise Sunset API. If the ISS is near and it’s dark enough to see it, the script sends you an email notification to remind you to look up!

📋 How It Works

1. Checks ISS current latitude and longitude.

2. Compares ISS position with your location within ±5 degrees.

3. Checks if it’s currently night at your location.

4. If both are true, sends an email alert using SMTP.
