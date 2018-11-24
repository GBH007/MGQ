# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

from .item import Inventory
from .stat import Stat,SolidLv

_DEFAULT_ENTITY_ID=-1
_DEFAULT_ENTITY_NAME='unknown'
_DEFAULT_EQUIPED_SLOTS=['main_hand','off_hand','helment','chestplate','leggins','boots']


class Entity:
	def __init__(self,ent_id=None,name=None,item_list=None,equiped_list=None,equiped_active_magic=None,equiped_passive_magic=None,equiped_triggered_magic=None,lv=None):
		self.__id=ent_id if ent_id else _DEFAULT_ENTITY_ID
		self.__name=name if name else _DEFAULT_ENTITY_NAME
		self.__lv=lv if lv else SolidLv()
		#~ self.__item_list=item_list if item_list else []
		self.inventory=Inventory(item_list)
		self.__equiped_slots=equiped_list if equiped_list else {}
		self.__active_magic=equiped_active_magic if equiped_active_magic else []
		self.__passive_magic=equiped_passive_magic if equiped_passive_magic else []
		self.__triggered_magic=equiped_triggered_magic if equiped_triggered_magic else []
	def getEquipedSlots(self):
		return self.__eqiuped_slots
	def getActiveMagic(self):
		return self.__active_magic
	def getPassiveMagic(self):
		return self.__passive_magic
	def getTriggeredMagic(self):
		return self.__triggered_magic
		

