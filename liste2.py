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
with open('lista.txt','r')as f:
    lista1=f.readline()
a=(lista1)
with open('lista1.txt','w') as f:
    f.write(str(a))
b=sorted(lista1)
with open('lista2.txt','w') as f:
     f.write(str(b))
c=sorted(lista1,reverse=True)
with open('lista3.txt','w') as f:
     f.write(str(c))
d=len(lista1)
with open('cardinal.txt','w') as f:
     f.write(str(d))
e=max(lista1)
with open('max.txt','w') as f:
     f.write(str(e))
f=min(lista1)
with open('min.txt','w') as f:
     f.write(str(e))
lista1.extend([111])
with open('list4.txt','w') as f:
     f.write(str(lista1))
lista1.remove(111)
lista1.insert(2,'222')
with open('lista5.txt','w') as f:
     f.write(str(lista1))