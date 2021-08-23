from urllib.parse import urlparse
import pandas as pd
import numpy as np
import requests
import os

# 다시 수정받기
list = ['google', 'youtube', 'facebook', 'baidu', 'wikipedia', 'yahoo', 'google', 'reddit', 'qq', 'amazon', 'taobao', 'twitter', 'tmall', 'google', 'live', 'vk', 'instagram', 'sohu', 'sina', 'jd', 'weibo', '360', 'google', 'google', 'linkedin', 'google', 'list', 'google', 'google', 'yandex', 'netflix', 'google', 'yahoo', 'google', 't', 'ebay', 'google', 'pornhub', 'imgur', 'bing', 'msn', 'onclkds', 'twitch', 'google', 'google', 'tumblr', 'gmw', 'alipay', 'livejasmin', 'xvideos', 'mail', 'microsoft', 'ok', 'aliexpress', 'wordpress', 'hao123', 'stackoverflow', 'imdb', 'github', 'amazon', 'blogspot', 'pinterest', 'csdn', 'wikia', 'apple', 'google', 'popads', 'youth', 'office', 'bongacams', 'paypal', 'microsoftonline', 'google', 'google', 'whatsapp', 'google', 'xhamster', 'detail', 'diply', 'google', 'adobe', 'coccoc', 'craigslist', 'nicovideo', 'txxx', 'dropbox', 'amazon', 'google', 'amazon', 'googleusercontent', 'google', 'booking', 'thepiratebay', 'google', 'porn555', 'kbstar', 'shinhan', 'wooribank', 'ibk', 'kakaobank']

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
  parse = urlparse(url)
  domain = parse.netloc.split('.')
  try:
    int(domain[-1],0)
    return 1
  except ValueError:
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

def ngram(s, num):  #num : 몇글자씩 끊을 건지
    res=[]
    slen=len(s)-num+1 # slen : 끊었을 때 나오는 개수
    for i in range (slen):
        ss=s[i:i+num] #num만큼 s문자열에서 단어 자르기
        res.append(ss) #자른 단어는 res배열에 저장
    return res

def diff_ngram(sa,sb,num):
    a=ngram(sa,num)	#a문자열을 num단어씩 자른 배열
    b=ngram(sb,num) #b문자열을 num단어씩 자른 배열
    r=[]
    cnt=0
    for i in a:
        for j in b:
            if i==j:    #a에서 자른 단어가 b에도 있다면
                cnt+=1   #cnt++
                r.append(i) #중복되는 단어i를 r배열에 추가한다.
    return cnt/len(b) #cnt/len=(중복되는 횟수/b의 길이), r=중복되는 단어

def brands(url):
  domain = urlparse(url).netloc.lower()
  for names in list:
    return diff_ngram(domain, names, 2)


def preprocessing(url):
    res = []
    res.append(length(url))
    res.append(url_shorten(url))
    res.append(at_sign(url))
    res.append(double_slash(url))
    res.append(dot(url))
    res.append(IP_add(url))
    res.append(dash(url))
    res.append(http(url))
    res.append(brands(url))

    columns = ['length', 'url_shorten', 'at_sign', 'redirection', 'dot', 'IP', 'dash', 'http', 'brands']
    final_res = pd.DataFrame(res, columns= columns)

    return final_res
