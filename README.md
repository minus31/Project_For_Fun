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

--------

# 2. Face To Pictogram 

>  **기간** : 8/6 ~ 8/20 (2018)

### Preface
 Trying style transfering but output image is much much more simple than input image, 


### Dataset
<img style="float: center;" src="https://www.dropbox.com/s/42vhth6e0exn37x/Screenshot%202018-08-18%2010.03.43.png?raw=1" width="900">

> - **image size = 300, 300**
> - **image color = 'gray'**
> - **the number of images = 34**


### Image processing
  - used **opencv**
  - **RGB image** to **Gray scale**
  - made image size to **300 x 300**


### Discriminator & Generator 

##### Discriminator 

- Q1. why discriminator's output is 32x32x1 
> I thought discriminator has a role of discriminating fake or real with 0, 1 each.
> is it technic ? 

>> **This Answer was writen on the paper**
>>
>> - by implementing, reserchers dose Johnson 's Residual architecture which is known as very productive on style transfering problem for generator, and use **PatchGAN**'s discriminator 


>  PatchGAN research 


##### Discriminator 

- In the paper, Generator is **Johnson's model** which have shown imporessive results for neural style transfer and superresolution
> but my target image is quite simple form, So I create the generator with DenseNet architecture for reducing operation and the number of parameters. 



### Model 

####  Loss function

$\begin{eqnarray}
\mathcal{L}_{cyclegan} 
&=& \mathcal{L}_{GAN} + \lambda \mathcal{L}_{cycle} \\ \\
&\rightarrow& \mathcal{L}_{GAN_G} = \mathbf{E}[log D_y(y)] \ + \ \mathbf{E}[log (1 - D_y(G(x)))] \\
&\rightarrow& \mathcal{L}_{GAN_F} = \mathbf{E}[log D_x(x)] \ + \ \mathbf{E}[log (1 - D_x(F(y)))] \\
&\rightarrow& \mathcal{L}_{GAN} =  \mathcal{L}_{GAN_G} \ + \ \mathcal{L}_{GAN_F} \\
&\rightarrow& \mathcal{L}_{cycle} = \mathbf{E}||F(G(x)) - x||_1 \ + \ \mathbf{E}||G(F(y)) - y||_1 
\end{eqnarray}$


##### L1_lambda 

 - My result images are very simple compared to the input. 
 - And, I reduce L1_lambda 10(in paper) to 0.5 

 **Output** (when L1_lambda = 0.5)
   <img src="https://www.dropbox.com/s/uagy0ydrhllmiyt/Screenshot%202018-08-18%2012.20.49.png?raw=1"> 

 


##### Problem 

 - It has trained about 10000 epochs, but it isn't giving proper outputs 

 - As the image above describe, background is still has a value. 
 > - To solve this, first thing to do is `normalizing`. 
 >
 > > - BUT, before that, I have an idea which is making all value to 0 or 255 by threshold(`mean` would work okay.).


 * *The Result of the idea*

 <img src="https://www.dropbox.com/s/iz8fkw1uwgvg60v/Screenshot%202018-08-18%2017.25.56.png?raw=1">

 $\rightarrow$ It seems better, but some images are tranfered unproperly, like below.

 <img src="https://www.dropbox.com/s/zgfdoxf34trksno/Screenshot%202018-08-18%2017.36.23.png?raw=1" width="700">