import requests

'''
addlist = input()

while True:
    print("Input an address: ")
    result = requests.get(f"http://www.juso.go.kr/addrlink/addrLinkApi.do?currentPage=1&countPerPage=1&keyword={input()}'&confmKey=devU01TX0FVVEgyMDIwMDgxMTAwMzYxMjExMDA0NTY=&resultType=json").json()
    print(result["results"]["juso"][0]["jibunAddr"])#["results"]["juso"][whd'jibunAddr'])
'''



while True:
    print("Input an address: ")
    result = requests.get(f"http://www.juso.go.kr/addrlink/addrLinkApi.do?currentPage=1&countPerPage=1&keyword={input()}'&confmKey=devU01TX0FVVEgyMDIwMDgxMTAwMzYxMjExMDA0NTY=&resultType=json").json()
    print(result["results"]["juso"][0]["jibunAddr"])#["results"]["juso"][whd'jibunAddr'])