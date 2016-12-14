"""tuplas"""
def tuplas():
    
    print "Para declarar una tupla podemos guiarnos con el ejemplo: mi_tupla=('uno',2,'tres',4) y estas son estaticas"
    print "los elementos numericos se incluyen tal cual, y los tipo string entre-comillados"
    print "El que sean estaticas quiere decir que sus valores no podran alterarse una vez definidas aunque podemos usar alguna tecnica que veremos mas adelante" 
    mi_tupla=('uno', 2 ,'tres',4)
    print str(mi_tupla)+" esto es una tupla y sus elementos se engloban con el parentesis ()"
    print "las tuplas pueden contener otras tuplas, listas , diccionarios o combinaciones entre ellas y otros tipos de datos"
    print "dentro de las tuplas podemos realizar alguna accion que tambien podremos realizar en las listas, asique lo que aprendas con las tuplas podras aplicarlo en las listas"
    print "puedes probar y crear tu primera tupla: atrevete"
    print "permite que te guie, colola el cursor justo a la derecha de >>>"
    print ""
    print "Ejercicio 1 Declara tu primera tupla"
    print "Escribre primera_tupla=('uno',2,'tres',4) aunque te invito a que uses tus propios nombres y hagas la tupla a tu libre albedrio si tienes problemas te puedes cenir al ejemplo"
    print "Ahora podras listar la tupla si escribes el nombre de la tupla"
    print "Cuando creas que has practicado lo suficiente y quieras avanzar hazmelo saber escribiendo continuar(1)"

    
def continuar(continuar):    
    
    if continuar == 1:
        acciones_tuplas()
    if continuar == 2:
        acciones_tuplas2()
    if continuar == 3:
        acciones_tuplas2_1()
    if continuar == 4:
        acciones_tuplas2_2()
    if continuar ==5:
        acciones_range()
    if continuar == 6:
        accion_enumerar_tuplas()
    if continuar ==7:
        accion_enumerar_listas()
    

def acciones_tuplas():
    print "ACCESO A LOS ELEMENTOS POR EL INDICE"
    print "Podemos seleccionar de elementos de la tupla individualmente por su indice"
    print "Cuando declaramos una tupla=(1,2,3,4) esta tupla contiene 4 elementos y estos se posicionan segun se hayan definido, cojiendo el elemento de la izquierda el primer indice que siemrpe empiezan por 0"
    print "Por lo tanto los indices de tupla es de 4 empezando por el 0 .(0,1,2,3)"
    print "entonces para que nos muestre el primer elemento en este ejemplo es el uno, deberiamos llamarlo por su indice 0"
    
    """Seleccion de elementos de la tupla/lista unidimensional """
    
   
    print "EJERCICIO 2 :"
    mi_tupla=('uno', 2 ,'tres',4)
    print (mi_tupla) 
    print "ejemplo : tupla[0] te invito a que crees la tupla del ejemplo llames a cada elemento por su indice y lo descrubras por ti mismo "
    print "primer elemento de la tupla tiene direccion 0 se define mi_tupla[0] y su contenido es "+ mi_tupla[0]
    print "segundo elemento de la tupla tiene direccion 1 se define mi_tupla[1] y su contenido es "+ str(mi_tupla[1])
    print "tercer elemento de la tupla tiene direccion 2 se define mi_tupla[2] y su contenido es "+ mi_tupla[2]
    print "cuarto elemento de la tupla tiene direccion 3 se define mi_tupla[3] y su contenido es "+ str(mi_tupla[3])
    print "cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(2)"
    print ""
