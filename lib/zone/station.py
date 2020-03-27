# 根据地铁线路筛选出地铁站

import requests
from lxml import etree

from lib.zone.metro import get_metro_lines
from lib.const.xpath import METRO_STATION_XPATH
from lib.request.headers import *
from lib.spider.base_spider import SPIDER_NAME

# 设置不感兴趣的区域边际，必须是有且仅有两个站名的list
# 这两个站区间之外的站都不会被抓取，但是这两个站会被包含
not_interested_edges = {
  '1': ['会展中心', '大新'],
  '2': ['香梅北', '赤湾'],
  '5': ['赤湾', '灵芝'],
  '7': ['龙井', '福民'],
  '9': ['前湾', '上梅林'],
  '11': ['宝安', '福田']
}

def delete_not_interested_stations(links, name):
  if name not in not_interested_edges:
    return links
  
  edges = not_interested_edges[name]
  if len(edges) != 2:
    return links
  
  station_names = list()
  for link in links:
    station_names.append(link.text)
  
  edge1 = station_names.index(edges[0])
  edge2 = station_names.index(edges[1])

  if edge1 > edge2:
    return links[edge2:edge1 + 1]
  else:
    return links[edge1:edge2 + 1]

# 拼接需要的页面url
# 在这里手动设置了‘整租’和‘一居’
def get_metro_line_url(city, metro_line):
  return 'https://{0}.zu.{1}.com/ditiezufang/{2}/"'.format(city, SPIDER_NAME, metro_line)

def get_metro_stations(city, metro_line_info):
  page = get_metro_line_url(city, metro_line_info['path'])

  stations = list()
  try:
    headers = create_headers()
    response = requests.get(page, timeout=10, headers=headers)
    html = response.content
    root = etree.HTML(html)
    links = root.xpath(METRO_STATION_XPATH)
    
    links = delete_not_interested_stations(links, metro_line_info['name'])

    for link in links:
      rela_link = link.attrib['href']
      rela_link = rela_link[:-1]
      rela_link = rela_link.split("/")[-1]
      
      stations.append({
        'path': rela_link,
        'name': link.text
      })
    
    return stations
  except Exception as e:
    print(e)

if __name__ == '__main__':
  get_metro_stations('sz', { 'path': 'li2413200637833233', 'name': '11' })
