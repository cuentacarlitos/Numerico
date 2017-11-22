#!/usr/bin/env python
# -*- coding: utf-8 -*-
file = open('datos201612.txt', 'r')

class Info(object):
	"""__init__() functions as the class constructor"""
	def __init__(self, mag=None, tec=None, dia=None,year=None,mes=None,dias=None):
		self.mag = mag
		self.tec = tec

		self.year= year
		self.mes = mes
		self.dias=dias

class Station(object):
	"""__init__() functions as the class constructor"""
	def __init__(self, number=None, info=None):
		self.number = number
		self.info =  []

def read_archive():
	line= ' '
	infoList=[]
	stationList=[]
	i=1
	while(line):
		if(i<1489):
			line=file.readline()
			est= ''
			mag= ''
			tec= ''
			diar= ''
			year= ''
			mes= ''
			for w in range(0,8):
				est=est+line[w]
			for w in range(8,10):
				mag=mag+line[w]
			for w in range(10,12):
				tec=tec+line[w]
			for w in range(12,14):
				diar=diar+line[w]
			for w in range(14,16):
				year=year+line[w]
			for w in range(16,18):
				mes=mes+line[w]
			daysList=[None]
			x=18
			y=x+6
			while (y!=210):
				dia=''
				for w in range(x,y):
					dia=dia+line[w]
					#daysList.append(dia)
				daysList.append(dia)
				x=y
				y=x+6
			i=i+1
			newInfo=Info(mag,tec,year,mes,daysList)
			already=False
			for w in stationList:
				if((est==w.number) & (mag != '08')):
					already=True
					w.info.append(newInfo)
			if not(already):
				auxStation=Station(est,newInfo)
				auxStation.info.append(newInfo)
				stationList.append(auxStation)
		else:
			line=''
	return stationList