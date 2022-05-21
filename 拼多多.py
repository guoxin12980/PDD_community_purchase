import requests
import json
from bs4 import BeautifulSoup
import pyperclip
import re
import time
import pyautogui
import time
import requests
import json

url_new = 'https://mobile.yangkeduo.com/audio_record.html?goods_id=359973723970'
def robot():
    resp2= requests.get(url=url_new,headers=myheaders_get)
    resp2.encoding='utf-8'
    resp2
    info_bs4=BeautifulSoup(resp2.text,"html.parser")
    info_test=info_bs4.body
    test01=info_test.find(id="main")
    info_temp = test01.findAll(name="div", attrs={"class" :"_2aTrQCkV"})
    anlin_info=[]
    report=""
    report1="当前时间:"+str(time.asctime())+"\n此信息为安临小区当前拼多多外卖情况,已经过滤份数较少外卖\n"
    report+=report1
    #print(report1)
    for i in info_temp:
        try:
            name = i.get_text()
            #print(name)
            id_goods=i.find(name="div", attrs={"class" :"_1Vaf42cR"}).get('id')

            result= re.findall('\d+',id_goods)
            anlin_info.append(name+'\n链接------https://mobile.yangkeduo.com/audio_record.html?goods_id='+result[0])
            result_sucesess = re.findall('已成团',name)
            #print(result_sucesess)
            if result_sucesess !=[]:
                test_wechat=re.findall('】.*',name)[0][1:]+'❕链接------https://mobile.yangkeduo.com/audio_record.html?goods_id='+result[0]
                report=report+test_wechat+'\n'
                #print(test_wechat)
            result_num = re.findall('已拼.*件',name)
            Percentage =eval(result_num[0][2:-1])
            if Percentage>=0.13:
                test_wechat=re.findall('】.*',name)[0][1:]+'链接------https://mobile.yangkeduo.com/audio_record.html?goods_id='+result[0]
                #print(test_wechat)
                report=report+test_wechat+'\n'
        except Exception as e:
            pass
    report2="机器人🤖️无盈利义务播报，小区🈚️封控楼，快递到后各拿各的，切记做好消杀工作，机器人不承担责任，只为帮助有需要的邻居！机器人不承担责任谢谢🙏"
    report+=report2
    #print(report2)
    print(report)

    for num in range(1,6):
        #time.sleep(1)
        #print(num)
        #print('anlin%d.png'%num)
        location=pyautogui.locateCenterOnScreen('anlin%d.png'%num,confidence=0.9,grayscale=True)

        pyautogui.moveTo(location[0]/2,location[1]/2)
        pyautogui.click()
        #\n换行符
        pyperclip.copy(report)
        #pyperclip.paste()
        pyautogui.hotkey('command','v')
        #pyautogui.keyDown('command')
        #pyautogui.keyDown('v')
        pyautogui.press('enter')
        time.sleep(2.5)


myheaders_get = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "cookie":'你的cookie',
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "Android",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Mobile Safari/537.36"
    }
