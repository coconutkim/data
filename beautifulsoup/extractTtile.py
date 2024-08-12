import re #regex 정규 표현식
from bs4 import BeautifulSoup #텍스트 형태의 데이터에서 원하는 html 태그 추출

html = """
<li><a href="https://news.v.daum.net/v/20181126211257847" class="link_txt">&#39;
판사 블랙리스트&#39; 없다던 법원 곤혹...&#39;고의 부실조사&#39; 의혹</a></li>
<li><a href="https://news.v.daum.net/v/20181126193835503" class="link_txt">中군
용기, 3차례 KADIZ 진입후 이탈...정부, 엄중 항의</a></li>
<li><a href="https://news.v.daum.net/v/20181126201817082" class="link_txt">&#39;수수료 인하&#39; 자영업자 부담 줄고 소비자 & #39;혜택&#39;도 줄어드나</a></li>
<li><a href="https://news.v.daum.net/v/20181126201503029" class="link_txt">KT 화
재 후 첫 평일...복구됐다지만 먹통 피해 여전</a></li>
<li><a href="https://news.v.daum.net/v/20181126203723330" class="link_txt">내일
도 초미세먼지 &#39;나쁨&#39;...낮동안 온화</a></li>
"""

#parse: 주어진 데이터를 해석하고 분석하여 원하는 형식 또는 구조로 변환하는 작업
#뷰티풀수프로 html 파싱
soup = BeautifulSoup(html, 'html.parser')

#모든 <a> 태그에서 텍스트를 추출하겠다
titles = [a.get_text() for a in soup.find_all('a', class_='link_txt')]

#한글만 포함된 제목을 추출하는 정규 표현식
#re.sub 파이썬의 re 모듈에서 제공하는 함수, 문자열에서 특정 패턴을 찾아 다른 문자열로 치환하는데 사용한다
korean_titles = [re.sub(r'[^가-힣\s]', '', title).strip() for title in titles]

#한글이 포함된 제목만 출력한다
korean_titles = [title for title in korean_titles if title]

#한글이 포함된 제목만 출력한다
korean_titles = [title for title in korean_titles if title]

for title in korean_titles:
    print(title)

#뷰티풀수프를 사용해 html에서 텍스트를 추출한다
#정규 표현식을 사용해 한글로 이루어진 부분만 남긴다
#한글 제목만 리스트에 저장해 출력한다