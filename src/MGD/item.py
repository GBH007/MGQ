# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

from .stats import _MAIN_CHARTER_STAT

_DEFAULT_ARMOR_DEFENSE=100
_DEFAULT_WEARPON_ATTACK=100
_ITEM_TYPES=['armor','wearpon','magic','thing']
_ITEM_CLASS=['d','c','b','a','s','ss','sss']
_DEFAULT_ITEM_NAME='unknow'
_DEFAULT_ITEM_TYPE='unknow'
_DEFAULT_ITEM_CLASS=_ITEM_CLASS[0]


class Item:
	def __init__(self,name=None,item_type=None,item_class=None):
		self.__item_type=item_type if item_type else _DEFAULT_ITEM_TYPE
		self.__item_class=item_class if item_class else _DEFAULT_ITEM_CLASS
		self.__name=name if name else _DEFAULT_ITEM_NAME
	def getItemType(self):
		return self.__item_type
	def getItemClass(self):
		return self.__item_class
	def getItemName(self):
		return self.__name
	def __str__(self):
		return 'type={0}\nclass={1}\nname={2}'.format(self.__item_type,self.__item_class,self.__name)

class Equipment(Item):
	def __init__(self,bonus_stat=None,name=None,item_type=None,item_class=None):
		Item.__init__(self,name,item_type,item_class)
		self.__bonus_stat={i:bonus_stat.get(i,0) for i in _MAIN_CHARTER_STAT} if bonus_stat else {i:0 for i in _MAIN_CHARTER_STAT}
	def getBonusStat(self):
		return self.__bonus_stat

class Armor(Equipment):
	def __init__(self,bonus_stat=None,defense=None,name=None,item_class=None):
		Equipment.__init__(self,bonus_stat,name,'armor',item_class)
		self.__defense=defense if defense else _DEFAULT_ARMOR_DEFENSE
		
class Wearpon(Equipment):
	def __init__(self,bonus_stat=None,attack=None,name=None,item_class=None):
		Equipment.__init__(self,bonus_stat,name,'wearpon',item_class)
		self.__attack=attack if attack else _DEFAULT_WEARPON_ATTACK
		
class Inventory:
	def __init__(self,item_list=None):
		self.__item_list=item_list if item_list else []
	def __getitem__(self,key):
		return self.__item_list[key]
	def __setitem__(self,key,value):
		self.__item_list[key]=value
	def __delitem__(self,key):
		del self.__item_list[key]
	def __len__(self):
		return len(self.__item_list)
	def add(self,item):
		self.__item_list.append(item)

