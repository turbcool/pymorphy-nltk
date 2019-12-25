#0. Включаем в программу сторонние библиотеки:
import pymorphy2
import nltk
import string
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
#Эта штука докачивает нужные пакеты из интернета, если их у тебя нет:
nltk.download("punkt")
nltk.download("stopwords")

#1. Задаём исходный текст, с которым будем работать:
input_text = "Привет мир. Привет ещё раз. Привет! Тест програмы. Тест2. Да! Да? нет! К новому году я куплю килограмм мандаринов."
print("Исходный текст:")
print(input_text)

#2. Превращаем строку с исходным текстом в массив слов:
tokens = nltk.word_tokenize(input_text) #Вход - строка input_text, выход - массив слов.

#3. Осуществляем "токенизацию" - очищаем слова, чтобы остался только их корень ("токен")
 #Удаляет знаки пунктуации из каждого элемента в массиве:
tokens = [i for i in tokens if ( i not in string.punctuation )]
 #Удаляет слова-пустышки из массива слов:
stop_words = stopwords.words('russian')
stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', 'к', 'на'])
tokens = [i for i in tokens if ( i not in stop_words )]

print("Слова:")
print(tokens)

#4. Считаем сколько раз нам встретилось каждое слово:
count = {} #count - содержит пары значений [word: count]
for word in tokens: 
    #Для каждого слова:
    if (word not in count):
        #Мы не встречались с таким словом. Значит количество его вхождений равно 1.
        count[word]=1 #(добавляет пару значений [word: count])
    else:
        #Мы повторно встречаемся с уже добавленным словом:
        count[word]+=1 #(прибавляет 1 к count в паре значений [word: count])

print(count)