"""SELECIONAR DETEREMINADO RANGO SLICING"""
def acciones_tuplas2():
    print "SELECIONAR DETEREMINADO RANGO POR EL INDICE (SLICING) '"
    mi_tupla=('uno', 2 ,'tres',4)
    print (mi_tupla)
    print "si queremos selecionar un determinado rango de elementos de la tupla/lista podemos hacerlos por el INDICE con una relacion [desde:hasta:seleccion en saltos]"
    print "recuerda que el primer elemento de listas y tuplas se ubica en la posicion 0"
    print "mi_tupla[0:0] "+ str(mi_tupla[0:0])+" busca desde la posicion 0 hasta la 0 sin ser incluido devuelve el tipo de dato tupla = () "
    print "mi_tupla[0:1] "+ str(mi_tupla[0:1])+" del indice 0 hasta el indice 1 sin contar esta ultima"
    print "mi_tupla[0:2] "+ str(mi_tupla[0:2])+" del indice 0 hasta el indice 2 sin contar esta ultima"
    print "mi_tupla[0:3] "+ str(mi_tupla[0:3])+" del indice 0 hasta el indice 3 sin contar esta ultima"
    print "mi_tupla[0:4] "+ str(mi_tupla[0:4])+" del indice 0 hasta el indice 4 sin contar esta ultima"
    print "mi_tupla[1:4] "+ str(mi_tupla[1:4])+" del indice 1 hasta el indice 4 sin contar esta ultima"
    print  "EJERCICIO 3"
    print " crea una tupla de cuatro elementos y juega con los rangos explorando desde el indice  "
    print "cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(3)"
"""printeo de un rango de direcciones"""
def acciones_tuplas2_1():
    print "SLICING DIMENSIONAL"
    print "las tuplas pueden tener varias dimensiones ejemplo mi_tupla2=(('uno', 2 ,'tres',4),('cinco',6,'siete',8))"
    mi_tupla2=('uno', 2 ,'tres',4),('cinco',6,'siete',8)
    print str(mi_tupla2)+"es una tupla bidimensional"
    print "Al tener 2 dimensiones este ejemplo, python trata la tupla/lista misma manera pero de forma conjunta,si antes hablabamos de una dimension trataba los elementos de ese conjunto, ahora al tener varios conjuntos se comportara de la misma manera para esos conjunto y si queremos tratar una dimension deberemos hacerlo de forma independiente"
    print "mi_tupla2[0:0]= "+ str(mi_tupla2[0:0])+" desde la posicion 0 hasta la 0 sin incluirla no encuentra nada pero sabemos si se trata de una lista o tupla en este caso es tupla"   
    print "mi_tupla2[0:1]= "+ str(mi_tupla2[0:1])+" selecionamos desde 0 al primera dimension"
    print "mi_tupla2[1:0]= "+ str(mi_tupla2[1:0])+" esto no tendria sentido ya que le decimos que mire desde la 1 hasta la 0 sin incluir 0 "
    print "mi_tupla2[1:1]= "+ str(mi_tupla2[1:2])+" selecionamos desde primera dimension hasta la dimension"
    print "mi_tupla2[0:2]= "+ str(mi_tupla2[0:2])+" selecionamos desde 0 hasta la segunda dimension"
    print "Cuando creas que has practicado lo suficiente hazmelo saber con continuar(4)"
def acciones_tuplas2_2():
    print "AHORA CON LOS 3 ARGUMENTOS A TOPE"
    print "Ya sabemos como acceder a un determinado rango por los indices de la tupla"
    print "haciendo uso de [desdeIndice:HastaSinSerIncluido] pero aun no hemos usado el tercer parametro que podemos incluir la seleccion de la informacion"
    print "Para acceder a un determinado rango lo haremos de la siguiente manera mi_tupla[desde:hasta:seleccion en saltos]"
    print "Recuerda las tuplas son estaticas y las listas dinamicas"
    print "ejemplo numeros=(0,1,2,3,4,5,6,7,8,9,10)"
    print "numeros[0:10:2] "
    print "[desde:hasta:seleccion en saltos] significado de los parametros"
    print "Como podemos ver le estoy diciendo que desde el indice 0 hasta el indice 10=9 sin ser este incluido y que estos los muestra cada 2 indices"
    print "de tal forma que deberia printear (0,2,4,6,8)"
    print " EJERCICIO 4"
    print "Haz una practica y juega con el ultimo valor para que lo experimentes de tu propia mano"
    print "cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(5)"
    
    
    print ""
