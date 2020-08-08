from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
line_list = []
with open("list_9.txt", encoding = "UTF-8") as file:
    for i in file.readlines():
        i = i.replace("\n", "")
        i = i.replace("\u3000", "")
        if i.find("(") > -1:
            i = i[:i.find("(")]
        if i != "":
            line_list.append(i)

print(line_list)


driver.get('https://map.kakao.com/')
text_input = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/fieldset/div[1]/input")
address = []

for i in line_list:
    text_input.send_keys(f"9호선{i}")
    text_input.send_keys(Keys.RETURN)
    time.sleep(5)
    try:
        print(driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div[7]/div[5]/ul/li[1]/div[5]/div[2]/p[1]").text)
        address.append(driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div[7]/div[5]/ul/li[1]/div[5]/div[2]/p[1]").text)
    except:
        address.append("")
    time.sleep(0.5)
    text_input.clear()
#/html/body/div[5]/div[2]/div[1]/div[7]/div[4]/ul/li[1]/div[5]/div[2]/p[1]

for i in range(len(address)):
    print(f"{line_list[i]}: {address[i]}")