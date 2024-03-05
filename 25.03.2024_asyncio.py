# реализоавтаь асинхронную программу, при запуске спросить у пользователя что он хочет(котиков или собачек или и то и то) спросить сколько картинок ему нужно, дальше необходимо выполнить асинхронный запрос к апи для получчения картинок, скачать их и сохранить в папку(укажет пользователь)
import json
import time
import requests
from bs4 import BeautifulSoup
import datetime
import csv
import asyncio
import aiohttp

interface = input("Вы хотите увидеть котиков или собачек? Введите cats или dogs: ")
numimg = int(input('Введите желаемое количество картинок: '))

access_template = ['number of images: {}']

print('\n' + '-' * 30)
print('{}'.format(interface))
print('\n'.join(access_template).format(numimg))

cats_data = []

dogs_data = []
async def get_page_data(session, page):
    headers = {
        "accept": "https://cdn2.thecatapi.com/images/c9j.jpg",
        "user-agent": "Mozilla/5.0 (X11: Lunix x68_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.147.125.252 Safari/537.36"
    }

    url = "https://cdn2.thecatapi.com/images/c9j.jpg={page}"

    async with session.get(url=url, headers=headers) as response:
        response_text = await response.text()

        soup = BeautifulSoup(response_text, "lxml")

        cats_items = soup.find("tbody", class_="products-table__boody").find_all("tr")

        for bi in cats_items:
            cats_data = bi.find_all("td")

            try:
                cat_title = cats_data[0].find("a").text.strip()
            except:
                cat_title = "Нет имени кота"

            try:
                cat_breed = cats_data[1].find("a").text.strip()
            except:
                cat_breed = "Нет породы кота"

            cats_data.append(
                {
                    "cat_title": cat_title,
                    "cat_breed": cat_breed
                }
            )
    finish_time = time.time() - start_time
    print(f"Затраченно на работу скрипта время: {finish_time}")

    cookies = {
        '_ga_F9QWXK982J': 'GS1.1.1709626282.1.0.1709626282.0.0.0',
        '_ga': 'GA1.1.1551017448.1709626282',
    }

    headers = {
        'authority': 'thecatapi.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': '_ga_F9QWXK982J=GS1.1.1709626282.1.0.1709626282.0.0.0; _ga=GA1.1.1551017448.1709626282',
        'referer': 'https://www.google.com/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    response = requests.get('https://thecatapi.com/', cookies=cookies, headers=headers)
    print(f"[INFO] Обработал станицу {page}")


async def get_page_data1(session, page):
    headers = {
        "accept": "https://random.dog/938d494d-71d1-4d76-9187-bcaa5c23c57d.PNG",
        "user-agent": "Mozilla/5.0 (X11: Lunix x68_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.147.125.252 Safari/537.36"
    }

    url = "https://random.dog/938d494d-71d1-4d76-9187-bcaa5c23c57d.PNG={page}"

    async with session.get(url=url, headers=headers) as response:
        response_text = await response.text()

        soup = BeautifulSoup(response_text, "lxml")

        dogs_items = soup.find("tbody", class_="products-table__boody").find_all("tr")

        for bi in dogs_items:
            dogs_data = bi.find_all("td")

            try:
                dog_title = dogs_data[0].find("a").text.strip()
            except:
                dog_title = "Нет имени собаки"

            try:
                dog_breed = dogs_data[1].find("a").text.strip()
            except:
                dog_breed = "Нет породы собаки"

            dogs_data.append(
                {
                    "dog_title": dog_title,
                    "dog_breed": dog_breed
                }
            )
    finish_time = time.time() - start_time
    print(f"Затраченно на работу скрипта время: {finish_time}")

    cookies = {
        '_ga': 'GA1.2.624293114.1709643402',
        '_gid': 'GA1.2.1212510832.1709643402',
        '_gat': '1',
        '_ga_T9FGK5RBRL': 'GS1.2.1709643402.1.0.1709643402.0.0.0',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': '_ga=GA1.2.624293114.1709643402; _gid=GA1.2.1212510832.1709643402; _gat=1; _ga_T9FGK5RBRL=GS1.2.1709643402.1.0.1709643402.0.0.0',
        'Referer': 'https://yandex.ru/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://random.dog/', cookies=cookies, headers=headers)

    print(f"[INFO] Обработал станицу {page}")

async def gather_data():
    headers = {
        "accept": "https://cdn2.thecatapi.com/images/c9j.jpg",
        "user-agent": "Mozilla/5.0 (X11: Lunix x68_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.147.125.252 Safari/537.36"
    }

    url = "https://cdn2.thecatapi.com/images/c9j.jpg={page}"

    async with aiohttp.ClientSession() as session:
        response = await session.get(url=url, headers=headers)
        soup = BeautifulSoup(await response.text(), "lxml")
        pages_count = int(soup.find("div", class_="pagination-numbers").find_all("a")[-1].text)

        tasks = []

        for page in range(1, pages_count + 1):
            task = asyncio.create_task(get_page_data(session, page))
            tasks.append(task)

        await asyncio.gather(*tasks)

def main():
    asyncio.run(gather_data())
    cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")

    with open(f"thecatapi_{cur_time}_async.json", "w") as file:
        json.dump(cats_data, file, indent=4, ensure_ascii=False)

    with open(f"thecatapi_{cur_time}_async.csv", "w") as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                "Имя кота",
                "Порода кота"
            )
        )

        for cat in cats_data:

            with open(f"thecatapi_{cur_time}_async.csv", "a") as file:
                writer = csv.writer(file)

                writer.writerow(
                    {
                        cat["cat_title"],
                        cat["cat_breed"]
                    }
                )

    finish_time = time.time() - start_time
    print(f"Затраченно на работу скрипта время: {finish_time}")

