# -*- coding: utf-8 -*-
# author:   Григорий Никониров
#           Gregoriy Nikonirov
# email:    mrgbh007@gmail.com
#

#~ import GUI.core as gg
from GUI.core import *
from GUI.core import _TEXTURIES
from MGD.item import Inventory,Item,_ITEM_CLASS,_ITEM_TYPES
import glob
import random
import time
import threading

def test1():
	s=GUICore()
	#~ s=GUICore(100,50)
	s.mainloop()
def test2():
	s=GUICore()
	#~ tl=s._GUICore__textures.getTextureList()
	tl=_TEXTURIES.getTextureList()
	for i,e in enumerate(tl):
		s.placeTexture(e,i%10*50,i//10*50,str(i))
	threading.Thread(target=test2_1(s,tl))
	s.mainloop()
def test2_1(s,tl):
	time.sleep(2)
	for i,e in enumerate(tl):
		s.removeByTag(str(i))
		time.sleep(1)
def test3():
	s=GUICore()
	a=AskFrame('lol?',lambda:print('ok'),lambda:print('no'))
	s.placeWidget(a,50,50)
	s.mainloop()
def test4():
	s=GUICore()
	b=Inventory([123,12,312,3,3,42,4])
	a=InventoryFrame(b)
	s.placeWidget(a,10,10)
	s.mainloop()
def test5():
	s=GUICore()
	b=Item()
	a=ItemShortInfoFrame(b)
	s.placeWidget(a,10,10)
	s.mainloop()
def test6():
	s=GUICore()
	b=Inventory()
	for i in range(30):
		b.add(Item(str(i),random.choice(_ITEM_TYPES),random.choice(_ITEM_CLASS)))
	a=InventoryFrame(b)
	s.placeWidget(a,10,10)
	c=EntityInfoFrame(1)
	s.placeWidget(c,300,10)
	s.mainloop()
def test7():
	s=GUICore()
	a=EntityInfoFrame(1)
	s.placeWidget(a,10,10)
	s.mainloop()
	
	
