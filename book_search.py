# -*- coding: utf-8 -*-
import requests
from io import BytesIO
from PIL import Image
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from home.models import bookSearch


url = 'http://www.aladin.co.kr/ttb/api/ItemLookUp.aspx'
data = urllib.parse.urlencode({
    'ttbkey': '',
    'itemIdType': 'ISBN13',
    'ItemId': '9791170485131'# 플러터 스캔 기능으로 ISBN 받아옴.
})
con = urllib.request.urlopen(url + '?' + data)
objectXml = con.read()
con.close()

soup = BeautifulSoup(objectXml, features='xml')
result = soup.find('error')

# 에러가 아닌 경우.
if result is None:
    result_item = soup.find('item')

    book_result={
        'title':result_item.find('title').text,
        'author':result_item.find('author').text,
        'publisher':result_item.find('publisher').text,
        'pub_date':result_item.find('pub_date').text,
        'description':result_item.find('description').text,
        'cover':result_item.find('cover').text,

    }

    #item_result.append(book_result)
    bookSearch(
        title=book_result['title'],
        author=book_result['author'],
        publisher=book_result['publisher'],
        pub_date=book_result['pub_date'],
        description=book_result['description'],
        cover=book_result['cover']
    ).save()


else:
    print(result.find('errorMessage').text)

