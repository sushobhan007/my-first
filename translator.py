from googletrans import Translator
sentence=str(input('Say..............'))
translator=Translator()
translated_sentence=translator.translate(sentence,src='en',dest='bn')
print(translated_sentence.text)