"CREAR LISTAS CON RANGE "
def acciones_range():
    print "CREAR LISTAS/TUPLAS CON RANGE"
    print "creo una lista de enteros para el ejemplo con [range] mi_listin = range[20], esto crea una lista en ese rango del 0 al 19"
    mi_listin = range(20)
    print (mi_listin)
    print "ahora convierto la lista en tupla ya que range solo crea listas pero despues podemos convertirlas a tuplas con tuple"
    print "mi_listin =tuple(range(20))"
    mi_listin =tuple(range(20))
    print (mi_listin)
    print "REPETICION"
    print"podemos consultar determinados rangos y que nos devuelva el valor en la medida que nos interese mi_listin[0:20:2] Como en el ejercicio 4"
    print mi_listin[0:20:2]
    print "solo sirve para crear listas numericas"
    print "practica un poco creando una lista con range y combinarlo con lo aprendido en el ejercicio 4"
    print "Ejercicio 5:"
    print "cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(6)"
    print ""
"""ENUMERAR EL INDICE"""
def accion_enumerar_tuplas():
    print "ENUMERAR UNA TUPPLA POR EL INDICE CON [ENUMERATE]"
    print "creo una tupla con rango 20 con mi_listin = range(20)"
    print "Por si acaso me aseguro de que lo que creo es una tupla y puedo hacerlo de la siguiente manerami_listin = tuple(mi_listin) "
    mi_listin = range(20)
    mi_listin = tuple(mi_listin)
    print "'print' tuple(enumerate(mi_listin)) es una tupla" 
    print tuple(enumerate(mi_listin))
    print "Cuando creas que has practicado lo suficiente hazmelo saber con continuar(7)"
def accion_enumerar_listas():
    print "ENUMERAR UNA LISTA POR EL INDICE CON [ENUMERATE]"
    print "Vamos dominando las tuplas a si que el siguiente ejemplo sera una lista"
    print "las listas se recorren de la misma forma que las tuplas"       
    print "las listas se definen ejemplo mi_lista=('1',dos,'3',cuatro)"
    print "las diferencias entre las tuplas en deficion tupla=() vs lista=[]"
    print "las listas son dinamicas, por lo que podemos agregar,borrar,modificar elementos etc que no se pueden hacer con las tuplas"
    print "las listas son dinamicas a diferencia de las tuplas y eso nos abre unas funcionalidades extra que iremos viendo mas adelante"
    print "Ahora vamos a repetir el ejercicio pero tomando contacto con las listas asique puedes guiarte por el siguiente ejemplo y veras la similitud/diferencias con las tuplas"
    print "creo una lista con rango 20 con mi_liston = range(20)"
    mi_liston = range(20)
    mi_liston = list(mi_liston)
    print "'print' list(enumerate(mi_listin)) es una lista" 
    print list(enumerate(mi_liston))
    print "Como podras observar se comparta de la misma manera, y apreciaras que ya no va entre parentesis, si no entre corchetes"
    print "Cuando creas que has practicado lo suficiente hazmelo saber con continuar(8)"
print ""
"""MODIFICAR VALORES EN CONJUNTO MEDIANTE SLICING"""
def acciones_mod_slic_listas():
    mi_listin = range(20)
    print "MODIFICAR VALORES SOLO EN LISTAS"
    print "Recordamos que las tuplas son estaticas y las listas dinamicas,verdad ??"
    print "pues "
    print "mi_listin[6:7]='seis','sieto','ocho'"
    mi_listin[6:9]="seis","siete","ocho"
    print (mi_listin)
print ""


