from googletrans import Translator
trans = Translator()
res = trans.translate("震えるぞハート、燃え尽きるほどヒート", src="ja", dest="en")
print(res.text)
