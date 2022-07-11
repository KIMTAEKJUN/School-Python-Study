import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud

pre = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=94775&type=after&onlyActualPointYn=N&onlySpoilerPointYn=N&order=highest&page="
review = []
rate = []

for i in range(1, 4460, 40):
    url = pre + str(i)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    id_list = []
    id_pre = "_filtered_ment_"

    for i in range(10):
        id_list.append(id_pre + str(i))

    for id in id_list:
        review.append(soup.find("span", {"id": id}).get_text().strip())
        rate_list = []
        rate_list = (soup.select("div.star_score > em"))

    for r in rate_list:
        r = int(re.sub('<.+?>', '', str(r)))

        rate.append(r)

df = pd.DataFrame({"review": review, "rate": rate})

# 결측치 확인하기
df.isnull().sum()

# 데이터프레임을 CSV 파일로 저장하기
df.to_csv('review_HW.csv')
df

# CSV 파일에 저장된 데이터 불러오기
df = pd.read_csv("review_HW.csv")
df