print ""
"""OBTENER LA POSICION DEL ELEMENTO POR SU VALOR [INDEX]"""
print "OBTENER LA POSICION DEL ELEMENTO POR SU VALOR"
print "nombres=['juan','pepe','kiko','jose']"
print "print (nombres.index('pepe'))"
nombres=['juan','pepe','kiko','jose']
print (nombres.index('pepe'))
print ""
"""SABER CUANTAS VECES APARECE UN ELEMENTO EN UNA LISTA"""
print "SABER CUANTAS VECES APARECE UN ELEMENTO EN UNA LISTA [COUNT]"
print "cosas=['raton','teclado','monitor','cpu','monitor','raton','raton']"
print "print (cosas.acount('raton'))"
print "print (cosas.acount('monitor'))"
print "(cosas.acount('teclado'))"
cosas=['raton','teclado','monitor','cpu','monitor','raton','raton']
print "El raton aparece "+str(cosas.count('raton'))+" veces"
print "El monitor aparece "+str(cosas.count('monitor'))+" veces"
print "el teclado aparece "+str(cosas.count('teclado'))+" veces"
print ""
"""ORDENADAR LISTAS [SORT]"""
print "ORDENADAR LISTAS"
print " numeros=[43,5,4,67,32]"
print "print (numeros)"
print " numeros.sort()"
print "print (numeros) "
numeros=[43,5,4,67,32]
print (numeros)
numeros.sort()
print (numeros)
print "Funciona de igual manera con los string y los ordena alfabeticamente"
print " animales=['zorro','pato','gato','anguila','burro']"
print " print (animales)"
print " animales.sort()"
print " print (animales)"
animales=['zorro','pato','gato','anguila','burro']
print (animales)
animales.sort()
print (animales)
print ""
"""INVERTIR LISTAS """
print "INVERTIR LISTAS Y PUEDE COMBINARSE CON [SORT] [REVERSER]"
letras=['g','w','x','j','v','a']
print (letras)
letras.reverse()
print (letras)
print "Comprobamos que altera inversamente el contenido del letras si probamos a ordenarlo primero y despues invertirlo"
letras.sort()
letras.reverse()
print (letras)
print ""

"""CONVERSIONES"""
print ""
print "Conversiones de lista a tupla y viceversa"
print "mi_lista=[1,'dos',3,'cuatro']" 
print "mi_lista_tupla=tuple(mi_lista)"
print "mi_tupla_lista=list(mi_lista_tupla)"
mi_lista=[1,'dos',3,'cuatro']
print str(mi_lista)+" esto es una lista"
"""transformo una lista a una tupla"""
mi_lista_tupla=tuple(mi_lista)
print str(mi_lista_tupla)+" he volcado el contenido de mi_lista en mi_lista_tupla y tranformandolo en una tupla 'mi_lista_tupla=tuple(mi_lista)' "
"""tranformo una tupla en una lista"""
mi_tupla_lista=list(mi_lista_tupla)
print str(mi_tupla_lista)+" he volcado el contenido de mi_lista_tupla(tupla) en mi_tupla_lista(lista) mi_tupla_lista=list(mi_lista_tupla)"
print ""
print ""
"""asignacion de valores"""
print "ASIGNACION DE 1 ELEMENTO A LA DERECHA a la lista con el metodo [append]: Solo permite un argumento"
print "mi_lista1=[1,2,3]"
print "mi_lista1.append(4)"
mi_lista1=[1,2,3]
print (mi_lista1)
mi_lista1.append(4)
print (mi_lista1)
print "mi_listac=['uno','dos','tr3s']"
print "mi_listac.append('cuantr0')"
mi_listac=['uno','dos','tr3s']
print (mi_listac)
mi_listac.append('cuantr0')
print (mi_listac)
print ""
print "ASIGNACION DE VARIOS VALORES POR LA DERECHA [EXTEND]"
print "mi_lista1.extend[5,6,7,8,9]"
mi_lista1.extend([5,6,7,8,9])
print (mi_lista1)

