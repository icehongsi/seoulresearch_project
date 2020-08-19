from pyproj import Proj, Transformer, CRS
from functools import partial
import pandas as pd
import requests


'''
1. transformer = Transformer.from_crs를 활용하여 좌표를 변환해줄 객체 생성
2. transformer(y축 좌표, x축 좌표) >> 반환값은 튜플
3. transformation 함수: epsg_from, epsg_to, x_coordinate, y_coordinate
'''

def transformation(epsg_from, epsg_to, x_coordinate, y_coordinate):
    return Transformer.from_crs(f"epsg:{epsg_from}", f"epsg:{epsg_to}").transform(y_coordinate, x_coordinate)

def address