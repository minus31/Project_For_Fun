# Project_For_Fun
데이터를 찾거나, 간단한 분석을 하기만해도 설레는 마음을 지키기위한 프로젝트 Repo


## 1. Article to Gender 

> **기간** : 7/31 ~ 8/3 (2018)
### 분석 흐름

- **데이터 수집**
- **Preprocessing**
- **Modeling**
- **Conclusion**


#### 데이터 수집 
  - 출처 : 다음 뉴스 연령 별 선호 뉴스 란의, 성별 정보 이용 
  <img src="https://www.dropbox.com/s/kji6gfuczzsjolc/Screenshot%202018-08-01%2000.58.23.png?raw=1">
  
  - 파일 : Article_Crawler.ipynb
  
  
#### Preprocessing 

 - Tokenizer : konlpy.twitte를 Customize 해서 사용했음. (아래 규칙 추가 적용)
   > - 명사(Noun)으로 분류된 토큰들이 띄어쓰기 없이 문서 내에서 3회 이상 사용되었다면 합성명사로 간주
   > - 띄어쓰기 없이 사용되는 명사의 개수는 2~3개의 범위로 설정
   > - 합성명사에 조사가 들어가는 것을 최대한 방지하기 위해 마지막 토큰이 조사에 포함되지 않는 것만 추출
   
 - Tf-idf Counter vectorizer 사용 
 
 
#### Modeling 

  - 모델 : scikit learn의 Multinomial Naive Bayes 모델 사용 
  
  - 성능 : 0.73(Accuracy)
  
#### Conclusion 

> 성능은 만족 스럽지 못했지만, 1년동안 각 성별의 사람들이 어떤 키워드의 뉴스에 더 관심을 가졌는지 알 수 있었다. 

**여성들이 선호한 뉴스의 키워드**
<img src="https://www.dropbox.com/s/xxysf0mso2mayc8/Screenshot%202018-08-01%2022.04.02.png?raw=1">
 
**남성들이 선호한 뉴스의 키워드**
<img src="https://www.dropbox.com/s/54aqdyddpq2glpm/Screenshot%202018-08-01%2022.04.21.png?raw=1">
 
 
