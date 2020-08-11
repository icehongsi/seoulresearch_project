import requests

url =  "http://www.juso.go.kr/addrlink/addrLinkApi.do?currentPage=1&countPerPage=10&keyword=서울특별시 종로구 동숭동 4'&confmKey=devU01TX0FVVEgyMDIwMDgxMTAwMzYxMjExMDA0NTY=&resultType=json"

result = requests.get(url)
print(result.json())
