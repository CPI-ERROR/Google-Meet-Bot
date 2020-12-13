import json
from google_meet import GoogleMeet

# with open('credentials.json', 'r') as f:
#     credentials = json.load(f)

meet_bot = GoogleMeet("201951079@iiitvadodara.ac.in", "201951079", "/home/kapil/chromedriver_linux64/chromedriver")
meet_bot.attendMeeting()

