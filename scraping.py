from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


URL = "https://dic.nicovideo.jp/a/日常会話に使えるジョジョの奇妙な冒険の台詞集"

b = webdriver.Chrome(ChromeDriverManager().install())
b.get(URL)

article = b.find_element(By.CLASS_NAME, "article")
trs = article.find_elements(By.TAG_NAME, "tr")

parts = []
quotes = []
names = []
scenes = []
df = pd.DataFrame()

for (i, tr) in enumerate(trs):
	tds = tr.find_elements(By.TAG_NAME, "td")
	if 457 < i:
		break
	for (j, td) in enumerate(tds):
		if j == 0:
			parts.append(td.text)
		elif j == 1:
			quotes.append(td.text)
		elif j == 2:
			names.append(td.text)
		elif j == 3:
			scenes.append(td.text)


df["parts"] = parts
df["quotes"] = quotes
df["names"] = names
df["scenes"] = scenes

df.to_csv("data.csv")
print("done")
