import unicodedata as uni
import pandas as pd
from random import randint

SELECTED_PARTS = ["第1部", "第2部", "第3部", "第4部", "第5部"]
MAX_WIDTH = 18
data = pd.read_csv("data.csv")
parts = data["parts"]
quotes = data["quotes"]
names = data["names"]
scenes = data["scenes"]
length = len(parts)


def getQuoteIndex(length):
	while True:
		random_index = randint(0, length)
		if parts[random_index] in SELECTED_PARTS:
			return random_index


def trim_useless_text(text):
	text.replace("\n", "").replace("［", "").replace("］", "")
	return text


def makePadding(quote):
	length = len(quote)
	size = (MAX_WIDTH - length) // 2
	padding = "　" * size
	return padding


def strlen(text):
    count = 0
    for c in text:
        if uni.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count

def makeTweetText(quote, part, name, scene):
	tweet = "ﾆﾌﾞﾆﾌﾞﾆﾌﾞﾆﾌﾞﾆﾌﾞﾆﾌﾞﾆﾌﾞﾆﾌﾞﾆﾌﾞﾆﾌﾞﾆﾌﾞ" + "\n"
	tweet += makePadding(quote) + quote  + "\n"
	tweet += "ﾆﾌﾞﾆﾌﾞﾆﾌﾞﾆﾌﾞﾆﾌﾞﾆﾌﾞﾆﾌﾞﾆﾌﾞﾆﾌﾞﾆﾌﾞﾆﾌﾞ" + "\n"
	tweet += "(" + part + ": " + name + ")" + "\n\n"
	tweet += "【場面】" + "\n" + scene
	if 200 < strlen(tweet):
		tweet = tweet.replace("ﾆﾌﾞ", "") 
	return tweet


def trim_newline(index):
	quote = trim_useless_text(quotes[index])
	part = trim_useless_text(parts[index])
	name = trim_useless_text(names[index])
	scene = trim_useless_text(scenes[index])
	return quote, part, name, scene


def selectWord():
	index = getQuoteIndex(length)
	quote, part, name, scene = trim_newline(index)
	print(quote, part, name, scene)
	tweet = makeTweetText(quote, part, name, scene)
	return tweet
