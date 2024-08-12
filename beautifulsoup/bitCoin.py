from bs4 import BeautifulSoup as bs
import requests
import time
import json

t = time.time() 
t1 = int(t) 
t2 = t1 -100000

# code = requests.get('https://upbit.com/exchange/CRIX.UPBIT.KRW-BTC')
url = f'https://crix-api-tv.upbit.com/v1/crix/tradingview/history?symbol=BTCKRW&resolution=1D&from={t2}&to={t1}&countback=2'
html_text = bs(requests.get(url).text, 'html.parser')
html_text = html_text.text

#"c":[91789000.00000000,90420000.00000000],
val = html_text.split('"c":')[1]
print()
val[19:27]
while 0:
    t = time.time()
    #현재 시간의 타임스탬프를 반환한다
    t1 = int(t)
    #현재 시간을 초 단위로 반환한 값
    t2 = t1 -100000
    #약 27.8시간을 뺀 값으로, 과거 특정 시간을 나타낸다

    # code = requests.get('https://upbit.com/exchange/CRIX.UPBIT.KRW-BTC')
    url = f'https://crix-api-tv.upbit.com/v1/crix/tradingview/history?symbol=BTCKRW&resolution=1D&from={t2}&to={t1}&countback=2'
    html_text = bs(requests.get(url).text, 'html.parser')
    html_text = html_text.text

    #"c":[91789000.00000000,90420000.00000000],
    val = html_text.split('"c":')[1]
    #c라는 키워드를 기준으로 분리한다
    #c는 api 응답에서 종가 closing price를 나타내는 키이다
    print(val[19:27] , end='')
    #해당 텍스트에서 특정 범위의 문자열을 추출하려고 시도한다
    print('', end='\b')
    time.sleep(0.2)
    print('', end='\b')
    time.sleep(0.2)
    print('', end='\b')
    time.sleep(0.2)
    print('', end='\b')
    time.sleep(0.2)
    print('', end='\b')
    time.sleep(0.2)
    print('', end='\b')
    time.sleep(0.2)
    print('', end='\b')
    time.sleep(0.2)
    print('', end='\b')
    time.sleep(0.2)
dic = json.loads(html_text)
#html text를 json 형식의 파이썬 딕셔너리로 변환한다
print(type(dic))
for i in dic.items():
#변환된 딕셔너리의 키-값 쌍을 출력한다
    print(i)
print(int(dic.get('c')[1]))
#종가 closing price에서 두 번째 값을 가져오며 이를 정수로 변환한다
val = html_text.split('"c":')[1]
print(val[19:27])

#--chatGPT의 수정 제안--
#제안 내용: json 형식이므로 html.parser가 필요하지 않다

#제안 이유:
#json은 경량 데이터 교환 형식으로
# 주로 키-값 쌍으로 구성된 구조화된 데이터를 나타내는데 사용한다

#html은 웹 페이지의 구조와 콘텐츠를 정의하는 마크업 언어다
#태그를 사용하여 배치하고 형식화한다

#이처럼 json은 텍스트로 이루어진 명확한 구조를 가진 데이터 형식이므로
#html.parser가 필요하지 않다

#html.parser는 태그와 그 안의 콘텐츠를 분석하도록 설계되어 있어
#단순한 구조의 json 데이터를 처리하기에는 적합하지 않다