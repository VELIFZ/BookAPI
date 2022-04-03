import requests as r
from .forms import Search

def getBookInfo():
    form = Search()
    res = r.get(f'https://www.googleapis.com/books/v1/volumes?q={form.name.data}').json()
    if res.status_code == 200:
        info = []
        for item in res['items']:
            try:
                title = item['volumeInfo']['title']
                published_date = item['volumeInfo']['publishedDate']
                description = item['volumeInfo']['description']
                publisher = item['volumeInfo']['publisher']
                image = item['volumeInfo']['imageLinks']['thumbnail']
                a = item['volumeInfo']['authors']
                for x in range(len(a)):
                    authors = a[x]
                #print([a[x] for x in range(len(a))])
                c = item['volumeInfo']['categories']
                for i in range(len(c)):
                    categories = c[i]
                info.append((title, published_date, description, publisher, image, authors, categories))
            except:
                print('')
            return info
    else:
        return res.status_code

