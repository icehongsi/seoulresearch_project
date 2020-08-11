import requests
import pandas as pd
import time

class Exceptions(Exception):
    def __str__(self):
        return "Exceptions occurred"

class getAddress:
    def __init__(self, forExcelFile = True):#&category=050101
        self.url = "http://api.vworld.kr/req/search?service=search&request=search&\
                                        &size=5&page=1&query={}&type=place&format=json&errorformat=json&crs=EPSG:5179\
                                                    &key=8FEEBFAF-A069-393A-B997-411AA9884913"
        if forExcelFile:
            file_dir = "C:/Users/Youngju Hong/Documents/projectfile/"
            self.new_subway_info = pd.read_csv(f"{file_dir}서울특별시 노선별 지하철역 정보(신규).csv",  encoding = 'cp949')
            del self.new_subway_info["전철명명(영문)"]
            self.new_subway_info["호선"] = self.new_subway_info["호선"].apply(self.eliminate_zero)
            self.new_subway_info["호선 + 역명"] = self.new_subway_info["호선"].astype(str) + " " + self.new_subway_info["전철역명"] + "역" #n호선 XX역 형태
            self.new_subway_info["전철역"] = self.new_subway_info["전철역명"].astype(str) + "역" #XX역 형태
            self.__call__()
        else:
            self.addressretrieveinterface()

    def __call__(self):
        address_list = pd.DataFrame(columns = ["호선", "지하철 역명", "검색 키워드", "주소", "위도", "경도"])

        for i in self.new_subway_info.index:
            element = self.retrieve_request(i) #검색 작업
            if element is None:
                print("{}: Data Not Found".format(self.new_subway_info.loc[i, "전철역명"]))
                address_list.loc[i] = [self.new_subway_info.loc[i, "호선"], self.new_subway_info.loc[i, "전철역명"], None, None, None, None]
            else:
                print(self.new_subway_info.loc[i, "호선"], self.new_subway_info.loc[i, "전철역명"], element["title"], element["address"]["parcel"])
                address_list.loc[i] = [self.new_subway_info.loc[i, "호선"], self.new_subway_info.loc[i, "전철역명"],\
                                       element["title"], element["address"]["parcel"], element["point"]["y"], element["point"]["x"]]

        address_list.to_excel("subway_address.xlsx")

    def retrieve_request(self, index):
        #first trial
        returned = requests.get(self.url.format(self.new_subway_info.loc[index, "전철역"])).json()["response"]
        if returned["status"] in ("NOT_FOUND", "ERROR"):
            returned = requests.get(self.url.format(self.new_subway_info.loc[index, "전철역명"])).json()["response"]
            if returned["status"] in ("NOT_FOUND", "ERROR"):
                return None

        return self.refine_result(self.new_subway_info.loc[index, "전철역"], returned["result"]["items"])
        '''
        input 형태:
        {'id': 'AA0002179410', 'title': '독산역(하안동입구)', 'category': '교통시설 > 철도/지하철 > 지하철', 'address': {'road': '서울특별시 금천구 범안로 1144', 'parcel': '서울특별시 금천구 가산동'}, 'point': {'x': '126.889357472281', 'y': '37.4662003852277'}}
        {'id': 'AA0002140517', 'title': '독산역1번출구', 'category': '교통시설 > 철도/지하철 > 지하철', 'address': {'road': '서울특별시 금천구', 'parcel': '서울특별시 금천구 가산동'}, 'point': {'x': '126.889382864358', 'y': '37.4664365308264'}}
        '''

    def refine_result(self, index, json): #input: returned["result"]["items"]
        for result in json:
            if index in result["title"]: # 조건: XX역 키워드가 검색어 내부에 있음
                if result["address"]["parcel"].split(' ')[0] in ("서울특별시", "인천광역시", "경기도"):
                    return result

        return None



    def addressretrieveinterface(self):
        searched_address = pd.DataFrame(columns = ["검색 키워드", "주소", "위도", "경도"])
        count = 0
        while True:
            print("Input an Address for search: type nothing for quit.")
            temp_address = input()
            if temp_address == "":
                break
            result = requests.get(self.url.format(temp_address)).json()["response"]
            if result["status"] in ("NOT_FOUND", "ERROR"):
                print("Result not found")
            else:
                print("Results: Choose your option.")
                for i in result["result"]["items"]:
                    print(f"검색어: {i['title']}, 주소: {i['address']['parcel']}, 좌표: {i['point']['x'], i['point']['y']}")
                    answer =  input("Take or Leave - 1/0")
                    if answer == "1":
                        searched_address[count] = [i['title'], i['address']['parcel'], i['point']['x'], i['point']['y']]
                        count += 1
                        break

                    print("-" * 50)

        searched_address.to_excel("searched_address.xlsx")

    def eliminate_parentheses(self, name):
        if name.find("(") != -1:
            name = name[:name.find("(")]
        return name

    def eliminate_zero(self, name):
        if name[0] == "0":
            name = name[1:]
        return name

    def iserror(self, request):
        if request.json()["status"] in ("NOT_FOUND", "ERROR"):
            return False
        else:
            return True


get = getAddress(0)