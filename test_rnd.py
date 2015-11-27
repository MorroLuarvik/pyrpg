#!/usr/bin/python
# -*- coding: utf-8 -*-

from rnd import Rnd

rnd = Rnd()
	
cou = 0
while rnd.get() <> 0:
	cou += 1
print('from 0 to 0: {0} ones'.format(cou))


simples = [2]
end = 7000 #65535 #1000000000
lastSimple = simples[-1]
while simples[-1] < end:
	lastSimple += 1
	isSimple = False
	for findedSimples in simples:
		if lastSimple % findedSimples == 0:
			isSimple = False
			break
		isSimple = True
	if isSimple:
		simples.append(lastSimple)
	
print(simples[-1])
print(simples[-20])
print(simples[-30])


print(rnd.get(2))
print(rnd.get(2))
print(rnd.get(2))
print(rnd.get(2))
print(rnd.get(2))
print(rnd.get(2))
print(rnd.get(2))
print(rnd.get(2))
print(rnd.get(2))
print(rnd.get(2))
print(rnd.get(2))
