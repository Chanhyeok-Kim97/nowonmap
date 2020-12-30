import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.headless = True
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
browser.get("https://www.nowon.kr/corona19/index.do")
time.sleep(3)
#covid_tab_cont > div > div.accordion-list.c-accordion-list > div:nth-child(2)
#covid_tab_cont > div > div.accordion-list.c-accordion-list > div:nth-child(4)
#covid_tab_cont > div > div.accordion-list.c-accordion-list > div:nth-child(20) //아코디언 타이틀
for i in range(1,10) :
    titles = browser.find_element_by_css_selector(f"#covid_tab_cont > div > div.accordion-list.c-accordion-list > div:nth-child({(2*i)})").find_elements_by_tag_name('p')#.find_elements_by_tag_name("p")
    content= browser.find_element_by_css_selector(f"#covid_tab_cont > div > div.accordion-list.c-accordion-list > div:nth-child({(2*i+1)}) > div").get_attribute('textContent')
    for i in range(len(titles)-1) :
        if i==0:
            print("No:",titles[i].text)
            continue
        print(titles[i].text)
    print(content.strip())
    print('')

nextPagebtn=browser.find_element_by_css_selector("#page-div > a:nth-child(2)")
nextPagebtn.click()
time.sleep(3)

for i in range(1,10) :
    titles = browser.find_element_by_css_selector(f"#covid_tab_cont > div > div.accordion-list.c-accordion-list > div:nth-child({(2*i)})").find_elements_by_tag_name('p')#.find_elements_by_tag_name("p")
    content= browser.find_element_by_css_selector(f"#covid_tab_cont > div > div.accordion-list.c-accordion-list > div:nth-child({(2*i+1)}) > div").get_attribute('textContent')
    for i in range(len(titles)-1) :
        if i==0:
            print("No:",titles[i].text)
            continue
        print(titles[i].text)
    print(content.strip())
    print('')



'''
titles = browser.find_element_by_css_selector("#covid_tab_cont > div > div.accordion-list.c-accordion-list > div:nth-child(4)").find_elements_by_tag_name('p')#.find_elements_by_tag_name("p")
content= browser.find_element_by_css_selector("#covid_tab_cont > div > div.accordion-list.c-accordion-list > div:nth-child(5) > div").get_attribute('textContent')
for i in range(len(titles)-1) :
    if i==0:
        print("No:",titles[i].text)
        continue
    print(titles[i].text)
print(content.strip())
'''
# 출처: https://engkimbs.tistory.com/896 [새로비]
#covid_tab_cont > div > div.accordion-list.c-accordion-list > div.accordion-title.on
#covid_tab_cont > div > div.accordion-list.c-accordion-list > div:nth-child(4)
#covid_tab_cont > div > div.accordion-list.c-accordion-list > div:nth-child(6)
#covid_tab_cont > div > div.accordion-list.c-accordion-list > div:nth-child(8)
"""
tag_names = browser.find_element_by_css_selector("#covid_tab_cont > div > div.accordion-list.c-accordion-list").find_elements_by_tag_name("p")
for tag in tag_names:
    print(tag.text.split("\n"))
"""
#for tag in titles:
#    print(tag.text)
