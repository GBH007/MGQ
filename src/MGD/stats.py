# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#
"""
модуль с классами характеристик мп хп и тд
"""

_DEFAULT_MIN_STAT=0
_DEFAULT_CUR_STAT=50
_DEFAULT_MAX_STAT=100
_DEFAULT_NAME_STAT='stat'
_DEFAULT_MIN_LV=0
_DEFAULT_MAX_LV=30
_DEFAULT_CUR_LV=0
_DEFAULT_CUR_XP=0
_DEFAULT_MIN_XP=0
_MAIN_CHARTER_STAT=['endurance','intelligence','mastery','reflexes']

def _xp_for_next_lv(lv):return 25*lv+75
def _lv_for_xp(xp):return (9+0.08*xp)**0.5-3
def _xp_need_for_lv(lv):return 25*lv**2/2+75*lv

_DEFAULT_MAX_XP=_xp_need_for_lv(_DEFAULT_MAX_LV)

class Stat:
	def __init__(self,current=None,maximum=None,minimum=None):
		self.__cur=current
		self.__min=minimum
		self.__max=maximum
	def getDict(self):
		return {
			'current':self.__cur,
			'maximum':self.__max,
			'minimum':self.__min,
		}
	def _stab(self):
		if self.__min!=None:
			self.__cur=max(self.__cur,self.__min)
		elif self.__max!=None:
			self.__cur=min(self.__cur,self.__max)
	def __add__(self,other):
		self.__cur+=other
		self._stab()
		return self
	def __sub__(self,other):
		self.__cur-=other
		self._stab()
		return self
	def setCurrent(self,value):
		self.__cur=value
		self._stab()
	def _setMax(self,value):
		self.__max=value
		self._stab()
	def _setMin(self,value):
		self.__min=value
		self._stab()
	def getCurrent(self):
		return self.__cur
	
class NamedStat(Stat):
	def __init__(self,current=None,maximum=None,minimum=None,name=None):
		Stat.__init__(self,current=current,maximum=maximum,minimum=minimum)
		self.__name=name if name else _DEFAULT_NAME_STAT
	def __str__(self):return '{0}=[{1[minimum]}/{1[current]}/{1[maximum]}]'.format(self.__name,self.getDict())
	
class Lv:
	def __init__(self,current_lv=None,maximum_lv=None,minimum_lv=None,current_xp=None,set_default=False):
		self.__cur_lv=current_lv
		self.__max_lv=maximum_lv
		self.__min_lv=minimum_lv
		self.__cur_xp=current_xp
		if set_default:self._setDefault()
	def _setDefault(self):
		self.__cur_lv=_DEFAULT_CUR_LV
		self.__max_lv=_DEFAULT_MAX_LV
		self.__min_lv=_DEFAULT_MIN_LV
		self.__cur_xp=_DEFAULT_CUR_XP
	def getDict(self):
		return {
			'current_lv':self.__cur_lv,
			'maximum_lv':self.__max_lv,
			'minimum_lv':self.__min_lv,
			'current_xp':self.__cur_xp,
		}
	def _stab(self):
		if self.__cur_xp<_DEFAULT_CUR_XP:self.__cur_xp=_DEFAULT_CUR_XP
		while self.__cur_xp>=_xp_for_next_lv(self.__cur_lv):
			self.__cur_xp-=_xp_for_next_lv(self.__cur_lv)
			self.__cur_lv+=1
		if self.__min_lv!=None:
			self.__cur_lv=max(self.__cur_lv,self.__min_lv)
		if self.__max_lv!=None:
			self.__cur_lv=min(self.__cur_lv,self.__max_lv)
	def __add__(self,other):
		self.__cur_xp+=other
		self._stab()
		return self
	def __sub__(self,other):
		self.__cur_xp-=other
		self._stab()
		return self
	def setCurrentLv(self,value):
		self.__cur_lv=value
		self._stab()
	def setCurrentXp(self,value):
		self.__cur_xp=value
		self._stab()
	def getLv(self):return self.__cur_lv
		
class SolidLv(Stat):
	def __init__(self,current=None,maximum=None,minimum=None):
		Stat.__init__(self,current if current else _DEFAULT_CUR_XP,maximum if maximum else _DEFAULT_MAX_XP,minimum if minimum else _DEFAULT_MIN_XP)
	def getLv(self):
		return _lv_for_xp(self.getCurrent())
		

