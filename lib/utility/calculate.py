class CalculateInfo(object):
  def __init__(self):
    self.price_list = list()
    self.size_list = list()
    self.house_number = 0

  def init(self, house_list):
    for house in house_list:
      if (house.get_layout().find('1室') >= 0 or house.get_layout().find('1居室') >= 0):
        self.price_list.append(house.get_price())
        self.size_list.append(house.get_size())
        self.house_number += 1

  def price_per_house(self):
    if (self.house_number == 0):
      return 0

    total_price = 0
    for price in self.price_list:
      total_price += price

    return total_price / self.house_number

  def size_per_house(self):
    if (self.house_number == 0):
      return 0

    total_size = 0
    for size in self.size_list:
      total_size += size

    return total_size / self.house_number
