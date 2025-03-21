# 비트코인 자동 매매 프로그램

https://github.com/user-attachments/assets/a29c69f7-0aa3-4963-abd0-0c293f79e554


- 빨강: 이전 15개 이동평균선
- 초록: 이전 50개 이동평균선
- 보라: 최고가
- 하늘: 최저가

## 실행방법

python3가 설치되어야 합니다.

```
git clone https://github.com/doongeon/bitcoin-consoleChart.git
cd bitcoin-consoleChart
python3 -m venv venv
source venv/bin/activate
pip install pandas plotille requests jwt
python3 main.py
```

## 매매 로직

upbit api키를 받으시면 매도, 매수 주문도 가능합니다.

- 매수 로직: 15이동평균선이 50이동평균선을 뚫고 올라올때
- 매도 로직: 15이동평균선이 50이동평균선을 뚫고 내려갈때
