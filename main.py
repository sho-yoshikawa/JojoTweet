import tweepy
from passwd import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET
from select_word import selectWord

client = tweepy.Client(
	consumer_key=CONSUMER_KEY,
	consumer_secret=CONSUMER_SECRET,
	access_token=ACCESS_TOKEN,
	access_token_secret=ACCESS_SECRET
)

def tweet_serifu():
	tweet, tweet_en = selectWord()
	client.create_tweet(text=tweet)
	client.create_tweet(text=tweet_en)

while True:
	try:
		tweet_serifu()
		break
	except Exception as e:
		print(e)

print("*** done ***")
