import requests
import pandas as pd
import time

class Exceptions(Exception):
    def __str__(self):
        return "Exceptions occurred"

class getAddress:
    def __init__(self):
        file_dir = "C:/Users/Youngju Hong/Documents/projectfile/"
        self.new_subway_info = pd.read_csv(f"{file_dir}서울특별시 노선별 지하철역 정보(신규).csv",  encoding = 'cp949')
        del self.new_subway_info["전철명명(영문)"]
        self.new_subway_info["호선"] = self.new_subway_info["호선"].apply(self.eliminate_zero)
        self.new_subway_info["호선 + 역명"] = self.new_subway_info["호선"].astype(str) + " " + self.new_subway_info["전철역명"] + "역"
        self.new_subway_info["전철역"] = self.new_subway_info["전철역명"].astype(str) + "역"

        self.url = "http://api.vworld.kr/req/search?service=search&request=search&\
                                &size=1&page=1&query={}&type=place&format=json&errorformat=json&\
                                &key=8FEEBFAF-A069-393A-B997-411AA9884913"

        self.__call__()

    def __call__(self):
        address_list = {}
        for i in self.new_subway_info.index:
            element = self.retrieve_request(i)
            if element is None:
                print("{}: Data Not Found".format(self.new_subway_info.loc[i, "호선 + 역명"]))
                address_list[self.new_subway_info.loc[i, "호선 + 역명"]] = "None"
            else:
                print(element)
                address_list["{}({})".format(self.new_subway_info.loc[i, "호선 + 역명"], element["title"])] = element["address"]["parcel"]
                #print(address_list)

        pd.DataFrame.from_dict(address_list, orient = "index").to_excel("Addresses.xlsx")

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

    def retrieve_request(self, index):
        #first trial
        returned = requests.get(self.url.format(self.new_subway_info.loc[index, "전철역"])).json()["response"]
        if returned["status"] in ("NOT_FOUND", "ERROR"):
            returned = requests.get(self.url.format(self.new_subway_info.loc[index, "전철역명"])).json()["response"]
            if returned["status"] in ("NOT_FOUND", "ERROR"):
                return None

        return returned["result"]["items"][0]




getAddress()

#category=050101
#rint(result.json()["response"]["result"]["items"])#["response"]["result"]["items"])#["response"]["result"]["items"][0]["address"]["parcel"])



#result = requests.get("""http://api.vworld.kr/req/search?service=search&request=search&page=1&query={}&type=place&format=json&errorformat=json&key=8FEEBFAF-A069-393A-B997-411AA9884913""".format(new_subway_info.loc[i, "전철역명"]))