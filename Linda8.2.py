# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 22:33:06 2018

@author: XR
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 22:45:38 2018

@author: XR
"""

import http.client
import hashlib
import json
import urllib
import random
from aip import AipSpeech
import os
import time
import requests
import win32api
import cv2
import wikipedia
import wolframalpha
import googlemaps
from gmplot import gmplot
import math
import numpy as np

'''fuction def list'''

def distance(lang):
    EARTH_RADIUS=6378.137
    gmaps = googlemaps.Client(key='AIzaSyAuGLlmS0-IlfaGm_XusuHJ0s8ROAtmVzc')

    address1=input('address:')
    geocode_result = gmaps.geocode(address1)

    dict1 = geocode_result[0]
    dict1_lat=dict1['geometry']['location']['lat']
    dict1_lng=dict1['geometry']['location']['lng']
    a1=abs(dict1_lat)
    b1=abs(dict1_lng)

    address2=input('address:')
    geocode_result2 = gmaps.geocode(address2)

    dict2 = geocode_result2[0]
    dict2_lat=dict2['geometry']['location']['lat']
    dict2_lng=dict2['geometry']['location']['lng']
    a2=abs(dict2_lat)
    b2=abs(dict2_lng)
    a=abs(a1*math.pi/180-a2*math.pi/180)
    b=abs(b1*math.pi/180-b2*math.pi/180)
    s = 2 * math.asin(math.sqrt(math.pow(np.sin(a/2),2) + np.cos(a1*np.pi/180)*np.cos(a2*np.pi/180)*math.pow(np.sin(b/2),2)))
    s = s * EARTH_RADIUS;
    s=int(s*1000)/1000
    if lang=='1':
        print('两地之间的距离为',s,'公里')
    else:print('the distance between two place is',s,'kilometers')
def google_map(address):
    gmaps = googlemaps.Client(key='AIzaSyAuGLlmS0-IlfaGm_XusuHJ0s8ROAtmVzc')
    geocode_result = gmaps.geocode(address)

    dict1 = geocode_result[0]
    dict1_lat=dict1['geometry']['location']['lat']
    dict1_lng=dict1['geometry']['location']['lng']
    a=dict1_lat
    b=dict1_lng
    gmap = gmplot.GoogleMapPlotter(a,b,18)
    top_attraction_lats, top_attraction_lons = zip(*[
            (a,b)
            ])
    gmap.scatter(top_attraction_lats, top_attraction_lons, '#010101', size=20, marker=False)

    gmap.marker(a, b, 'cornflowerblue')
    gmap.draw("my_map.html")
    os.system('my_map.html')

def search_wiki(question):
  # running the query
  # Search for page... try block 
  searchResults = wikipedia.search(question)
  if not searchResults:
    print("No result from Wikipedia")
    return
 
  try:
      wikiSummary = wikipedia.summary(searchResults)
      ny = wikipedia.page(searchResults)
      
  except wikipedia.exceptions.DisambiguationError as e:
     print(e.options)

  return wikiSummary
  print('for detail,here is the website,press 1 to enter',ny.url)
  n=input('')
  if n=='1':
       win32api.ShellExecute(0, 'open', ny.url, '','',1)


def wolfsearch(q):
    app_id='Q77HTY-A9VGRYRKK6'
    client=wolframalpha.Client(app_id)
    res=client.query(q)
    if res['@success'] == 'false':
        return ('1')
    else:
        try:
            return next(res.results).text
        except:
            return ('1')
def Robot_Speech(voice):
    APP_ID = '14977199'
    API_KEY = 'n42HbS7x2dKIfMTH0rFlgliv'
    SECRET_KEY = 'GW7mQhe9G7Vo5W4kbSqGrFfSswE1jySr'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = client.synthesis(voice, 'zh', 1, {
        'vol': 10, 'spd':4, 'per':'4'
    })
   
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)

def baidu_translate1(content1):
    appid = '20151113000005349'
    secretKey = 'osubCEzlGjzvw8qdQc41'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = content1
    fromLang = 'en' # 
    toLang = 'zh'   # 
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
 
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        jsonResponse = response.read().decode("utf-8")# 获得返回的结果，结果为json格式
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
        dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
        return dst # 打印结果
    except Exception as e:
        return (e)
    finally:
        if httpClient:
            httpClient.close()

def baidu_translate2(content2):
    appid = '20151113000005349'
    secretKey = 'osubCEzlGjzvw8qdQc41'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = content2
    fromLang = 'zh' # 源语言
    toLang = 'en'   # 翻译后的语言
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
 
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        jsonResponse = response.read().decode("utf-8")# 获得返回的结果，结果为json格式
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
        dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
        return dst # 打印结果
    except Exception as e:
        return (e)
    finally:
        if httpClient:
            httpClient.close()
'''face id'''
def imgdata(file1path, file2path):
    import base64
    f = open(r'%s' % file1path, 'rb')
    pic1 = base64.b64encode(f.read())
    f.close()
    f = open(r'%s' % file2path, 'rb')
    pic2 = base64.b64encode(f.read())
    f.close()
    # 将图片信息格式化为可提交信息，这里需要注意str参数设置
    params = json.dumps(
        [{"image": str(pic1, 'utf-8'), "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},
         {"image": str(pic2, 'utf-8'), "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"}]
    )
    return params.encode(encoding='UTF8')
 
 
# 进行对比获得结果
def img(file1path, file2path):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
    params = imgdata(file1path, file2path)
    access_token = '24.bcce4bb6d52999b0edb217f621b5fffa.2592000.1546132611.282335-14989391'
    request_url = request_url + "?access_token=" + access_token
    request1 = urllib.request.Request(url=request_url, data=params)
    request1.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request1)
    content1= response.read()
    
    return content1





    
'''主程序''' 


lang=input('中文，请按1    english,press 2：')
speak_pd=False
a=False
score=0
lang1='1'
if lang=='1':
    id1=input("使用face id 登陆,输入 1. 使用密码登陆则直接输入密码: ")
    
    if id1=='1':
        input("在摄像头弹出后按空格键拍照，了解请按回车")
        cap = cv2.VideoCapture(0)
        while lang1=='1':
    # get a frame1
            ret, frame = cap.read()
    # show a frame
            cv2.imshow("capture", frame)
            if cv2.waitKey(1) & 0xFF == ord(' '):
                cv2.imwrite("1.jpg", frame)
                break
        cap.release()
        cv2.destroyAllWindows()

        print("Linda:Linda 需要一段时间来识别哥哥的脸部信息哦 请稍后......")
        file1path=r'1.jpg'
        file2path =r'face base/1.jpg'
        res = img(file1path, file2path)
        res= eval(res)
    # # 获得分数
        score = res['result']['score']
        print('您的面部比对分数是',score)
    if id1!='1':
        if id1=='m':a=True
        else:print("你是谁？ 我不认识你 我的哥哥在哪里")    
    if score > 80 or a==True: 
        a=True
        print("Linda:你好 很开心见到你！    ")
        speak=input('Linda:是否想听到宝宝的声音呢？yes or no:    ')
        if speak=='yes':speak_pd=True
        else:speak_pd=False
api_url = "http://openapi.tuling123.com/openapi/api/v2"
while a==True and lang=='1':
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
    content1 = input('Marty：')
    
    
    '''功能plus'''
    
    if content1[-1]=='?':
        print('searching…………')
        answer=wolfsearch(content1)
        if answer !='1':
            print(answer)
            continue_search=input('use wiki to search further y/n :')
        if answer == '1' or continue_search=='y':
            searchResults = wikipedia.search(content1)
            if not searchResults:
                print("No result from Wikipedia")
                continue
            else:    
                try:
                    wikiSummary = wikipedia.summary(searchResults[0])
                    wikiSummary=baidu_translate1(wikiSummary)
                    ny = wikipedia.page(searchResults[0])
                except wikipedia.exceptions.DisambiguationError as e:
                    print(e.options)

                print(wikiSummary)
                print('网址',ny.url)
                n=input('想要了解详细信息请输入1，否则按回车键')
                if n=='1':
                    win32api.ShellExecute(0, 'open', ny.url, '','',1)
                    continue
                else:
                    continue
    if content1=='help':
        with open('help1.txt') as  f1:
            f11 = f1.readlines()
        for x in f11:
            print(x)
        continue
    if content1=='搜索':
        s=input('请输入您要搜索的关键词： ')
        print(s.encode('utf8'))
        url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=4&tn=98012088_5_dg&wd='+s+'&oq=%25E5%2593%2588%25E5%2593%2588%25E5%2593%2588%25E6%2598%25AF21&rsv_pq=ea004e100007f052&rsv_t=dbdfY1C5G%2F2K65bQa%2BV%2BqAkOEWLOY9LjXXBR9SvC%2F8kJ8zekOrwOn3XgYEYe%2FhdUasNLmw&rqlang=cn&rsv_enter=1&inputT=527&rsv_sug3=24&rsv_sug2=0&rsv_sug4=563'
        win32api.ShellExecute(0, 'open',url, '','',1)
    if content1=='地图':
        address=input('请输入您要搜索的地址')
        google_map(address)
        continue
    if content1=='计算距离':
        distance()
        continue
    if content1=="记事本":
        win32api.ShellExecute(0, 'open', 'notepad.exe', '','',1)
        continue
    if content1=="网页":
        web=input("请输入您要进入的网址: ")
        web='http://'+web
        win32api.ShellExecute(0, 'open', web, '','',1)
        continue
    if content1=='放一首我喜欢听的歌':
        os.system('music/loveyourself.mp3')
        continue
    if content1=='时间':
        print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        continue
    if content1=="quit()":
        print('Linda:希望下次还能见到你呀 再见')
        break
    data = {
        "perception":
        {
            "inputText":
            {
                "text": content1
            },

        },

        "userInfo":
        {
            "apiKey": "f25e52036d494f7c8f306b0c9812b17e",
            "userId": "357191"
        }
    }
    data = json.dumps(data).encode('utf8')
    response_str = requests.post(api_url, data=data, headers={'content-type': 'application/json'})
    response_dic = response_str.json()
    results_text = response_dic['results'][0]['values']['text']
    print('Linda：' + results_text)
    if speak_pd==True:
        Robot_Speech(results_text)  
        os.system('auido.mp3')
       
'''英文程序'''
a=False
espeak_pd=False
score=0
cd_code2=False
if lang=='2':
    id2=input("use face id,answer 1,use key,just answer the key: ")
    
    if id2=='1':
        input("after the camera jump out, press space to capture your face,press enter to continue")
        cap = cv2.VideoCapture(0)
        while lang1=='1':
    # get a frame1
            ret, frame = cap.read()
    # show a frame
            cv2.imshow("capture", frame)
            if cv2.waitKey(1) & 0xFF == ord(' '):
                cv2.imwrite("1.jpg", frame)
                break
        cap.release()
        cv2.destroyAllWindows()

        print("Linda:Linda need some time to recognize your face......")
        file1path=r'1.jpg'
        file2path =r'face base/1.jpg'
        res = img(file1path, file2path)
        res= eval(res)
    # # 获得分数
        score = res['result']['score']
        print('your face compared score is',score)
    if id2=='m':cd_code2=True
    if score > 80 or cd_code2==True:
        a=True
        print("Linda:My majesty,nice to see you, how are you doing today")
        espeak=input("Linda:Do you want to hear my voice,my majesty? yes or no   ")
        if espeak=='yes':espeak_pd=True    
    else: 
        a=False
        print("who are you? i'm sorry , i only serve to my lord")

    
    
    
while a==True or cd_code2==True:
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
    espeak_pd==False
    content1 = input('marty：')
    continue_search='n'
    if content1[-1]=='?':
        print('searching…………')
        answer=wolfsearch(content1)
        if answer !='1':
            print(answer)
            continue_search=input('use wiki to search further y/n :')
        if answer == '1' or continue_search=='y':
            searchResults = wikipedia.search(content1)
            if not searchResults:
                print("No result from Wikipedia")
                continue
            else:    
                try:
                    wikiSummary = wikipedia.summary(searchResults[0])
                    ny = wikipedia.page(searchResults[0])
                    print(wikiSummary)
                    print('here is the webstie',ny.url)
                    n=input('for detail press 1, otherwise ,press enter')
                except wikipedia.exceptions.DisambiguationError as e:
                    print(e.options)
                if n=='1':
                    win32api.ShellExecute(0, 'open', ny.url, '','',1)
                    continue
                else:
                    continue
    if content1=='search':
        s=input('put the key words： ')
        print(s.encode('utf8'))
        url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=4&tn=98012088_5_dg&wd='+s+'&oq=%25E5%2593%2588%25E5%2593%2588%25E5%2593%2588%25E6%2598%25AF21&rsv_pq=ea004e100007f052&rsv_t=dbdfY1C5G%2F2K65bQa%2BV%2BqAkOEWLOY9LjXXBR9SvC%2F8kJ8zekOrwOn3XgYEYe%2FhdUasNLmw&rqlang=cn&rsv_enter=1&inputT=527&rsv_sug3=24&rsv_sug2=0&rsv_sug4=563'
        win32api.ShellExecute(0, 'open',url, '','',1)
    if content1=='map':
        address=input('the address you want to search')
        google_map(address)
        continue
    if content1=='distance':
        distance()
        continue
    if content1=='help':
        with open('help2.txt') as  f1:
            f11 = f1.readlines()
        for x in f11:
            print(x)
        continue
    if content1=="notepad":
        win32api.ShellExecute(0, 'open', 'notepad.exe', '','',1)
        continue
    if content1=="website":
        web=input("enter your website:   ")
        web='http://'+web
        win32api.ShellExecute(0, 'open', web, '','',1)
        continue
    if content1=="play a song":
        os.system('loveyourself.mp3')
        continue
    if content1=='time':
        print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
    if content1=="quit()":
        print('Linda:have a good day , My majasty!')
        break
    data = {
        "perception":
        {
            "inputText":
            {
                "text": baidu_translate1(content1)
            },
       
        },

        "userInfo":
        {
            "apiKey": "f25e52036d494f7c8f306b0c9812b17e",
            "userId": "357191"
        }
    }
    try:    
        data = json.dumps(data).encode('utf8')
        response_str = requests.post(api_url, data=data, headers={'content-type': 'application/json'})
        response_dic = response_str.json()
        results_text = response_dic['results'][0]['values']['text']
        content2=results_text
        voice=baidu_translate2(content2)
    except:
          print("这个问题宝宝回答不出来哦")
    
    print('Linda：' + voice)
    if espeak_pd==True:
        Robot_Speech(voice)  
        os.system('auido.mp3')
   
print("")
print("goodbye")
input("")
