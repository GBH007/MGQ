# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

import glob
import os
import tkinter

_DEFAULT_TEXTURES_FOLGER='../textures/'

class Textures:
	def __init__(self,textures_folger=None):
		self.__texture_folger=textures_folger if textures_folger else _DEFAULT_TEXTURES_FOLGER
		self.__textures={}
	def reload(self,textures_folger):
		self.__texture_folger=textures_folger if textures_folger else _DEFAULT_TEXTURES_FOLGER
		self.load()
	def load(self):
		self.__textures={os.path.split(i)[1].split('.')[0]:tkinter.PhotoImage(file=i) for i in glob.glob(os.path.join(self.__texture_folger,'*.gif'))}
	def __getitem__(self,key):
		return self.__textures[key]
	def getTextureList(self):
		return self.__textures.keys()
