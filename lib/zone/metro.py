"""
为了支持深圳地铁租房搜索，目前仅围绕这个条件进行测试
"""

import requests
from lxml import etree
from lib.const.xpath import METRO_LINE_XPATH
from lib.request.headers import *
from lib.spider.base_spider import SPIDER_NAME

# 排除不感兴趣的地铁线
not_interested_metro = ['不限', '3号线(龙岗线)', '4号线(龙华线)']

def get_metro_lines(city):
  url = "https://{0}.zu.{1}.com/ditiezufang/".format(city, SPIDER_NAME)
  headers = create_headers()
  response = requests.get(url, timeout=10, headers=headers)
  html = response.content
  root = etree.HTML(html)
  elements = root.xpath(METRO_LINE_XPATH)

  metros_info = list()
  for element in elements:
    # 去除‘不限’这种情况
    if element.text in not_interested_metro:
      continue

    # name是为了导出显示方便，以及在进行站筛选的时候可以map
    # id用于call api
    metros_info.append({
      'name': element.text[:element.text.index('号线')],
      'path': element.attrib['href'].split('/')[-2]
    })
  
  return metros_info

if __name__ == "__main__":
  metros_info = get_metro_lines("sz")
  print(metros_info)