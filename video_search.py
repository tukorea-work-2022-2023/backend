import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='dahee1228!', db='crawling_video', charset='utf8')
cursor = conn.cursor()

def crawling_video_db(keyword,video_list):
    if 'C언어'==keyword:
        cursor.execute("DROP TABLE crawling_video.CLanguage_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.CLanguage_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.CLanguage_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif '파이썬'==keyword:
        cursor.execute("DROP TABLE crawling_video.python_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.python_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.python_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif '자바'==keyword:
        cursor.execute("DROP TABLE crawling_video.java_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.java_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.java_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif 'SQL'==keyword:
        cursor.execute("DROP TABLE crawling_video.sql_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.sql_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.sql_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif 'HTML+CSS+자바스크립트'==keyword:
        #cursor.execute("DROP TABLE crawling_video.html_videos")
        #conn.commit()
        cursor.execute("CREATE TABLE crawling_video.html_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.html_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif '코틀린'==keyword:
        cursor.execute("DROP TABLE crawling_video.cotlin_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.cotlin_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.cotlin_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif 'IT 트렌드'==keyword:
        cursor.execute("DROP TABLE crawling_video.it_trend_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.it_trend_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.it_trend_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif '개발자 면접'==keyword:
        cursor.execute("DROP TABLE crawling_video.interview_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.interview_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.interview_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif '백엔드'==keyword:
        cursor.execute("DROP TABLE crawling_video.backend_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.backend_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.backend_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif '프론트엔드'==keyword:
        cursor.execute("DROP TABLE crawling_video.frontend_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.frontend_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.frontend_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif '앱개발'==keyword:
        cursor.execute("DROP TABLE crawling_video.app_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.app_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.app_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif '정보보안'==keyword:
        cursor.execute("DROP TABLE crawling_video.security_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.security_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.security_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif 'Spring Boot'==keyword:
        #cursor.execute("DROP TABLE crawling_video.springboot_videos")
        #conn.commit()
        cursor.execute("CREATE TABLE crawling_video.springboot_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.springboot_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif '스프링 프레임워크'==keyword:
        cursor.execute("DROP TABLE crawling_video.springframework_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.springframework_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.springframework_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif 'Python Django'==keyword:
        cursor.execute("DROP TABLE crawling_video.django_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.django_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.django_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif 'Python Flask'==keyword:
        cursor.execute("DROP TABLE crawling_video.flask_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.flask_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.flask_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif 'Node.js'==keyword:
        cursor.execute("DROP TABLE crawling_video.nodejs_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.nodejs_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.nodejs_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif 'React.js'==keyword:
        cursor.execute("DROP TABLE crawling_video.react_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.react_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.react_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif 'Vue.js'==keyword:
        cursor.execute("DROP TABLE crawling_video.vue_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.vue_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.vue_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif 'Angular'==keyword:
        cursor.execute("DROP TABLE crawling_video.Angular_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.Angular_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.Angular_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif 'jQuery'==keyword:
        cursor.execute("DROP TABLE crawling_video.jQuery_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.jQuery_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.jQuery_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif 'React Native'==keyword:
        cursor.execute("DROP TABLE crawling_video.reactnative_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.reactnative_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.reactnative_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif '플러터'==keyword:
        cursor.execute("DROP TABLE crawling_video.flutter_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.flutter_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.flutter_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif '모의해킹'==keyword:
        cursor.execute("DROP TABLE crawling_video.hacker_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.hacker_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.hacker_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif '보안관제'==keyword:
        cursor.execute("DROP TABLE crawling_video.cert_videos")
        conn.commit()
        cursor.execute("CREATE TABLE crawling_video.cert_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.cert_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()
    elif 'CS지식'==keyword:
        #cursor.execute("DROP TABLE crawling_video.cs_videos")
        #conn.commit()
        cursor.execute("CREATE TABLE crawling_video.cs_videos (title text, url text, view int, date text)")
        conn.commit()
        for i in range(len(video_list)):
            title = video_list[i]['ten_title']
            url = video_list[i]['ten_link']
            view=video_list[i]['ten_view']
            date=video_list[i]['ten_created']
            cursor.execute(
                f"INSERT INTO crawling_video.cs_videos VALUES(\"{title}\",\"{url}\",\"{view}\",\"{date}\")")
            conn.commit()


from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

import time
import pandas as pd
import random

from selenium.webdriver.chrome.service import Service

service = Service()

# f-string

language = ['C언어', '파이썬', '자바', 'sql', '코틀린']

it_trend = ['IT 트렌드']

interview = ['개발자 면접']

job = ['백엔드', '프론트엔드', '앱개발', '정보보안']

backend = ['spring boot', '스프링 프레임워크', 'Python Django', 'Python Flask', 'Node.js']

frontend = ['react', 'vue', 'Angular', 'jQuery']

app = ['React Native', '플러터']

security = ['모의해킹', '보안관제']

#cs_know = ['CS지식']

front = ['React.js', 'Vue.js']


# 10개의 목록이 나올 때까지 크롤링
def video_list_search(name):
    video_list = crawling(name)
    while len(video_list) < 10:
        video_list = crawling(name)
    crawling_video_db(name, video_list)
    print(video_list)
    return video_list


# 크롤링 작업
def crawling(name):
    keyword = name  # input('검색어를 입력하시오 : ') # 바코드를 받음
    yt_url = f'https://www.youtube.com/results?search_query={keyword}'

    options = wb.ChromeOptions()
    options.add_argument('start-maximized')  # 크롬 최대화
    options.add_experimental_option("excludeSwitches", ["enable-logging"])  # [Chrome이 자동화된 테스트 소프트웨어에 의해 제어되고 있습니다.] 제거

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
    driver.delete_all_cookies()
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

    try:
        # 데이터 프레임 생성
        global yt_df
        yt_df = pd.DataFrame(yt_dic)

    # yt_df
    # yt_df.to_csv('yt_df.csv', encoding='utf-8-sig', index=False)

    finally:
        # 공백을 0으로 채움
        yt_df['조회수'] = yt_df['조회수'].replace('', '0')
        yt_df[yt_df['조회수'] == '0']

        # 콤마 제거하기
        yt_df['조회수'] = yt_df['조회수'].astype(str).str.replace(',', '')

        yt_df = yt_df.astype({'조회수': 'int'})

        try:
            # 1차 크롤링 : 키워드가 들어있는 영상 필터링
            yt_df = yt_df[yt_df['영상제목'].str.contains(keyword)]

        finally:
            # 2차 크롤링 : 조회수 많은 순으로 정렬
            yt_df = yt_df.sort_values(by=['조회수'], ascending=False)

            yt_df = yt_df.reset_index(drop=True)

            max_ten_title = []
            max_ten_link = []
            max_ten_created = []
            max_ten_view = []

            video_list = []

            try:
                for i in range(10):
                    max_ten_title.append(yt_df['영상제목'][i])
                    max_ten_link.append(yt_df['영상주소'][i])
                    max_ten_created.append(yt_df['생성일자'][i])
                    max_ten_view.append(yt_df['조회수'][i])

                # 딕셔너리로 묶어버리기
                for i in range(10):
                    print(str(i + 1) + '.' + ' ' + max_ten_title[i] + ':' + max_ten_link[i] + ' , ' + str(
                        max_ten_view[i]) + ' , ' + str(max_ten_created[i]))

            finally:

                try:
                    for i in range(10):
                        # 딕셔너리 형태로 저장
                        video_dict = {
                            'ten_title': max_ten_title[i],
                            'ten_link': max_ten_link[i],
                            'ten_view': max_ten_view[i],
                            'ten_created': max_ten_created[i],
                        }
                        print(video_dict)
                        video_list.append(video_dict)
                        # print(video_list[i])

                finally:
                    return video_list


# for i in range(len(front)):
#    video_list_search(front[i])


