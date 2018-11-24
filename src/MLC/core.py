# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

from .datasaver import DataSaver
from MGD.item import Inventory

class Core:
	def __init__(self,data_folger=None):
		datasaver=DataSaver(data_folger)
		self.__entitys=datasaver.loadEntitys()
		if not self.__entitys:
			self.__entitys=[]
		self.__inventory=datasaver.loadInventory()
		if not self.__inventory:
			self.__inventory=Inventory()
