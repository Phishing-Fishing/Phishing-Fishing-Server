from urllib.parse import urlparse
import urllib.request
import pandas as pd
import numpy as np
import requests
import os
import re

list = ['google','naver','youtube','daum','tistory','kakao','tmall','google','coupang','amazon','netflix','facebook','sohu','namu','qq','wikipedia','taobao','360','jd','microsoft','baidu',
 'yahoo','instagram','dcinside','zoom','adobe','donga','11st','twitch','nate','weibo','gmarket','sina','chosun','jobkorea','office','fmkorea','danawa','apple','saramin',
 'stackoverflow','ebay','aliexpress','bing','afreecatv','dropbox','yna','auction','yahoo','brunch','reddit','myshopify','chase','live','chaturbate','force','zillow','linkedin',
 'microsoftonline','walmart','etsy','indeed','twitter','salesforce','espn','cnn','wellsfargo','intuit','nytimes','craigslist','imdb','msn','capitalone','hulu','paypal',
 'homedepot','yelp','tiktok','amazonaws','spotify','pinterest','kbstar','wooribank','shinhan','ibk','kebhana','nonghyup','kdb','citibank','standardchartered','knbank',
 'busanband','dgb','kjbank','kfcc','suhyup','epostbank','jbbank','jejubank','paybooc','hanacard','hyundaicard','shinhancard','kbcard','wooricard','bccard','hanacard','lottecard',
 'samsungcard','konacard','americanexpress']

def length(url):
  return len(url)

def url_shorten(url):
    req = 'https://unshorten.me/json/'+url
    response = requests.request("GET", req).json()
    if (response['success'] and response['resolved_url'] != url): 
        return 1
    else:                                                        
        return 0

def at_sign(url):
  if '@' in url:
    return 1
  else:
    return 0

def double_slash(url):
  if '//' in url[7:]:
    return 1
  else:
    return 0

def dot(url):
  return url.count('.')

def IP_add(url):
  regex = re.compile('^(.*?)(?:[0-9]{1,3}\.){3}[0-9]{1,3}(.*?)$')
  if regex.search(url) :
    return 1
  else :
    return 0

def dash(url):
  if '-' in url:
    return 1
  else:
    return 0

def http(url):
  if url.startswith('http://'):
    return 1
  else:
    return 0

def ngram(s, num):  #num : ???????????? ?????? ??????
    res=[]
    slen=len(s)-num+1 # slen : ????????? ??? ????????? ??????
    for i in range (slen):
        ss=s[i:i+num] #num?????? s??????????????? ?????? ?????????
        res.append(ss) #?????? ????????? res????????? ??????
    return res

def diff_ngram(sa,sb,num):
    a=ngram(sa,num)	#a???????????? num????????? ?????? ??????
    b=ngram(sb,num) #b???????????? num????????? ?????? ??????
    r=[]
    cnt=0
    for i in a:
        for j in b:
            if i==j:    #a?????? ?????? ????????? b?????? ?????????
                cnt+=1   #cnt++
                r.append(i) #???????????? ??????i??? r????????? ????????????.
    return cnt/len(b) #cnt/len=(???????????? ??????/b??? ??????), r=???????????? ??????

def check_brand(url) :
  percent = 0
  same = 0
  check_url = urlparse(url).netloc.lower()+urlparse(url).path.lower()
  for element in list :
    if element in url :
      return 1
    else :
      for pos in range(len(check_url)) :
        same = 0
        for i, c in enumerate(element) :
          if pos+i < len(check_url) :
            if url[pos+i] == c :
              same = same + 1
            else :
              continue
            temp = same/len(element)
            if percent < temp :
              percent = temp
      continue
  return percent

def brands(url):
  domain = urlparse(url).netloc.lower()
  for names in list:
    return diff_ngram(domain, names, 2)


def preprocessing(url):
    res = []
    
    res.append(url_shorten(url))
    res.append(length(url))
    res.append(at_sign(url))
    res.append(double_slash(url))
    res.append(http(url))
    res.append(dash(url))
    res.append(dot(url))
    res.append(IP_add(url))
    res.append(check_brand(url))

    columns = ['unshorten', 'length', 'at', 'double_slash', 'http', 'hyphen', 'dot', 'ip_form', 'brand']
    final_res = pd.DataFrame([res], columns= columns)

    return final_res
