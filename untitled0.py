# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 10:41:12 2020

@author: kylel
"""
import requests
from bs4 import BeautifulSoup
payload = {"startStation": "2f940836-cedc-41ef-8e28-c2336ac8fe68",
           "endStation": "fbd828d8-b1da-4b06-a3bd-680cdca4d2cd",
           "theDay": "2020/04/18",
           "timeSelect": "11:00",
           "waySelect": "DepartureInMandarin"}
res = requests.post("https://m.thsrc.com.tw/tw/TimeTable/SearchResultList",data = payload)

soup = BeautifulSoup(res.text,"html.parser")
for  i in range(1,11):
    trainNumber = soup.find_all('div',class_="ui-block-a")[i]
    trainTime = soup.find_all('div',class_="ui-block-b")[i]
    nonReservedNumber = soup.find_all('div',class_="ui-block-c")[i]
    print("車次:"+trainNumber.text)
    print("出發-抵達(行車時間):"+trainTime.text)
    print("自由座車廂數:"+nonReservedNumber.text)
    print("=========================================")
    