import time
import requests
import asyncio
import httpx


def fetch(lst):
    results = [requests.get(url) for url in lst]
    print(results)


async def fast_fetch(lst):
    async with httpx.AsyncClient() as client:
        req = [client.get(url) for url in lst]
        results = await asyncio.gather(*req)
    print(results)


urls = [
    'https://books.toscrape.com/catalogue/category/books/travel_2/index.html',
    'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html',
    'https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html',
    'https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html',
    'https://books.toscrape.com/catalogue/category/books/classics_6/index.html',
    'https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html',
    'https://books.toscrape.com/catalogue/category/books/romance_8/index.html',
    'https://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html',
    'https://books.toscrape.com/catalogue/category/books/fiction_10/index.html',
    'https://books.toscrape.com/catalogue/category/books/childrens_11/index.html',
    'https://books.toscrape.com/catalogue/category/books/religion_12/index.html',
    'https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html',
    'https://books.toscrape.com/catalogue/category/books/music_14/index.html',
    'https://books.toscrape.com/catalogue/category/books/default_15/index.html',
    'https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html',
    'https://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html',
    'https://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html',
    'https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html',
    'https://books.toscrape.com/catalogue/category/books/new-adult_20/index.html',
    'https://books.toscrape.com/catalogue/category/books/young-adult_21/index.html',
    'https://books.toscrape.com/catalogue/category/books/science_22/index.html',
    'https://books.toscrape.com/catalogue/category/books/poetry_23/index.html',
    'https://books.toscrape.com/catalogue/category/books/paranormal_24/index.html',
    'https://books.toscrape.com/catalogue/category/books/art_25/index.html',
    'https://books.toscrape.com/catalogue/category/books/psychology_26/index.html',
    'https://books.toscrape.com/catalogue/category/books/autobiography_27/index.html',
    'https://books.toscrape.com/catalogue/category/books/parenting_28/index.html',
    'https://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html',
    'https://books.toscrape.com/catalogue/category/books/humor_30/index.html',
    'https://books.toscrape.com/catalogue/category/books/horror_31/index.html'
]

start = time.perf_counter()

# fetch(urls)                   # 47.85777150001377
asyncio.run(fast_fetch(urls))   # 3.0143239999888465

end = time.perf_counter()
print(end - start)
