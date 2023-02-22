from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


# 최신 크롬 드라이버 사용하도록 세팅: 현재 OS에 설치된 크롬 브라우저 버전에 맞게 cache에 드라이버 설치
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())


import time
import random
import pandas as pd


def scroll():
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

# 검색 키워드 설정: 키워드 내 띄어쓰기는 URL에서 '+'로 표시되기 때문에 이에 맞게 변환
SEARCH_KEYWORD = '잭 니콜라스 GC'.replace(' ', '+') # 잭 니콜라스  GC 부분 입력받도록

driver = webdriver.Chrome(service=service)
# 스크래핑 할 URL 세팅
URL = "https://www.youtube.com/results?search_query=" + SEARCH_KEYWORD
# 크롬 드라이버를 통해 지정한 URL의 웹 페이지 오픈
driver.get(URL)
# 웹 페이지 로딩 대기
time.sleep(3)
# 무한 스크롤 함수 실행
scroll()


# 페이지 소스 추출
html_source = driver.page_source
soup_source = BeautifulSoup(html_source, 'html.parser')


# 콘텐츠 모든 정보
content_total = soup_source.find_all(class_ = 'yt-simple-endpoint style-scope ytd-video-renderer')
# 콘텐츠 제목만 추출
content_total_title = list(map(lambda data: data.get_text().replace("\n", ""), content_total))
# 콘텐츠 링크만 추출
content_total_link = list(map(lambda data: "https://youtube.com" + data["href"], content_total))


#print(content_total)

#--------조회수 & 업로드 날짜 추출(Updated at 2022-10-11)--------#
content_record_src = soup_source.find_all(class_ = 'inline-metadata-item style-scope ytd-video-meta-block')
content_view_cnt = [content_record_src[i].get_text().replace('조회수 ', '') for i in range(0, len(content_record_src), 2)]
content_upload_date = [content_record_src[i].get_text() for i in range(1, len(content_record_src), 2)]

print(content_record_src)

print(f"content_total_title : {len(content_total_title)}, content_total_link: {len(content_total_link)}, content_view_cnt: {len(content_view_cnt)}, content_upload_date: {len(content_upload_date)}")

#for i in range(len(content_view_cnt)):
 #   print(content_total_title[i]+content_view_cnt[i])
#print(content_view_cnt)
#---------------------------------------------------------#

# 딕셔너리 포맷팅
content_total_dict = {'title'       : content_total_title,
                      'link'        : content_total_link,
                      'view'        : content_view_cnt,
                      'upload_date' : content_upload_date
                     }


df = pd.DataFrame(content_total_dict)
df.to_csv("content_total.csv", encoding='utf-8-sig')

