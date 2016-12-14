print "hola mundo"

variable = "hola mundo desde la variable"
print variable

variable= 5
print variable

variable= '234asdfgd'
print variable

pepe = True

print variable
if pepe == True:
	print True
elif pepe =='Mundo':
	print False
else:
	
	pass 
	""" igual al break """

mi_lista = ['cadena',12,True,[1,False]] 
""" la lista puede tener modo edicion, por lo que alberga metodos,lista primer valor 'cadena'es texto, integer, boolean y el cuarto element es una lista con un entero y un booleano """


mi_lista.append('otro elemento')
""" con esto anadimos mas elementos a la lista """

mi_lista[0]= 'cadenas' 
""" con esto sobreescribo la direccion 0 """

print mi_lista

print mi_lista[0]

mi_tupla=('tupla',12,False)
"""  tuplas no se puede modificar en ejecucion sus campor, solo lectura """
print mi_tupla
print mi_tupla[0]

mi_diccionario={'nombre':'Raul',
				'apellido':'Abejon',
				'edad':33,
				}
print mi_diccionario

print mi_diccionario['edad']

for i in mi_lista :
	print i 

for i in mi_tupla :
	print i
i= 0
for i in mi_diccionario :
	print mi_diccionario[i]
	""" imprime la clave """