if __name__ == '__main__':
    main()


start_time = time.time()

def get_data():
    cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")
    with open(f"thecatapi_{cur_time}.csv", "w") as file:
        writer = csv.writer(file)

        writer.writerow(
            (
            "Имя кота",
            "Порода кота"
            )
        )

    headers = {
        "accept": "https://cdn2.thecatapi.com/images/c9j.jpg",
        "user-agent": "Mozilla/5.0 (X11: Lunix x68_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.147.125.252 Safari/537.36"
    }

    url = "https://cdn2.thecatapi.com/images/c9j.jpg=table"

    response = requests.get(url=url, headers = headers)
    soup = BeautifulSoup(response.text(), "lxml")

    pages_count = int(soup.find("div", class_="pagination-numbers").find_all("a")[-1].text)

    cats_data = []
    for page in range(1, pages_count + 1):
        url = "https://cdn2.thecatapi.com/images/c9j.jpg={page}"

        response = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(response.text(), "lxml")

        cats_items = soup.find("tbody", class_="products-table__boody").find_all("tr")

        for bi in cats_items:
            cats_data = bi.find_all("td")

            try:
                cat_title = cats_data[0].find("a").text.strip()
            except:
                cat_title = "Нет имени кота"

            try:
                cat_breed = cats_data[1].find("a").text.strip()
            except:
                cat_breed = "Нет породы кота"

            cats_data.append(
                {
                "cat_title": cat_title,
                "cat_breed": cat_breed
                }
            )

            with open(f"thecatapi_{cur_time}.csv", "a") as file:
                writer = csv.writer(file)

                writer.writerow(
                    (
                        cat_title,
                        cat_breed
                    )
                )

        print(f"Обработана {page}/{pages_count}")
        time.sleep(1)

    with open(f"thecatapi_{cur_time}.csv", "w") as file:
        json.dump(cats_data, file, indent=4, ensure_ascii=False)

def main():
    get_data()
    finish_time = time.time() - start_time
    print(f"Затраченно на работу скрипта время: {finish_time}")

if __name__ == '__main__':
    main()


for interface in range(numimg):
    if __name__ == '__main__':
        main()