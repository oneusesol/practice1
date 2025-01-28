import requests
from bs4 import BeautifulSoup

# 네이버 뉴스의 URL
url = 'https://search.naver.com/search.naver?&where=news&query=피싱+스미싱'

# HTTP 요청 보내기
response = requests.get(url)

# 파일 열기 (쓰기 모드)
with open('output.txt', 'w', encoding='utf-8') as f:
    # 요청이 성공적이면 200번 상태 코드
    if response.status_code == 200:
        # BeautifulSoup로 HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 뉴스 리스트에서 각 뉴스 항목 추출
        articles = soup.find_all('a', {'class': 'news_tit'})

        # 각 뉴스의 제목과 링크 출력
        for article in articles:
            title = article.get_text()  # 뉴스 제목
            link = article['href']  # 뉴스 링크
            
            # 파일에 제목과 링크를 저장
            f.write(f"제목: {title}\n")
            f.write(f"링크: {link}\n")
            f.write('-' * 80 + '\n')
    else:
        f.write("페이지 요청에 실패했습니다.\n")