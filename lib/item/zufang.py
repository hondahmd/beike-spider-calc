#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 二手房信息的数据结构


class ZuFang(object):
    def __init__(self, district, area, xiaoqu, layout, size, price, brand):
        self.district = district
        self.area = area
        self.xiaoqu = xiaoqu
        self.layout = layout
        self.size = size
        self.price = price
        self.brand = brand

    def text(self):
        info = self.district + "," + \
                self.area + "," + \
                self.xiaoqu + "," + \
                self.layout + "," + \
                self.size + "," + \
                self.price + "," + \
                self.brand
        return info

    def get_price(self):
      try:
        return int(self.price)
      except Exception as e:
        return 0
    
    def get_size(self):
      try:
        return float(self.size[:self.size.find('平米')])
      except Exception as e:
        return 0

    def get_layout(self):
      return self.layout
