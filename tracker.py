import requests
from bs4 import BeautifulSoup
from plyer import notification


def notifyMe(title, content):
    notification.notify(
        title=title,
        message=content,
        app_icon="cd/home/asus/PycharmProjects/covid_tracker/icon.ico",
        timeout=1
    )


# notifyMe("It Works 🔥🔥🔥", "This is the content"
numbers = []

if __name__ == "__main__":
    # for i in range(100):
    data = requests.get('https://www.mohfw.gov.in/')
    soup = BeautifulSoup(data.text, 'html.parser')

    for text in soup.find_all('ul')[6].find_all('strong'):
        numbers.append(text.text)

    print(numbers)
    # text = text.text.split("\n")
    # print(text)
    notifyMe("Covid 19 updates",
             f"Active: {numbers[0]}\nRecovered: {numbers[1]}\nDeaths: {numbers[2]}\nMigrated: {numbers[3]}")
    print("Successful 🔥🔥🔥")
