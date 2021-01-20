#Se citesc elementele unei liste, care reprezintă numere întregi (pozitive și negative). Să se afișeze la ecran:
	#a) conținutul (elementele) listei /lista1
	#b) lista sortată în ordine crescătoare / lista2
	#c) lista sortată în ordine descrescătoare / lista3
	#d) numărul de elemente din listă
	#e) elementul MAX
	#f) elementul MIN
	#g) să se adauge la coadă în lista inițială elementul – 111. 
	   # Să se afișeze lista nou-formată. / lista4
	#h) să se adauge pe poziția a doua din lista inițială elementul – 222. 
	    #Să se afișeze lista nou-formată. / lista5
lista1=[20,0,1,21,3,6,-4,-17]
print('a.lista1:',lista1)
lista2=sorted(lista1)
print('b.lista2:',lista2)
lista3=sorted(lista1,reverse=True)
print('c.lista3:',lista3)
print('d.numarul de elemente:',len(lista1))
print('e.numarul maxim:',max(lista1))
print('f.numarul minim:',min(lista1))
lista1.extend([111])
print('g.lista4:',lista1)
lista1.remove(111)
lista1.insert(2,'222')
print('h.lista5:',lista1)