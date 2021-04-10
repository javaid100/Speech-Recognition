# =============== For Translator ================================

from googletrans import Translator

sentence = str(input("The sectence: "))

translator = Translator()

tr_sen = translator.translate(sentence, src='ur', dest='en')
s = tr_sen
print(tr_sen.text)

x = translator.translate(str(s), src='en', dest='ur')
print(x.text)
