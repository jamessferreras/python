import tweepy
import random
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

krt_list = [	'The Daft Wee Ghostie ',
		'The Loch Ness Monster ',
		'A Wendigo ',
		'The Rake ',
		'Bloody Bones ',
		'Shane Madej ',
		'Harold the Scarecrow ',
		'Bloody Mary ',
		'Aaron Kelly ',
		'The Headless Horseman ',
		'The Goatman ',
		'The Jersey Devil ',
		'Lilith ',
		'Baba Yaga ',
		'Slenderman ',
		'Mothman ',
		'Bigfoot ',
		'The Chupacabra ',
		'Godzilla ' ]

covid_list = [	'ate a whole cake.',
		'started playing animal crossing.',
		'prayed for the pandemic to be over.',
		'baked homemade bread.',
		'learned to play the guitar.',
		'learned to speak french.',
		'layed in bed for 24 hours.',
		'cut their own hair.',
		'cut someone elses hair.',
		'bing watched Greys Anatomy.',
		'binge watched Supernatural.',
		'read all of Beastars.',
		'used Netflix Party with friends.',
		'called their mom.',
		'called their dad.',
		'is knitting a hat',
		'is starting a youtube channel.',
		'is getting fit.'
		'is growing out their hair.',
		'fell asleep on a zoom call.',
		'scrubbed their floors.',
		'dusted their apartment',
		'went through their clothes.']


#tweeting
x=0
y=5

while x < y:
	try:
		monster = random.choice(krt_list)
		activity = random.choice(covid_list)
		t = monster + activity
		print(t)
		api.update_status(status=t)
		x+=1
		sleep(30)

	except 	tweepy.TweepError as e:
		print(e.reason)
		sleep(2)



#likikng
i=0
while i<len(krt_list):
	for tweet in api.search(q=krt_list[i], lang="en", rppa=10):
		print("*")
		tweet.favorite()
		i+=1
exit()
