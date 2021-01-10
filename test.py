from dateutil.parser import parse as date_parse
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.headless = True
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
browser.get("https://www.nowon.kr/corona19/index.do")
time.sleep(3)
content= browser.find_element_by_css_selector(f"#covid_tab_cont > div > div.accordion-list.c-accordion-list").get_attribute('textContent')

req = browser.page_source
r = req

soup = BeautifulSoup(r, "html.parser")
titles = soup.findAll("div", {"class":"accordion-title"})
contents=soup.findAll("div",{"class":"accordion-content"})
arr=[]
for i in range(10):
    arr.append(titles[i].text.strip().split('\n'))



patients = {}
for i in range(10):
    patients[i+1]={}
    for j in range(3):
        if(j==0):
            patients[i+1]["ID"]=arr[i][j]
        if(j==1):
            patients[i+1]["Region"]=arr[i][j]
        if(j==2):
            patients[i+1]["Confirmed Date"]=arr[i][j]
    patients[i+1]["Gender"]=" "
    patients[i+1]["Age"]=" "
    patients[i+1]["Current Status"]=" "
    patients[i+1]["Paths"]=contents[i].text.strip()

print(patients)
# patient_num = 1
# for num, row in enumerate(patients_rows):
#     # print(patient_num)
#     if num % 2 == 0:
#         patients[patient_num] = {}
#         patients[patient_num]["Paths"] = [path.text for path in row.select('.corona-move li')]
#     else:
#         informations = [info.text for info in row.select('td')]
#         # print(informations)
#         patients[patient_num]["ID"] = informations[0]

#         patient_details = informations[1].split("/")
#         patients[patient_num]["Gender"] = patient_details[0]
#         patients[patient_num]["Age"] = patient_details[1]
#         patients[patient_num]["Region"] = patient_details[2]

#         patients[patient_num]["Confirmed Date"] = informations[3]
#         patients[patient_num]["Current Status"] = informations[4]

#         patient_num += 1
"""
patients = {
    1: {
        “ID”: 환자 식별자,
        “Gender”: 환자 성별,
        “Age”: 환자 나이,
        “Region”: 환자 지역,
        “Confirmed Date”:  확진 날짜,
        “Current Status”: 현재 상태(격리 장소, 퇴원 여부 등 기타 정보),
        “Paths”: raw 환자 동선 정보,
    },
    2: {
        “ID”: 환자 식별자,
        “Gender”: 환자 성별,
        “Age”: 환자 나이,
        “Region”: 환자 지역,
        “Confirmed Date”:  확진 날짜,
        “Current Status”: 현재 상태(격리 장소, 퇴원 여부 등 기타 정보),
        “Paths”: raw 환자 동선 정보,
    },
    …
}
'''
"""
