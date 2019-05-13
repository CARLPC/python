# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 09:47:44 2019

@author: Carlpc
"""

import requests
import random
import re
import base64
import json
import os
from bs4 import BeautifulSoup
import win32clipboard as w
import win32con
import time

def decode_wwei(image,hds):
    x=     random.choice(hds)
    try:
        req = requests.get("https://jiema.wwei.cn/",timeout=20,headers=x)
        pattern=re.compile(r'(?<=token=).*?(?=")')
        matchObj = re.findall(pattern,req.text)
        pageurl="https://jiema.wwei.cn/fileupload.html?op=jiema&token="+ matchObj[0]
        files={'id':(None,'WU_FILE_0'),'name':(None,'qq.png'),'type':(None,'image/png'),   \
               'lastModifiedDate':(None,u'Sat Feb 02 2019 09:44:18 GMT+0800 (中国标准时间)'),\
               'size':(None,'436'),'file':('qq.png',image,'image/png')}
        x['Accept']='*/*'
        x['Origin']='https://jiema.wwei.cn'
        x['Referer']='https://jiema.wwei.cn'
        x['Connection']='Keep-alive'
        x['Access-Sign']='*'
        x['Accept-Encoding']='gzip, deflate'
        #print "---"+image
        req =requests.post(pageurl,files=files,headers=x)
        if(len(req.text)>3):        
            print ("---"+req.text)
            response_body= req.text.encode('utf-8')
            response_body= json.loads(response_body )
            if('data' in response_body.keys()):
                print ("Decode succcess")
                return (1,response_body['data'])
            print ("Decode error")
            return (0,'-')
        else:
            print ("Decode error")
            return (0,'-')
        
    except Exception:
        return (0,'-')


def get_png_code(hds):
    try:
        req = requests.get("https://b.freess.biz",timeout=3,headers=random.choice(hds))
        pattern=re.compile(r'(?<=href="data:image/png;base64,).*?(?=")')
        matchObj = re.findall(pattern,req.text)
        if len(matchObj)<2 :
            print ("get ssr error")
            return (0,'-')
        else:
            print ("Get ssr Success")
            return (1,base64.b64decode(matchObj[1]))
    except Exception:
        print ("freess website error")
        return (0,'-')

def get_png_code_today(hds):
    try:
        getheader=random.choice(hds)
        getheader['Upgrade-Insecure-Requests']='1'
        req = requests.get("https://ss.freess.today/",timeout=3,headers=random.choice(hds))
        soup = BeautifulSoup(req.text, "lxml")
        reg = soup.find_all('a',class_="overlay lightbox")
        xx=''
        for item in reg:
            xx=item['href']
            if (xx):
                break
        if(xx):
            url='https://ss.freess.today/'+xx
            newheader=random.choice(hds)
            newheader['Upgrade-Insecure-Requests']='1'
            newheader['If-None-Match']='1da-583545495858d-gzip'
            newheader['If-Modified-Since']= 'Tue, 05 Mar 2019 08:05:03 GMT'
            req = requests.get(url,timeout=20,headers=random.choice(hds))
            if(req.status_code==200):
                print ("get today image success")
                return (1, req.content)
            else:
                print ("get image error")
                return (0,'-')
        else:
            print ("get image error")
            return (0,'-')
    except Exception:
        print ("get image error")
        return (0,'-')
	
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString)
    w.CloseClipboard()

def proxy_ok():
    try:
        my_proxies={"http":"http://127.0.0.1:","https":"https://127.0.0.1:"}
        req = requests.get("http://httpbin.org/ip",timeout=10,proxies=my_proxies)
        if(req.status_code ==200):
            print ("proxy success")
            return 1
        else:
            print ("proxy error")
            return 0
    except Exception:
        print ("proxy error")
        return 0



while(proxy_ok()==0):
    image=''
    hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},\
    {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},\
    {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},\
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'},\
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'},\
    {'User-Agent':'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'},\
    {'User-Agent':'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'}] 

    os.system('taskkill /IM Shadowsocks.exe /F')
    (status_code,image)=get_png_code(hds)
    if(status_code==0):
        (status_code,image)=get_png_code_today(hds)
    if(status_code):
        (status_code,ssrurl)=decode_wwei(image,hds)
        if(status_code):
            ssrurl=str(ssrurl).replace('ss://','')
            print ('ss://'+ssrurl)
            setText('ss://'+ssrurl)
            config=  (bytes.decode(base64.b64decode(ssrurl))).split(':')
            print(config)
            methon=config[0].replace(' ','')
            code=config[1].split('@')[0].replace(' ','')
            server=config[1].split('@')[1].replace(' ','')
            port=config[2].replace(' ','')
            del image ,hds,ssrurl,config
            
            fp=open('D:/software/Shadowsocks-4.0.7/gui-config.json','r')
            load_dict = json.load(fp)
            fp.close()
            server_config=load_dict['configs'][0]
            server_config['method']=methon
            server_config['password']=code
            server_config['server']=server
            server_config['server_port']=port
            fp=open('D:/software/Shadowsocks-4.0.7/gui-config.json','w')
            json.dump(load_dict,fp)
            fp.close()
            print (os.system("start /b D:/software/Shadowsocks-4.0.7/Shadowsocks.exe"))
            time.sleep(15)