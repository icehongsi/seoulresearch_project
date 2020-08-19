import requests

url =  "http://www.juso.go.kr/addrlink/addrLinkApi.do?currentPage=1&countPerPage=1&keyword={}&confmKey=devU01TX0FVVEgyMDIwMDgxMTAwMzYxMjExMDA0NTY=&resultType=json"



def doro_to_jibun(address):
    try:
        result = requests.get(url.format(address)).json()
        print(result["results"]["juso"][0]["jibunAddr"])
    except:
        print("No Result")
        pass

while True:
    temp = input()
    doro_to_jibun(temp)