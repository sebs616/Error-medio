x3=0
count=0
lista=[]

def valormedio():
	suma=0
	seguir=True
	cuenta=0
	promedio=0

	while seguir:
		y1=input("---------------------:")
		
		if y1==0:
			promedio=suma/cuenta
			error_medio(promedio, cuenta, promedio, lista)
			break

		lista.append(y1)

		cuenta+=1
		suma+=y1
		print "suma", suma
		print "cuenta", cuenta


def error_medio(valor_medio, count, promedio, lista):
	reference=0
	x3=0


	while len(lista)>0:
		x1=lista.pop()

		x2= x1-valor_medio
		print x1, "-", valor_medio, "=", x2
		if x2 < 0:
			x2=x2*-1

		x3+=x2
	print"----------------------------------------------------------------"
	print""
	print "value= ", x3
	print "error medio = ", x3/count, count
	print "valor medio = ", promedio
	


valormedio()
