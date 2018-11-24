# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

import os
import pickle

_DEFAULT_DATA_FOLGER='../data/'

def _data_loader(file_name):
	try:
		f=open(file_name,'rb')
		return pickle.load(f)
	except FileNotFoundError:
		return None
def _data_uploader(file_name,data):
		f=open(file_name,'wb')
		pickle.dump(data,f)
		f.close()

class DataSaver:
	def __init__(self,data_folger=None):
		self.__data_folger=data_folger if data_folger else _DEFAULT_DATA_FOLGER
	def loadEntitys(self):
		return _data_loader(os.path.join(self.__data_folger,'entity.dat'))
	def uploadEntitys(self,data):
		_data_uploader(os.path.join(self.__data_folger,'entity.dat'),data)
	def loadInventory(self):
		return _data_loader(os.path.join(self.__data_folger,'inventory.dat'))
	def uploadInventory(self,data):
		_data_uploader(os.path.join(self.__data_folger,'inventory.dat'),data)