"""MODIFICAR/SOBRE-ESCRIBIR ELEMENTOS EXISTENTES"""
print "Modificar elementos existentes"
print "mi_lista_C[0]=1 cambio el elemento 0 que es el primer elemento de la lista que es uno por 1"
mi_listac[0]=1
print (mi_listac)
"""INSERTAR ELEMENTOS EN LA POSICION DETERMINADA"""
print ""
print "Insertar elementos en la posicion determinada con el metodo [insert]:"
print "mi_listab=['a','b','c']"
print "mi_listab.insert(0,'letras')"
mi_listab=['a','b','c']
mi_listab.insert(0,'letras')
print (mi_listab)
print ""
print ""
print "Insertar elementos en la posicion determinada con el metodo [insert]:"
print "mi_listab=[1,2,3,5]"
print "mi_listab.insert(3,'4') coloco el elmento numero 4 en la posicion numero 3 ya que empienza en 0"
mi_listab = [1,2,3,5]
mi_listab.insert(3,'4')
print (mi_listab)
print ""
"""ELIMINAR ELEMENTOS POR SU VALOR ESPECIFICO"""
print "Eliminar Elementos por el valor del argumento [remove]"
print "mi_listab.remove(2) borrara el elemento si coincide con el argumento dado en este caso el 2"
mi_listab.remove(2)
print (mi_listab)
print ""
"""ELIMINAR ELEMENTOS POR SU POSICION"""
print "Eliminar elementos por su posicion[del]"
print "del mi_listab[3]  la posicion 3 equilvaldria al elemento con valor 5 "
del mi_listab[3]
print (mi_listab)
print "podemos combinar el [del] con la forma de determinar los rangos mi_lista[0:2] del 0 hasta el 2"
del mi_listab[0:2]
print (mi_listab)
print ""
"""ELIMINAR UN ELEMENTO INDICANDO SU POSICION Y OBTENER EL ELEMENTO ELIMINADO"""
print "ELIMINAR UN ELEMENTO INDICANDO SU POSICION Y OBTENER EL ELEMENTO ELIMINADO[.POP]"
print "mi_array=['tele','radio','movil','tablet']"
print "borrado=mi_array.pop(1)"
print "print (mi_array)"
print "print (borrado)"
mi_array=['tele','radio','movil','tablet']
borrado=mi_array.pop(1)
print (mi_array)
print (borrado)

"""ELIMINAR TODOS LOS ELEMENTOS"""
print ""
print "Eliminar todos los elementos con la funcion [del]"
print "del mi_listab[:] esto dejaria la lista totalmente vacia"
del mi_listab[:]
print (mi_listab)
"""CANTIDAD DE ELEMENTOS"""
print ""
print "Contar la cantidad de elementos con la funcion [len]"
print "len(mi_listab)"
print len(mi_listab)
print "mi_listap=['tuplas','listas','diccionarios']"
mi_listap=['tuplas','listas','diccionarios']
print (mi_listap)
print len(mi_listap)
print ""
"""DESEMPAQUETAMIENTO O UNPACKING"""
print "UNPACKING"
print "Asignar valores de una lista a un conjunto de objetos"
print "mis_datos=('Raul','Abejon','30','soltero)"
print "nombre, apellido, edad,estado=mis_datos"
mis_datos=('Raul','Abejon','30','soltero')
nombre, apellido, edad, estado=mis_datos
print (nombre)
print (apellido)
print (edad)
print (estado)
print "Para que sea efectivo el numero de valores ha de coincidir con el numero de objetos"
mis_datos=list(enumerate(mis_datos))
for i in mis_datos:
    print (i)
