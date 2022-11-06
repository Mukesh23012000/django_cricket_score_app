from django.shortcuts import render
from pytz import timezone 
from datetime import datetime,date
import requests
from bs4 import BeautifulSoup

def index(request):
    current_time = time()
    d2 = dates()
    a = cricket()
    return render(request,'index.html',{'time':current_time,'a':a,'date':d2})
def cricket():
    url = "http://static.cricinfo.com/rss/livescores.xml"

    r = requests.get(url)

    while r.status_code != 200:
        r = requests.get(url)
    
    soup = BeautifulSoup(r.text , 'html.parser')

    data = soup.find_all('description')
    a = []
    for i in range (1,100):
        try:
            score = data[i].text
            temp = str(i)
            #a[temp]= score
            a.append(score)
        except:
            break

    return a
def thank(request):
    return render(request,'thank.html')

def time():
    t = datetime.now(timezone("Asia/Kolkata")).strftime("%H:%M")
    a = int(datetime.now(timezone("Asia/Kolkata")).strftime('%H'))
    if a<=12:
        current_time = t+" A.M"
    else:
        b = a-12
        current_time=str(b)+datetime.now(timezone("Asia/Kolkata")).strftime(':%M')+" P.M"
    return current_time
def dates():
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    return d2
def check(request):
    current_time = time()
    d2 = dates()
    a = cricket()
    ch = ["India","Afghanistan","Pakistan","Australia","Sri lanka","Bangladesh","England","West Indies","South Africa","Zimbabwe","New Zealand"]
    b =[]
    for i in a:
        for j in ch:
            if j in i:
                if i in b:
                    pass
                else:
                    b.append(i)
            else:
                pass
    return render(request,'check.html',{'a':b,'time':current_time,'date':d2})
