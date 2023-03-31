from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

import time
import pandas as pd
import random

from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())

# f-string

keyword = input('검색어를 입력하시오 : ') # 바코드를 받음
yt_url = f'https://www.youtube.com/results?search_query={keyword}'
driver = wb.Chrome(service=service)
driver.get(yt_url)

# 브라우저 로드가 완료되기 위한 시간
time.sleep(2)

body = driver.find_element(By.TAG_NAME, value='body')

try:
    # 페이지 내 스크롤 높이 받아오기
    last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        # 임의의 페이지 로딩 시간 설정
        # PC환경에 따라 로딩시간 최적화를 통해 scraping 시간 단축 가능
        pause_time = random.uniform(1, 2)
        # 페이지 최하단까지 스크롤
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        # 페이지 로딩 대기
        time.sleep(pause_time)
        # 무한 스크롤 동작을 위해 살짝 위로 스크롤(i.e., 페이지를 위로 올렸다가 내리는 제스쳐)
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight-50)")
        time.sleep(pause_time)
        # 페이지 내 스크롤 높이 새롭게 받아오기
        new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
        # 스크롤을 완료한 경우(더이상 페이지 높이 변화가 없는 경우)
        if new_page_height == last_page_height:
            print("스크롤 완료")
            break

            # 스크롤 완료하지 않은 경우, 최하단까지 스크롤
        else:
            last_page_height = new_page_height

except Exception as e:
    print("에러 발생: ", e)

# selenium을 이용해서 HTML문서를 변환한 후에는 반드시 브라우저를 종료해야 한다!
html = bs(driver.page_source, 'lxml')
driver.close()

titleList = []
contentUrlList = []
reviewsList = []
dateList = []

for content in html.select('a#video-title'):
    title = content.get('title')
    content_url = 'https://www.youtube.com' + content.get('href')

    start_pos = content.get('aria-label').find('조회수') + 4
    end_pos = content.get('aria-label').rfind('회')

    reviews = content.get('aria-label')[start_pos:end_pos]

    titleList.append(title)
    contentUrlList.append(content_url)
    reviewsList.append(reviews)

#     print('영상제목:', title)
#     print('영상주소:', content_url)
#     print('조회수:', reviews)

# print(len(titleList))
# print(len(dateList))

date = html.select('div#metadata-line > span:nth-child(4)')

for i in range(len(date)):
    dateList.append(date[i].text.strip())
#     print('생성일자:',date[i])
#     print('-'*30)
# 유튜브 내용을 저장할 딕셔너리 생성
yt_dic = {
    '영상제목': titleList,
    '영상주소': contentUrlList,
    '조회수': reviewsList,
    '생성일자': dateList
}

# 데이터 프레임 생성
yt_df = pd.DataFrame(yt_dic)
# yt_df
# yt_df.to_csv('yt_df.csv', encoding='utf-8-sig', index=False)


#공백을 0으로 채움
yt_df['조회수']=yt_df['조회수'].replace('','0')
yt_df[yt_df['조회수']=='0']

#콤마 제거하기
yt_df['조회수']=yt_df['조회수'].astype(str).str.replace(',','')

yt_df=yt_df.astype({'조회수':'int'})

#조회수 많은 순으로 정렬
yt_df=yt_df.sort_values(by=['조회수'], ascending=False)

yt_df = yt_df.reset_index(drop=True)

max_ten_title=[]
max_ten_link=[]
max_ten_created=[]
max_ten_view=[]


for i in range(10):
    max_ten_title.append(yt_df['영상제목'][i])
    max_ten_link.append(yt_df['영상주소'][i])
    max_ten_created.append(yt_df['생성일자'][i])
    max_ten_view.append(yt_df['조회수'][i])


for i in range(10):
    print(str(i+1)+'.'+' '+max_ten_title[i]+':'+max_ten_link[i]+' , '+str(max_ten_view[i])+' , '+str(max_ten_created[i]))