print "como vemos al asociar elementos de una lista/tupla a objetos no incide en su indice"
print "tambien podemos combinar el indice de la lista con los objetos"
print "mis_datos2=('rul','tecnico','si','no')"
print "estudia, trabaja =mis_datos2[2:] relaciono los objetos desde el elemento 2 siendo los 2 ultimos en el ejemplo"
mis_datos2=('rul','tecnico','si','no')
estudia, trabaja = mis_datos2[2:]
print (mis_datos2)
print "estudia, trabaja =mis_datos2[:2] relacion los objetos hasta el elemento 2 sin incluirlo siendo los 2 primeros en el ejemplo"
nombre, titulo = mis_datos2[:2]
print (mis_datos2)
"""ZIP"""
print "[ZIP]"
print "Parecido a UNPACKING aunq vemos que crea una tupla por relacion entre indices de ambas listas"
print "cabecera = ['name','email','login'] "
print "union = zip(cabecera,dtos) "

print "print 'printeo con un for' "
print "for cabecera, dtos in union: "
print "     print (str(cabecera)+' :'+str(dtos))"
cabecera = ['name','email','login']
dtos = ['raul','drohne@gmail.com','drohne@gmail.com']
union = zip(cabecera,dtos)
print "print (union) "
print (union)
print "printeo con un for"
for cabecera, dtos in union:
    print (str(cabecera)+" : "+str(dtos))
print ""
    
"""SETS"""
print "[SET]"
print "es un conjunto de valores que no se pueden acceder desde el indice y no puede tener valores repetidos"
print "utensilios = ['tenedor','cuchillo','cuchara','cuchara','cuchillo','tenedor']"
print "print (utensilios)"
utensilios = ['tenedor','cuchillo','cuchara','cuchara','cuchillo','tenedor']
print (utensilios)
print "utensilios = set(utensilios)"
print "print (utensilios)"
utensilios = set(utensilios)
print (utensilios)
print "utensilios = list(set(utensilios)) "
print "print (utensilios) "
utensilios = list(set(utensilios))
print (utensilios)
print "utensilios = tuple(set(utensilios)) "
print "print (utensilios) "
utensilios = tuple(set(utensilios))
print (utensilios)
print ""
print "AnADIR ELEMENTOS en [set.add()]"
print "utensilios = set(utensilios) "
print "utensilios.add('hola') "
print "utensilios.add(1) "
print "utensilios.add('asd') "
print (utensilios)
print ""
utensilios = set(utensilios)
utensilios.add('hola')
utensilios.add(1)
utensilios.add('asd')
print (utensilios)
print "comprobamos que al anadir un elemento lo deja sin orden aparante"
print " "
print "ELIMINAR ELEMENTOS  en [set.remove()]"
print "utensilios.remove('cuchara') "
utensilios.remove('cuchara')
print (utensilios)
print "utensilios.remove('cuchillo') "
utensilios.remove('cuchillo')
print (utensilios)
print "utensilios.remove('tenedor') "
utensilios.remove('tenedor')
print (utensilios)
print "BUSCAR ELEMENTOS  en [set]"
print "print 'asd' in utensilios"
print 'asd' in utensilios
print ""
print "============================================================================================="
print "                    TUTORIAL PYTHON SOBRE TUPLAS LISTAS Y DICCIONARIOS"
print "=============================================================================================="
print "                               (TUPLAS) [LISTAS] Y {{DICCIONARIOS}"
print "Son tipos de datos como los arrays pero con particularidades que iremos explicando de forma detallada."
print "Los tipos de datos que pueden albergar pueden ser de cualquier tipo: int,boolean,string,objetos, listas,tuplas,diccionarios "
print "Para empezar con el tutorial escribe el tipo de dato por el cual quieres investigar, las opciones son: tuplas,listas o diccionarios"
print "Mi recomendacion esque empieces por las tuplas, continues con las listas y terminas con los diccionarios"
print "Por donde vas a empezar ?? typea tuplas, listas o diccionario para empezar"
nombre = raw_input()
print nombre
if nombre == 'tuplas':
    tuplas()










