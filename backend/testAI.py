from simplegmail import Gmail
from simplegmail.query import construct_query
from regexes import replaceLinks
import google.generativeai as genai
from dotenv import load_dotenv
import os
import time

load_dotenv("gemini.env")
API_KEY = os.getenv('ENV_API_KEY')
genai.configure(api_key = API_KEY )
model = genai.GenerativeModel("gemini-1.5-flash")
print(model.generate_content("how long can a prompt be"))
print("-------")
print(model.generate_content(
''' Summarize this: Hi rofl,
You previously turned on the Timeline setting—formerly called Location
History —which helps you go back in time and remember where you’ve been.
With Timeline, your visits and routes are automatically saved to a map on
each of your devices.
Timeline is changing and will now be created on your device. As part of
this, you'll need to choose settings for your data
[link]
*by
December 1, 2024* to avoid losing visits and routes.
How it works
Like before, your devices will continue to save your visits in Timeline
when this setting is on. But starting today, if you're signed in on
multiple smartphones, each device will save new visits on its own Timeline.
What you need to do
*If you’d like to keep your saved visits and routes,* choose your settings
[link]
on your preferred smartphone by *December 1, 2024*. (You may first need to
update the Google Maps app.)
After you do this, you’ll only be able to use Timeline in the app.
*If you take no action, you may lose data.* Google will try moving up to 90
days of Timeline data to the first signed-in device you use after
*December 1, 2024*. Your older data will be deleted. Timeline will also
remain on for your account, and your devices will continue saving new
visits. Your visits and routes older than 3 months will be auto-deleted.
Review & choose settings
[link]
If you don’t want any Timelines on your devices, you can turn off this
setting and delete your data in Activity controls
[link].

Your Timeline data
6
Countries/​Regions
[link]
17
Cities
[link]
346
Places
[link]
Go
to your Timeline
[link]
About Timeline
Timeline helps you go back in time, and remember where you've been, by
automatically saving your visits and routes to a map on each of your
devices. To learn more about Timeline, visit the Help Center
[link].
You received this email to let you know about important changes to your
Google Account and services.
Google LLC
1600 Amphitheatre Parkway, Mountain View, CA 94043'''
))
# model = genai.GenerativeModel('gemini-1.5-flash')
# response = model.generate_content('Teach me about how an LLM works')

# print(response.text)
