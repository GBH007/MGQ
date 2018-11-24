# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

import tkinter
from .textures import Textures

_DEFAULT_WINDOW_WIDTH=1280
_DEFAULT_WINDOW_HEIGHT=720
_DEFAULT_TAG='_'
_DEFAULT_ASK_FRAME_WIDTH=100
_DEFAULT_ASK_FRAME_HEIGHT=50
_DEFAULT_INVENTORY_WIDTH=900
_DEFAULT_INVENTORY_HEIGHT=600
_DEFAULT_INVENTORY_SEPARATOR_HEIGHT=200
_DEFAULT_ITEM_SHORT_INFO_WIDTH=100
_DEFAULT_ITEM_SHORT_INFO_HEIGHT=100
_DEFAULT_ENTITY_INFO_WIDTH=500
_DEFAULT_ENTITY_INFO_HEIGHT=170
_TEXTURIES=Textures()

class GUICore(tkinter.Tk):
	def __init__(self,width=_DEFAULT_WINDOW_WIDTH,height=_DEFAULT_WINDOW_HEIGHT,texturies_folger=None):
		tkinter.Tk.__init__(self)
		self.title('MGQ - no work edition - v-1.0.0')
		self.geometry('{0}x{1}'.format(width,height))
		self.__canvas=tkinter.Canvas(self)
		self.__canvas.pack(anchor=tkinter.NW,expand=tkinter.YES,fill=tkinter.BOTH)
		_TEXTURIES.reload(texturies_folger)
	def placeTexture(self,texture_name,dx,dy,tag=_DEFAULT_TAG):
		self.__canvas.create_image(dx,dy,image=_TEXTURIES[texture_name],anchor=tkinter.NW,tags=tag)
		self.__canvas.update()
		#~ self.update()
	def removeByTag(self,tag):
		self.__canvas.delete(tag)
		self.__canvas.update()
		#~ self.update()
	def placeWidget(self,widget,dx,dy,width=None,height=None,tag=_DEFAULT_TAG):
		self.__canvas.create_window(dx,dy,window=widget,anchor=tkinter.NW,width=width,height=height)
		self.__canvas.update()
		
class AskFrame(tkinter.Frame):
	def __init__(self,text,ok_func,no_func):
		tkinter.Frame.__init__(self,width=_DEFAULT_ASK_FRAME_WIDTH,height=_DEFAULT_ASK_FRAME_HEIGHT)
		tkinter.Label(self,text=text).pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=tkinter.YES)
		tkinter.Button(self,text='ok',command=ok_func).pack(side=tkinter.LEFT,fill=tkinter.X,expand=tkinter.YES)
		tkinter.Button(self,text='no',command=no_func).pack(side=tkinter.RIGHT,fill=tkinter.X,expand=tkinter.YES)

class ItemShortInfoFrame(tkinter.Frame):
	def __init__(self,item):
		tkinter.Frame.__init__(self,width=_DEFAULT_ITEM_SHORT_INFO_WIDTH,height=_DEFAULT_ITEM_SHORT_INFO_HEIGHT)
		tkinter.Label(self,image=_TEXTURIES['no_txr']).pack(side=tkinter.LEFT)
		tkinter.Label(self,text=str(item)).pack(side=tkinter.RIGHT)
		
class EntityInfoFrame(tkinter.Frame):
	def __init__(self,entity):
		tkinter.Frame.__init__(self,width=_DEFAULT_ENTITY_INFO_WIDTH,height=_DEFAULT_ENTITY_INFO_HEIGHT)
		self.__entity=entity
		self.__canvas=tkinter.Canvas(self,width=_DEFAULT_ENTITY_INFO_WIDTH,height=_DEFAULT_ENTITY_INFO_HEIGHT)
		self.__canvas.pack(fill=tkinter.BOTH,expand=tkinter.YES,anchor=tkinter.NW)
		self.slotsLoad()
	def slotsLoad(self):
		for i,s in enumerate(['am','pm','tm']):
			self.__canvas.create_text(10,i*55+25,anchor=tkinter.NW,text=s)
			for j in range(4):
				self.__canvas.create_image(50+j*55,i*55,anchor=tkinter.NW,image=_TEXTURIES['unactive_slot'],tags=s)
		self.__canvas.create_text(350,10,anchor=tkinter.NW,text='slots')
		for i in range(2):
			for j in range(3):
				self.__canvas.create_image(300+j*55,25+i*55,anchor=tkinter.NW,image=_TEXTURIES['unactive_slot'],tags='equiped_slots')

class InventoryFrame(tkinter.Frame):
	def __init__(self,inventory):
		tkinter.Frame.__init__(self)
		self.__inventory=inventory
		self.__canvas=tkinter.Canvas(self,width=_DEFAULT_INVENTORY_WIDTH,height=_DEFAULT_INVENTORY_HEIGHT,bg='grey')
		self.__canvas.pack(anchor=tkinter.NW,expand=tkinter.YES,fill=tkinter.BOTH)
		self.__canvas.create_window(0,_DEFAULT_INVENTORY_SEPARATOR_HEIGHT,window=tkinter.Button(image=_TEXTURIES['left_arrow'],command=self.prev),anchor=tkinter.NW,tags='prev')
		self.__canvas.create_window(_DEFAULT_INVENTORY_WIDTH,_DEFAULT_INVENTORY_SEPARATOR_HEIGHT,window=tkinter.Button(image=_TEXTURIES['right_arrow'],command=self.prev),anchor=tkinter.NE,tags='next')
		self.__canvas.create_window(_DEFAULT_INVENTORY_WIDTH/2,_DEFAULT_INVENTORY_SEPARATOR_HEIGHT,window=tkinter.Label(text='inventory {0}/inf'.format(len(self.__inventory))),anchor=tkinter.N,tags='inventory_info')
		
		
		self.__last_slot=None
		
		self.inventoryLoad()
		
		
	def next(self):pass
	def prev(self):pass
	def inventoryLoad(self):
		for i in range(6):
			for j in range(15):
				try:
					tx=self.__inventory[i*15+j].getItemClass()
				except IndexError:
					tx='unactive'
				self.__canvas.create_image(j*60+5,i*60+_DEFAULT_INVENTORY_SEPARATOR_HEIGHT+45,image=_TEXTURIES[tx+'_slot'],anchor=tkinter.NW,tags=(str(i*15+j),'inventory_slot'))
		self.__gIILoop()
	def __gIILoop(self):		#ОЧЕЕЕЕНь жесткий костыль
		self.getItemInfo()
		self.after(500,self.__gIILoop)
	def getItemInfo(self):
		try:
			slot=int(self.__canvas.gettags(self.__canvas.find_withtag(tkinter.CURRENT))[0])
			if self.__last_slot!=slot:
				self.__last_slot=slot
				try:
					item=self.__inventory[slot]
					self.__canvas.delete('item_short_info')
					self.__canvas.create_window(0,0,window=ItemShortInfoFrame(item),anchor=tkinter.NW,tags='item_short_info')
				except (IndexError,ValueError):
					pass
		except IndexError:
			pass
				
	
