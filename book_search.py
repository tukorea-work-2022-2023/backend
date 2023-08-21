# -*- coding: utf-8 -*-
import requests
from io import BytesIO
from PIL import Image
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


def barcode_book(id):
    url = 'http://www.aladin.co.kr/ttb/api/ItemLookUp.aspx'
    data = urllib.parse.urlencode({
        'ttbkey': 'ttbekgml75842102001',
        'itemIdType': 'ISBN13',
        'ItemId':id #'9791170485131'# 플러터 스캔 기능으로 ISBN 받아옴.
    })
    con = urllib.request.urlopen(url + '?' + data)
    objectXml = con.read()
    con.close()

    soup = BeautifulSoup(objectXml, features='xml')
    result = soup.find('error')

    # 에러가 아닌 경우.
    if result is None:
        result_item = soup.find('item')
        print(result_item)
        book_result={
            'title':result_item.find('title').text,
            'author':result_item.find('author').text,
            'publisher':result_item.find('publisher').text,
            'pubdate':result_item.find('pubDate').text,
            'description':result_item.find('description').text,
            'price': result_item.find('priceStandard').text,
            'cover':result_item.find('cover').text,

        }

        return book_result

    else:
        error=result.find('errorMessage').text
        return error

