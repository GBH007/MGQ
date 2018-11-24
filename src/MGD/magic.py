# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

from .item import Item

_DEFAULT_MAGIC_ELEMENTS=['physical','fire','water','earth','wind','lightning','acient','divine']
_DEFAULT_MAGIC_TYPES=['arrow','shield']
_DEFAULT_INDEX_OF_MAGIC_ELEMENT={j:i for i,j in enumerate(_DEFAULT_MAGIC_ELEMENTS)}
_DEFAULT_MAGIC_TABLE=(
	(	1.0,	1.2,	1.1,	0.9,	1.1,	1.2,	0.5,	0.1),
	(	2.0,	1.0,	0.8,	0.7,	1.5,	1.0,	0.5,	0.1),
	(	1.5,	0.8,	1.0,	1.1,	1.0,	1.0,	0.5,	0.1),
	(	1.1,	1.5,	1.0,	1.0,	1.1,	1.5,	0.5,	0.1),
	(	1.2,	1.2,	1.0,	0.9,	1.0,	1.5,	0.5,	0.1),
	(	1.5,	1.2,	2.0,	0.8,	1.1,	1.0,	0.5,	0.1),
	(	3.0,	4.0,	3.7,	3.5,	4.0,	4.0,	1.0,	0.2),
	(	8.0,	8.0,	8.0,	8.0,	8.0,	8.0,	5.0,	1.0),
)
_DEFAULT_MAGIC_ELEMENT=_DEFAULT_MAGIC_ELEMENTS[0]
_DEFAULT_MAGIC_TYPE=_DEFAULT_MAGIC_TYPES[0]

def _calculate_defense_magic_table_line(magic_table_line):
	return [1/i for i in magic_table_line]

class MagicSpell(Item):
	def __init__(self,magic_element=None,magic_table_line=None,magic_type=None,default_damage=0,default_mana_cost=0,name=None):
		Item.__init__(self,name,'magic')
		self.__magic_element=magic_element if magic_element else _DEFAULT_MAGIC_ELEMENT
		self.__magic_table_line=magic_table_line if magic_table_line else _DEFAULT_MAGIC_TABLE[_DEFAULT_INDEX_OF_MAGIC_ELEMENT[self.__magic_element]]
		self.__magic_type=magic_type if magic_type else _DEFAULT_MAGIC_TYPE
		self.__default_damage=default_damage
		self.__default_mana_cost=default_mana_cost
	def getAttackData(self,defense_element):
		return {
			'ratio':self.__magic_table_line[_DEFAULT_INDEX_OF_MAGIC_ELEMENT[defense_element]],
			'damage':self.__default_damage,
			'mana_cost':self.__default_mana_cost,
			'type':self.__magic_type,
		}
	def getDefenseData(self,attack_element):
		return {
			'ratio':1/self.__magic_table_line[_DEFAULT_INDEX_OF_MAGIC_ELEMENT[attack_element]],
			'damage':self.__default_damage,
			'mana_cost':self.__default_mana_cost,
			'type':self.__magic_type,
		}
	def getElement(self):
		return self.__magic_element


