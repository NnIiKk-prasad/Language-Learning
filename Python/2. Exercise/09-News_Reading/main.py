# -----Akhbaar Padhke Sunaao-----
import requests
import json
from win32com.client import Dispatch


def speak(str):
    tell = Dispatch("SAPI.SpVoice")
    tell.Speak(str)


if __name__ == '__main__':
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=94a53d42a2d64fda92c90d8008922880'
    news = requests.get(url)
    news_dict = json.loads(news.content)
    arts = news_dict['articles']
    speak("News for today.. Let's begin")
    i = 1
    for article in arts:
        print(article['title'])
        speak(f"News number {i}: {article['title']}")
        i += 1
    speak("Thanks for listening.")
