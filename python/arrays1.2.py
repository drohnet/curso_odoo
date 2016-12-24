##############################################################################################################################################
#################################### tutorial de listas tuplas acciones comunes y especificas ################################################
#####################################################drohne@gmail.com#########################################################################
##############################################################################################################################################
def indice():
    print "ACCIONES SOBRE LISTAS Y TUPLAS"
    print "CONTENIDO:comando a teclear"
    print "INDEX:continuar('i')"
    print "TUPLAS:continuar(0)"
    print "ACCESO A LOS ITEMS POR EL INDICE:continuar(1)"
    print "TUPLAS 1 DIMENSIONES RANGO POR EL INDICE :continuar(2)"
    print "TUPLAS 2 DIMENSIONES ACCESO ELEMENTOS POR INDICE:continuar(3)"
    print "AHORA CON LOS 3 ARGUMENTOS:continuar(4)"
    print "CREAR LISTAS/TUPLAS CON RANGE:continuar(5)"
    print "ENUMERAR EL INDICE[ENUMERATE]:continuar(6)"
    print "ENUMERAR UNA LISTA POR EL INDICE CON [ENUMERATE]:continuar(7)"
    print "OBTENER LA POSICION DEL ELEMENTO POR SU VALOR [INDEX]:continuar(8)"
    print "SABER CUANTAS VECES APARECE UN ELEMENTO EN UNA LISTA [COUNT]:continuar(9)"
    print "SABER CUANTAS VECES APARECE UN ELEMENTO EN UNA TUPLA [COUNT]:continuar(10)"
    print "SABER LA CANTIDAD DE ELEMENTOS DE UNA LISTA/TUPLA [LEN]:continuar(11)"
    print "CONVERSIONES ENTRE LISTAS TUPLAS Y VICIVERSA:continuar(12)"
    print "RESUMEN E INDICE:continuar(13)"
    print "LISTAS continuar:(14)"
    print "ORDENADAR LISTAS INT[SORT]:continuar(15)"
    print "ORDENADAR LISTAS DE STRING CON [SORT]:continuar(16)"
    print "INVERTIR LISTAS [REVERSER]:continuar(17)"
    print "ASIGNACION DE 1 ELEMENTO A LA DERECHA [APPEND]:continuar(18)"
    print "ASIGNACION DE VARIOS VALORES POR SU DERECHA [EXTEND]:continuar (19)"
    print "ASIGNACION DE ELEMENTOS EN UNA POSICION DETERMINADA:[INSERT] continuar(20)"
    print "ELIMINAR ITEMS POR SU PROPIO VALOR:[REMOVE]:continuar(21)"
    print "ELIMINAR ITEMS POR SU POSICION[DEL]:continuar(22"
    print "ELIMINAR ITEMS POR SU POSICION RETORNANDO EL ITEM ELIMINADO[POP]:continuar(23)"
    print "ELIMINAR TODOS LOS ELEMENTOS CON LA FUNCION [DEL]:continuar(24)"
    print "MODIFICAR ITEMS POR SU POSICION DE INDICE:continuar(25)"
    print "MODIFICAR ITEMS POR SU POSICION DE INDICE EN UN RANGO DE INDICES:continuar(26)"
    print "RESUMEN LISTAS continuar(27)"
    print "ASOCIAR OBJETOS A ELEMENTOS DE UNA LISTA/TUPLA continuar(28)"
    print "ASOCIAR OBJETOS A ELEMENTOS DE UNA LISTA/TUPLA POR INDICE DE RANGO continuar(29)"
    print "ZIP continuar(30)"
    print "SETS continuar(31)"
    print "ANADIR ELEMENTOS EN SET.ADDcontinuar (32)"
    print "ELIMINAR ELEMENTOS SET.REMOVE continuar(33)"
    print "BUSCAR ELEMENTOS EN SET continuar (34)"
    
def continuar(continuar):
    if continuar == 'i':
        indice()
    if continuar == "tuplas" or continuar == 0:
        tuplas()
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
    if continuar == 8 :
        accion_index()
    if continuar == 9 :
        accion_howmany_list()
    if continuar == 10 :
        accion_howmany_tuple()
    if continuar == 11 :
        accion_howmany_items()  
    if continuar == 12 :
        conversiones1()
    if continuar == 13 :
        resumen_acceso()
    if continuar == 14 or continuar== "listas" :
        accion_listas() 
    if continuar == 15 :
        accion_ordenarn()
    if continuar == 16 :
        accion_ordenarl()
    if continuar == 17 :
        accion_invertir()
    if continuar == 18 :
        accion_asigd()
    if continuar == 19 :
        accion_asig2()
    if continuar == 20 :
        accion_insert1()
    if continuar == 21 :
        accion_elem1()
    if continuar == 22 :
        accion_elem2()
    if continuar == 23 :
        accion_elem3()
    if continuar == 24 :
        accion_elem4()
    if continuar == 25 :
        acciones_mod_slic_lista()
    if continuar == 26 :
        acciones_mod_slic_listas()
    if continuar == 27 :
        acciones_lista_repaso()
    if continuar == 28 or continuar == "extras" : 
        unpack()
    if continuar == 29 :
        unpack2()
    if continuar == 30 :
        zips()
    if continuar == 31 :
        sets()
    if continuar == 32 :
        sets2()
    if continuar == 33 :
        sets3()
    if continuar == 34 :
        sets4()
"""tuplas"""
def tuplas():
    print "Las tuplas junto con las listas y diccionarios son un tipo de dato complejo similar en otros lenguajes como java o c a los arrays o vectores con alguna particularidad que iremos viendo poco a poco en este tutorial"
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
    
def acciones_tuplas():
    print "ACCESO A LOS ITEMS POR EL INDICE"
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
"""SELECIONAR DETEREMINADO RANGO """
def acciones_tuplas2():
    print "SELECIONAR DETEREMINADO RANGO POR EL INDICE UNIDIMENSIONAL '"
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
    print "TUPLAS 2 DIMENSIONES ACCESO ELEMENTOS"
    print "las tuplas/listas pueden tener varias dimensiones(mas de 1 tupla/lista/dic o combinacion de ellas) ejemplo mi_tupla2=(('uno', 2 ,'tres',4),('cinco',6,'siete',8))"
    mi_tupla2=('uno', 2 ,'tres',4),('cinco',6,'siete',8)
    print str(mi_tupla2)+"es una tupla bidimensional una tupla compuesta de 2 tuplas"
    print "Al tener 2 dimensiones este ejemplo, python trata la tupla/lista misma manera pero de forma conjunta,si antes hablabamos de una dimension trataba los elementos de ese conjunto, ahora al tener varios tuplas/listas se comportara de la misma manera para esos conjunto y si queremos tratar una dimension deberemos hacerlo de forma independiente"
    print "EJEMPLO1 :"
    print "mi_tupla2[0:0]= "+ str(mi_tupla2[0:0])+" desde indice de dimension 0 hasta indice de dimension 0 sin incluirla no encuentra nada pero sabemos si se trata de una lista o tupla en este caso es tupla"   
    print "mi_tupla2[0:1]= "+ str(mi_tupla2[0:1])+" selecionamos desde indice de dimension 0 hasta indice de dimension 1 sin ser incluido"
    print "mi_tupla2[1:0]= "+ str(mi_tupla2[1:0])+" esto no tendria sentido ya que le decimos que mire desde la 1 hasta la 0 sin incluir 0 "
    print "mi_tupla2[1:2]= "+ str(mi_tupla2[1:2])+" selecionamos desde indice de dimension 1 hasta el indice de dimension 2 sin ser incluido"
    print "mi_tupla2[0:2]= "+ str(mi_tupla2[0:2])+" selecionamos desde indice de dimension 0 hasta la indice de dimension 2"
    print "EJERCICIO_1=EJEMPLO1"
    print "EJEMPLO 2:"
    print "Entonces si queremos tratar cada elemento de una tupla/lista compuesta de otras listas tuplas deberemos hacerlo de forma individual"
    print "primero tendriamos que averiguar que elemento queremos tratar , con el ejemplo 1 hemos visto como hacerlo"
    print "una vez que tengamos claro cuales son las posiciones de los indices que queremos 'deslogsar' podemos guardarlo en una variable y tratarlos datos por elemento individual"
    print "primer_elemento=mi_tupla2[0:1]"
    print "segundo_elemento=mi_tupla2[1:2]"
    primer_elemento=mi_tupla2[0:1]
    segundo_elemento=mi_tupla2[1:2]
    print "El primer elemento de mi_tupla2 esta en el indice 0 lo he guardado en primer_elemento="+str(primer_elemento)
    print "El primer segundo elemento de mi_tupla2 esta en el indice 1 lo he guardado en segundo_elemento= "+str(segundo_elemento)
    print ""
    
    print "EJERCICIO_2=EJEMPLO2"
    print "Cuando creas que has practicado lo suficiente hazmelo saber con continuar(4)"
def acciones_tuplas2_2():
    print "AHORA CON LOS 3 ARGUMENTOS A TOPE"
    print "ya sabemos crear listas/tuplas"
    print "ya sabemos acceder a los elementos a sus dimensiones  y a los elementos dependiendo de su posicion y dimension "
    print "haciendo uso de [desdeIndice:HastaSinSerIncluido] pero aun no hemos usado el tercer parametro que podemos incluir la seleccion de la informacion"
    print "Para acceder a un determinado rango lo haremos de la siguiente manera mi_tupla[desde:hasta:seleccion en saltos]"
    print "Recuerda las tuplas son estaticas y las listas dinamicas"
    print "ejemplo numeros=(0,1,2,3,4,5,6,7,8,9,10)"
    numeros=(0,1,2,3,4,5,6,7,8,9,10)
    print "numeros[0:10:2] "
    
    print "[desde:hasta:seleccion en saltos] significado de los parametros"
    print "Como podemos ver le estoy diciendo que desde el indice 0 hasta el indice 10=9 sin ser este incluido y que estos los muestra cada 2 indices"
    print "de tal forma que deberia printear (0,2,4,6,8)"
    print " EJERCICIO 4 Y EJEMPLO :"
    print "numeros="+str(numeros)
    print "numeros[0:10:2]"
    print numeros[0:10:2]
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
    print "range() solo sirve para crear listas numericas"
    print "practica un poco creando una lista con range y combinarlo con lo aprendido en el ejercicio 4"
    print "Ejercicio 5:"
    print "cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(6)"
    print ""
"""ENUMERAR EL INDICE"""
def accion_enumerar_tuplas():
    print "ENUMERAR UNA TUPPLA POR EL INDICE CON [ENUMERATE]"
    print "Si necesitamos saber el numero de indice en alguna ocasion podemos usar enumerate() para que nos muestra el numero de indice junto el valor"
    print "como observamos lo hace en una tupla y por cada indice crea una tupla con el numero de indice y el valor del elemento del indice"
    print "creo una tupla con rango 20 con mi_listin = range(20)"
    print "Por si acaso me aseguro de que lo que creo es una tupla y puedo hacerlo de la siguiente manera mi_listin = tuple(mi_listin) aunque tambien puedo decirle ya de paso que lo enumere de la siguiente manera mi_listin = tuple(enumerate(mi_listin)) "
    mi_listin = range(20)
    print (mi_listin)
    mi_listin = tuple(enumerate(mi_listin))
    print "'print' tuple(enumerate(mi_listin)) es una tupla" 
    print (mi_listin)
    print "Cuando creas que has practicado lo suficiente hazmelo saber con continuar(7)"
def accion_enumerar_listas():
    print "ENUMERAR UNA LISTA POR EL INDICE CON [ENUMERATE]"
    print "Vamos dominando las tuplas a si que el siguiente ejemplo sera una lista"
    print "las listas se recorren de la misma forma que las tuplas"       
    print "las listas se definen ejemplo mi_lista=['1',dos,'3',cuatro]"
    print "las diferencias entre las tuplas en deficion tupla=() vs lista=[]"
    print "las listas son dinamicas a diferencia de las tuplas y eso nos abre unas funcionalidades extra que iremos viendo mas adelante"
    print "las listas al ser dinamicas, podemos agregar,borrar,modificar elementos etc que no se pueden hacer con las tuplas"
    print "Ahora vamos a repetir el ejercicio pero tomando contacto con las listas asique puedes guiarte por el siguiente ejemplo y veras la similitud/diferencias con las tuplas"
    print "creo una lista con rango 20 con mi_liston = range(20)"
    mi_liston = range(20)
    print (mi_liston)
    mi_liston = list(enumerate(mi_liston))
    print "mi_liston = list(enumerate(mi_liston))"
    print (mi_liston)
    print "Como podras observar se comparta de la misma manera, y apreciaras que ya no va entre parentesis, si no entre corchetes y cuando usamos enumerate tambien le indicamos si es una tuple o una list"
    print "Cuando creas que has practicado lo suficiente hazmelo saber con continuar(8)"
print ""

"""OBTENER LA POSICION DEL ELEMENTO POR SU VALOR [INDEX]"""
def accion_index():
    print "OBTENER LA POSICION DEL ELEMENTO POR SU VALOR [INDEX]"
    print "Si conocemos el valor especifico podemos consultar su numero de posicion dentro de la tupla/lista mediante variable.index('valor')"
    print "EJEMPLO EN LISTA:"
    print " creo lista nombres=['juan','pepe','kiko','jose']"
    print "typea nombres.index('pepe')"
    nombres=['juan','pepe','kiko','jose']
    print "esta en la posicion: "+str(nombres.index('pepe'))
    print "EJEMPLO EN TUPLA"
    print " creo tuplas nombres=('juan','pepe','kiko','jose')"
    print "typea nombres.index('kiko')"
    nombres=('juan','pepe','kiko','jose')
    print "esta en la posicion: "+str(nombres.index('kiko'))
    print "Cuando creas que has practicado lo suficiente hazmelo saber con continuar(9)"
print ""
"""SABER CUANTAS VECES APARECE UN ELEMENTO EN UNA LISTA"""
def accion_howmany_list():
    print "SABER CUANTAS VECES APARECE UN ELEMENTO EN UNA LISTA [COUNT]"
    print "Si necesitamos saber cuentos elementos con el mismo valor tenemos podemos usar variable.count('valor') "
    print "cosas=['raton','teclado','monitor','cpu','monitor','raton','raton']"
    print "print (cosas.count('raton'))"
    print "print (cosas.count('monitor'))"
    print "(cosas.acount('teclado'))"
    cosas=['raton','teclado','monitor','cpu','monitor','raton','raton']
    print "El raton aparece "+str(cosas.count('raton'))+" veces"
    print "El monitor aparece "+str(cosas.count('monitor'))+" veces"
    print "el teclado aparece "+str(cosas.count('teclado'))+" vez"
    print "Cuando creas que has practicado lo suficiente hazmelo saber con continuar(10)"
    print ""
def accion_howmany_tuple():
    print "SABER CUANTAS VECES APARECE UN ELEMENTO EN UNA TUPLA [COUNT]"
    print "como te he comentado varias veces lo que aprendas con las tuplas se aplica a las listas asique haz un ejercicio con las tuplas y cuenta el numero de veces que aparecen los elementos dentro de la tupla, puedes usar el ejemplo anterior para ello"
    print "cosas=('raton','teclado','monitor','cpu','monitor','raton','raton')"
    print "print (cosas.acount('raton'))"
    print "print (cosas.acount('monitor'))"
    print "(cosas.acount('teclado'))"
    cosas=('raton','teclado','monitor','cpu','monitor','raton','raton')
    print "El raton aparece "+str(cosas.count('raton'))+" veces"
    print "El monitor aparece "+str(cosas.count('monitor'))+" veces"
    print "el teclado aparece "+str(cosas.count('teclado'))+" veces"
    print "Cuando creas que has practicado lo suficiente hazmelo saber con continuar(11)"
    print ""
def accion_howmany_items():
    print "SABER LA CANTIDAD DE ELEMENTOS DE UNA LISTA/TUPLA [LEN]"
    print "Vamos a declarar varias tuplas y alguna lista con una cantidad diferente de elementos por ejemplo:"
    print "2 tuplas y 1 lista con una cantidad diferente de elementos "
    print "declaramos una tupla para el ejemplo:"
    print "caja=('calcetines','camisetas','calzoncillos')"
    print "armario=('camisas','camisetas','abrigos','pantalon')"
    print "mesita=['lampara','cenicero']"
    print "typea len(caja)"
    print "typea len(mesita"
    print "typea len(armario)"
    caja=('calcetines','camisetas','calzoncillos')
    armario=('camisas','camisetas','abrigos','pantalon')
    mesita=['lampara','cenicero']
    print "elementos de caja :"
    print len(caja)
    print "elementos de mesita :"
    print len(mesita)
    print "elementos de armario"
    print len(armario)
    print "Cuando creas que has practicado lo suficiente hazmelo saber con continuar(12)"
"""CONVERSIONES"""
def conversiones1():
    print "!!CONVERSIONES ENTRE LISTAS TUPLAS Y VICIVERSA !!"
    print "Si tenemos que modificar el contenido de una tupla sabemos que son estaticas y por ello no podemos, lo que si podemos es comvertir una tupla en lista "
    print "para manipularla como una lista y despues convertirla en una tupla"
    print "Pero como de momento solo sabemos consultar cualquier elemento y no manipular esta parte se vera al completo mas adelante:"
    print "***** convertir listas a tuplas *****"
    print "mi_lista=[1,'dos',3,'cuatro']" 
    print "mi_lista_tupla=tuple(mi_lista)"
    mi_lista=[1,'dos',3,'cuatro']
    print str(mi_lista)+" esto es una lista"
    mi_lista_tupla=tuple(mi_lista)
    print str(mi_lista_tupla)+" he volcado el contenido de mi_lista en mi_lista_tupla y tranformandolo en una tupla 'mi_lista_tupla=tuple(mi_lista)' "
    print "tranformo una tupla en una lista"
    print "mi_tupla_lista=list(mi_lista_tupla)"
    mi_tupla_lista=list(mi_lista_tupla)
    print str(mi_tupla_lista)+" he volcado el contenido de mi_lista_tupla(tupla) en mi_tupla_lista(lista) mi_tupla_lista=list(mi_lista_tupla)"
    print "Cuando creas que has practicado lo suficiente hazmelo saber con continuar(13)"
    print ""
    print ""
def resumen_acceso():
    print "============================================================================================================================================================"
    print "============================================================================================================================================================" 
    print "===================================================================ENHORABUENA=============================================================================="
    print "============================================================================================================================================================"

    print "vamos a echar un ojo atras para repasar los conocimientos adquiridos :"
    print "hemos visto las diferencias sintacticas que hay entre una tupla y una lista : "
    print "tupla=(1,2,3,4) la tupla usa parentesis"
    print "lista=[1,2,3,4] la lista va entre-corchetes"
    print "Sabemos que las tuplas son estaticas y las listas dinamicas"
    print "hemos aprendido a declarar tanto tuplas como listas"
    print "acceder a sus elementos por su indice de componente aunque tenga 1 o mas elementos y recoger la informacion como mejor nos convenga[desde:hasta:numero_saltos]"
    print "sabemos como individualizar los elementos multiples y tratarlos de forma indivudual"
    print "sabemos crear tuplas/listas numericas con range"
    print "sabemos como enumerar las listas/tuplas con su numero de indice y valor"
    print "sabemos como obetener el numero de indice por su valor con index"
    print "sabemos como contar cada elemento con count"
    print "y todo esto sirve tanto para listas como para tuplas, como habras observado todas estas operaciones son solo de consulta "
    print "sabemos como obtener el valor de un elemento, el valor de un indice, saber cuantas veces aparace, enumerarlo"
    print "y todas estas opciones coinciden en que ninguna modifica nada en todo caso inicializa como range una variable a un determinado rango de elementos"
    print "y como mucho hacer conversiones entre listas tuplas y viceversa pero el resto nos dara solo informacion que podremos tratar"
    print "Hasta aqui hemos recorrido la cantidad de opciones que manejan las tuplas que de la misma manera es aplicable a las listas"
    print "y apartir de aqui las siguientes cosas que veamos solo podran ser aplicadas a las listas"
    print "TUPALS: continuar(0) /tuplas"
    print "ACCESO A LOS ITEMS POR EL INDICE: continuar(1)"
    print "TUPLAS 1 DIMENSIONES RANGO POR EL INDICE: continuar(2)"
    print "AHORA CON LOS 3 ARGUMENTOS: continuar(4) "
    print "CREAR LISTAS/TUPLAS CON RANGE: continuar(5) "
    print "ENUMERAR EL INDICE[ENUMERATE]: continuar(6) "
    print "ENUMERAR UNA LISTA POR EL INDICE CON [ENUMERATE]: continuar(7) "
    print "OBTENER LA POSICION DEL ELEMENTO POR SU VALOR [INDEX]: continuar(8) "
    print "SABER CUANTAS VECES APARECE UN ELEMENTO EN UNA LISTA [COUNT]: continuar(9) "
    print "SABER CUANTAS VECES APARECE UN ELEMENTO EN UNA TUPLA [COUNT]: continuar(10) "
    print "SABER LA CANTIDAD DE ELEMENTOS DE UNA LISTA/TUPLA [LEN]: continuar(11) "
    print "CONVERSIONES ENTRE LISTAS TUPLAS Y VICIVERSA: continuar(12) "
    print "RESUMEN E INDICE: continuar(13) "
    print "cuando quieras seguir aprendiendo mas sobre las funionalidades extra que diferencia una lista de una tupla hazmelo saber escbribiendo continuar(14)"
"""ORDENADAR LISTAS [SORT]"""
def accion_listas():
    print "LISTAS"
    print "Las listas son un tipo de dato complejo como las tuplas, al igual que estas pueden contener otras tuplas listas o diccionarios"
    print "a las listas al ser modificables tenemos unas cuantas funcionalidades extras que no podemos hacer sobre las tuplas"
    print "Entonces recuerda que lo que aprendas a partir de aqui podria aplicarse sobre todo a las listas y en cierta medida a los diccionarios y de ningun modo sobre las tuplas"
    print "definicion de listas mi_lista =[1,2,3,4]"
    print "Si queremos a la hora de declarar una lista no tenemos porque iniciarla ejemplo mi_lista[] esto en las tuplas no seria posible ya que hay que inicializarlas siempre y definir su contenido"
    print "cuando quieras seguir aprendiendo mas sobre las funionalidades extra que diferencia una lista de una tupla hazmelo saber escbribiendo continuar(15)"
def accion_ordenarn():
    print "ORDENADAR LISTAS NUMERICAS CON [SORT]" 
    print "Si tenemos por alguna razon que ordenar una lista numerica tenemos la opcion variable.sort()"
    print "este metodo nos ordenara la lista numerica de menor a mayor"
    print "EJEMPLO :"
    print " numeros=[43,5,4,67,32]"
    print "print (numeros)"
    print " numeros.sort()"
    print "print (numeros) "
    numeros=[43,5,4,67,32]
    print (numeros)
    numeros.sort()
    print (numeros)
    print "Si quieres despues de hacer la prueba con una lista , haz la prueba con una tupla y veras que nos muestra un error, saca tus propias conclusiones:"
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(16)"
def accion_ordenarl():
    print "ORDENADAR LISTAS DE STRING CON [SORT]" 
    print "Al igual que usamos sort en listas numericas podemos hacerlo en listas de texto o mixtas"
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
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(17)"
"""INVERTIR LISTAS """
def accion_invertir():
    print "INVERTIR LISTAS [REVERSER]"
    print "Acabamos de ver sort que nos ordena las listas alfabeticamente con strings o de < las listas numericas"
    print "con variable.reverse consegimos alterar el estado original de la lista de forma inversa"
    print "ejemplo: lista=(2,1,3)"
    print "lista.reverse"
    print "esta accion nos invierte el contenido de la lista quedando de tal manera : (3,1,2)"
    print "EJERCICIO1: EJEMPLO"
    print "creamos una lista letras=['g','w','x','j','v','a'] "
    print "letras"
    print "letras.reverse()"
    print "letras"
    letras=['g','w','x','j','v','a']
    print (letras)
    letras.reverse()
    print (letras)
    print "EJERCICIO2:EJEMPLO"
    print "como ya conocemos el comando sort y el comando reverse podemos usarlo para ordenar una lista alfabeticamente y con reverse tener la lista ordenada inversamente"
    print "Comprobamos que altera inversamente el contenido del letras si probamos a ordenarlo primero y despues invertirlo"
    print "letras.sort()"
    print "letras.reverse()"
    print "letras"
    letras.sort()
    letras.reverse()
    print (letras)
    print ""
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(18)"


def accion_asigd():
    print "ASIGNACION DE 1 ELEMENTO A LA DERECHA "
    print "Con el metodo [append]:Podemos anadir un item por la derecha de elemento"
    print "EJEMPLO :"
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
    print "EJERCICIO: Practica tu mismo anadiendo elementos a una lista que crees y experimentalo tu mismo, saca tus propias conclusiones"
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(19)"
def accion_asig2():
    print "ASIGNACION DE VARIOS VALORES POR LA DERECHA [EXTEND]"
    print ".append solo nos permite meter items de uno en uno por sentencia"
    print ".extend nos da la misma funcionalidad que append solo que nos permite meter varios valores en una misma sentencia"
    print "EJEMPLO :"
    print "mi_lista1=[1,2,3]" 
    mi_lista1=[1,2,3]
    print "mi_lista1.extend[5,6,7,8,9]"
    mi_lista1.extend([5,6,7,8,9])
    print "mi_lista1"
    print (mi_lista1)
    print "EJERCICIO: crea una lista numerica, de strings, o mixta y anade varios elementos con el metodo .extend para que lo compruebes por ti mismo., saca tus propias conclusiones"
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(20)"

"""INSERTAR ELEMENTOS EN LA POSICION DETERMINADA"""
def accion_insert1():
    print "INSERTAR ELEMENTOS POR SU INDICE CON EL METODO [insert]:"
    print "Creamos una lista para el ejemplo : mi_listab=['a','b','c']"
    mi_listab=['a','b','c']
    print "Le digo que quiero agregar la palabra letras en el indice 0 "
    print "mi_listab.insert(0,'letras')"
    mi_listab.insert(0,'letras')
    print (mi_listab)
    print "Ahora repito el ejercicio pero con numeros defino la misma lista con numeros:"
    print "mi_listab=[1,2,3,5]"
    print "mi_listab.insert(3,'4') coloco el elmento numero 4 en la posicion de indice numero 3 ya que empienza en 0"
    mi_listab = [1,2,3,5]
    mi_listab.insert(3,'4')
    print (mi_listab)
    print "EJERCICIO: crea una lista numerica, de texto o mixta e intenta insertar items en la posicion que quieras para comprobarlo, saca tus propias conclusiones"
    print ""
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(21)"
"""ELIMINAR ELEMENTOS POR SU VALOR ESPECIFICO"""
def accion_elem1():
    print "ELIMINAR ITEMS POR VALOR DEL ITEM CON[remove]"
    print "remove solo admite un argumento en su homologo inverso msa cercano seria append "
    print "creamos una lista numerica"
    print "mi_listab = [1,2,3,5]"
    print "mi_listab.remove(2) borrara el elemento si coincide con el argumento dado en este caso el 2"
    print "typea mi_listab"
    mi_listab = [1,2,3,5]
    mi_listab.remove(2)
    print (mi_listab)
    print "EJERCICIO: Crea una lista y prueba a borrar elementos por su valor,  saca tus propias conclusiones"
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(22)"

"""ELIMINAR ELEMENTOS POR SU POSICION"""
def accion_elem2():
    print "ELIMINAR ITEMS POR SU POSICION DE INDICE[del]"
    print "creamos una lista para el ejemplo mi_listab = [1,2,3,5]"
    print "del mi_listab[3]  la posicion 3 se refiere al indice equilvaldria al elemento con valor 5 "
    mi_listab = [1,2,3,5]
    del mi_listab[3]
    print (mi_listab)
    print "podemos combinar el [del] con la forma de determinar los rangos mi_lista[0:2] del 0 hasta el 2"
    print "del mi_listab[0:2]"
    del mi_listab[0:2]
    print (mi_listab)
    print "EJERCICIO: Te animo a que crees una lista como mas te guste y pruebes  a eliminar primero items de uno en uno"
    print "Y despues repite el ejercicio eliminando items por rango de indice ,  saca tus propias conclusiones"
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(23)"
    print ""
"""ELIMINAR UN ELEMENTO INDICANDO SU POSICION Y OBTENER EL ELEMENTO ELIMINADO"""
def accion_elem3():
    print "ELIMINAR UN ELEMENTO INDICANDO SU POSICION Y OBTENER EL ELEMENTO ELIMINADO[.POP]"
    print "creamos una lista para el ejemplo"
    print "mi_array=['tele','radio','movil','tablet']"
    print "Ahora creo una variable llamada borrado y lo combino con el nombre de la lista + ,pop(y posicion de indice)"
    print "El motivo de la creacion de la variable borrado es porque necesitamos un contenedor para almacenar la informacion del item elinado ya que este metodo nos devuelve dicha informacion"
    print "borrado=mi_array.pop(1)"
    print "print (mi_array)"
    print "print (borrado)"
    mi_array=['tele','radio','movil','tablet']
    borrado=mi_array.pop(1)
    print "a si queda mi_array="+str(mi_array)
    print "a si queda la variable borrado ="+str(borrado)
    print "EJERCICIO: Crea una lista y practica con el ejemplo , y saca tus propias conclusiones:"
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(24)"
"""ELIMINAR TODOS LOS ELEMENTOS"""
def accion_elem4():
    print "ELIMINAR TODOS LOS ELEMENTOS CON LA FUNCION [del]"
    print "del mi_listab[:] esto dejaria la lista totalmente vacia"
    print "Creo una lista para el ejemplo :mi_listab=[9,8,7,6,5,4,3,2,1]"
    mi_listab=[9,8,7,6,5,4,3,2,1]
    print "del mi_listab[:]"
    print "Con esto dejamos la lista totalmente vacia"
    del mi_listab[:]
    print (mi_listab)
    print "Hasta aqui hemos visto todo lo referente al borrado de elementos dentro de las listas "
    print "EJERCICIO: Crea una lista y prueba a dejarla vacia como te muestro en el ejemplo :, y saca tus propias conclusiones "
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(25)"

"""MODIFICAR/SOBRE-ESCRIBIR ELEMENTOS EXISTENTES"""
def acciones_mod_slic_lista():
    print "MODIFICAR ELEMENTOS EXISTENTES en lLISTAS"
    print "creamos una lista de prueba mi_listac=['uno','dos','tr3s']"
    print "mi_listac[0]=1 cambio el item de la posicion indice 0 que es el primer elemento de la lista que es uno por 1"
    mi_listac=['uno','dos','tr3s']
    mi_listac[0]=1
    print (mi_listac)
    print "EJERCICIO: Crea una lista y prueba a modificar su contenido por la posicion de indice, y saca tus propias conclusiones "
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(26)"

"""MODIFICAR VALORES EN CONJUNTO MEDIANTE SLICING"""
def acciones_mod_slic_listas():
    mi_listin = range(20)
    print "MODIFICAR VALORES POR SU RANGO DE INDICE LISTAS"
    print "Creo una lista con range para el ejemplo mi_listin = range(20)"
    print (mi_listin)
    print "Si le indicamos una serie de valores en un determinado rango de indice esta accion nos sobreescribira dichos elementos que coincidan con el indice parametrizado "
    print "EJEMPLO:"
    print "mi_listin[6:9]='seis','sieto','ocho' le estoy indicando que haga la modificacion desde el indice 6 hasta la posicion indice 9"
    print "Para que funcione como esperamos tiene que tener coherencia entre el rango de indices que le damos y la cantidad de datos que queremos modificar"
    mi_listin[6:9]="seis","siete","ocho"
    print (mi_listin)
    print "Aunque si lo que queremos es introducir un determinado patron de modificacion podemos hacer uso del tercer parametro como cuando accediamos a los indices por rango"
    print "ejemplo:"
    print "creo una lista con range por ejemplo. mi_prueba=range(20)"
    mi_prueba=range(20)
    print (mi_prueba)
    mi_prueba[0:21:2]="dato_nuevo1","dato_nuevo2","dato_nuevo3","dato_nuevo4","dato_nuevo5","dato_nuevo6","dato_nuevo7","dato_nuevo8","dato_nuevo9","dato_nuevo10"
    print (mi_prueba)
    print "mi_prueba[0:20:2] con esta sintaxis que ya la conocemos , le estaria diciendo que desde la posicion indice 0 hasta la posicion indice 20 , inserte modificaciones cada 2 indices con los valores que quieras pasarle"
    print "en este caso para que nos funcione correctamente y si en una lista de 20 elementos quiero modificar cada 2 indices nos da un total de 10 que seran los valores que pedira para su correcto funcionamiento"
    print "EJERCICIO: Crea una lista y modifica varios por su rango [desde:hasta] y despues prueba hacerlo con los 3 argumentos [desde:hasta:saltos], y saca tus propias conclusiones"
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(27)"
def acciones_lista_repaso():
    print "============================================================================================================================================================"
    print "============================================================================================================================================================" 
    print "===================================================================ENHORABUENA=============================================================================="
    print "============================================================================================================================================================"
    print "Ya sabes tratar listas , hemos practicado : "
    print "LISTAS continuar (14)"
    print "ORDENADAR LISTAS INT[SORT] - continuar(15)"
    print "ORDENADAR LISTAS DE STRING CON [SORT] continuar(16)"
    print "INVERTIR LISTAS [REVERSER] continuar(17)"
    print "ASIGNACION DE 1 ELEMENTO A LA DERECHA [APPEND] continuar(18)"
    print "ASIGNACION DE VARIOS VALORES POR SU DERECHA [EXTEND] continuar (19)"
    print "ASIGNACION DE ELEMENTOS EN UNA POSICION DETERMINADA [INSERT] continuar(20)"
    print "ELIMINAR ITEMS POR SU PROPIO VALOR [REMOVE] continuar(21)"
    print "ELIMINAR ITEMS POR SU POSICION[DEL] continuar(22"
    print "ELIMINAR ITEMS POR SU POSICION RETORNANDO EL ITEM ELIMINADO[POP]continuar(23)"
    print "ELIMINAR TODOS LOS ELEMENTOS CON LA FUNCION [DEL]continuar(24)"
    print "MODIFICAR ITEMS POR SU POSICION DE INDICE continuar(25)"
    print "MODIFICAR ITEMS POR SU POSICION DE INDICE EN UN RANGO DE INDICES continuar(26)"
    print "RESUMEN LISTAS continuar(27)"
    print "ASOCIAR OBJETOS A ELEMENTOS DE UNA LISTA/TUPLA continuar(28)"
    print "ASOCIAR OBJETOS A ELEMENTOS DE UNA LISTA/TUPLA POR INDICE DE RANGO continuar(29)"
    
"""DESEMPAQUETAMIENTO O UNPACKING"""
def unpack():
    print "RELACIONAR OBJETOS CON ITEMS DE UNA LISTA / TUPLA"
    print "Podemos tener una serie de objetos(variables en este caso) y relacionar estos con los items de una lista"
    print "Ejemplo:"
    print "Creamos una tupla con 4 items mis_datos=('Raul','Abejon','30','soltero)"
    print "y creo 4 varibles y los inicializo con la lista de la siguiente manera "
    print "nombre, apellido, edad,estado=mis_datos"
    mis_datos=('Raul','Abejon','30','soltero')
    nombre, apellido, edad, estado=mis_datos
    print "Ahora al llamar al objeto me deberia mostrar el item asociado a la tupla"
    print (nombre)
    print (apellido)
    print (edad)
    print (estado)
    print "Para que sea efectivo el numero de valores ha de coincidir con el numero de objetos"
    print "Si la lista o tupla continue n numeros de items la cantidad de objetos a relacionar deben coincidir en n numero de objetos"
    print "Enumero los elementos de la tupla para comprobar que pese a estar asociado un item a un objeto sigue manteniendo la coherencia de sus indices:"
    mis_datos=tuple(enumerate(mis_datos))
    print (mis_datos)
    print ""
    for i in mis_datos:
        print (i)
    print "EJERCICIO:"
    print "Primero recrea este ejemplo para que veas el error que nos muestra por pantalla:"
    print "tupla=('pepe','coche','casa')"
    print "nombre,posesion1=tupla"
    print "Como puedes comprar si hacemos eso nos devuelve un error diciendo que no coinciden los argumentos con los objetos:"
    print "Ahora crea una tupla o lista y asociala unos objetos y depues typea el nombre de dichos objetos"
    print "haz la prueba guiandote en los ejemplos mostrados, para que saques tu propia conclusion"
    print "Cuando creas que has practicado los suficiente hazmelo saber escribiendo continuar(29)"
def unpack2():
    print "RELACIONAR OBJETOS CON ITEMS DE UNA LISTA / TUPLA POR INDICE DE RANGO"
    print "tambien podemos relacionar un determinado numero de items con objetos por su rango de indice:"
    print "mis_datos2=('rul','tecnico','si','no')"
    print "estudia, trabaja =mis_datos2[2:] relaciono los objetos desde el elemento 2 siendo los 2 ultimos en el ejemplo"
    print "de esta manera podriamos saltar la restriccion del primer ejemplo donde teniamos que asignar n numeros de items y que coincidiera con un n nuemro de objetos"
    mis_datos2=('rul','tecnico','si','no')
    estudia, trabaja = mis_datos2[2:]
    print (mis_datos2)
    print "estudia, trabaja =mis_datos2[:2] relacion los objetos hasta el elemento 2 sin incluirlo siendo los 2 primeros en el ejemplo"
    nombre, titulo = mis_datos2[:2]
    print (mis_datos2)
    print "Ejercicio:"
    print "Prueba a crear una lista y a relacionar un par de objetos a un determinado rango de items por su indice, puedes recrear el ejemplo mostrado para expertimentarlo de propia mano"
    print "Cuando creas que has practicado los suficiente hazmelo saber escribiendo continuar(30)"
"""ZIP"""
def zips():
    print "[ZIP]"
    print "Parecido a UNPACKING nos permite relacionar los items por indice entre listas Me explico"
    print "creo 2 listas cabecera y dtos"
    print "cabecera = ['name','email','login'] "
    print "dtos = ['raul','drohne@gmail.com','drohne@gmail.com']"
    print "Creo union y la defino de la siguiente manera con [ZIP] y las 2 listas creadas" 
    print "union = zip(cabecera,dtos)"
    cabecera = ['name','email','login']
    dtos = ['raul','drohne@gmail.com','drohne@gmail.com']
    union = zip(cabecera,dtos)
    print "y su resultado es tal cual te lo muestro:"
    print (union)
    print ""
    print "print 'printeo con un for' "
    print "for cabecera, dtos in union: "
    print "     print (str(cabecera)+' :'+str(dtos))"
    print "printeo con un for"
    for cabecera, dtos in union:
        print (str(cabecera)+" : "+str(dtos))
    print "Cuando creas que has practicado los suficiente hazmelo saber escribiendo continuar(31)"
print ""
    
"""SETS"""
def sets():
    print "[SET]"
    print "es un conjunto de valores que no se pueden acceder desde el indice y no puede tener valores repetidos"
    print "Creo una lista con 6 items alguno de ellos son del mismo valor :"
    print "utensilios = ['tenedor','cuchillo','cuchara','cuchara','cuchillo','tenedor']"
    print "print (utensilios)"
    utensilios = ['tenedor','cuchillo','cuchara','cuchara','cuchillo','tenedor']
    print (utensilios)
    print "Pasamos utensilios por set de la siguiente manera:"
    print "utensilios = set(utensilios)"
    print "print (utensilios)"
    utensilios = set(utensilios)
    print (utensilios)
    print "Repetimos la operacion con tuplas"
    print "Ejercicio: Repite los ejemplos, o crea una lista/tupla con items repetidos y usa set para comprobar como se comporta"
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(32)"
    print ""
def sets2():
    print "AnADIR ELEMENTOS en [set.add()]"
    print "para el ejemplo usamos el mismo ejemplo utensilios = ['tenedor','cuchillo','cuchara','cuchara','cuchillo','tenedor']"
    print "Eliminamos los items repetidos:"
    print "utensilios = set(utensilios) "
    utensilios = ['tenedor','cuchillo','cuchara','cuchara','cuchillo','tenedor']
    print (utensilios)
    print "utensilios.add('hola') "
    utensilios.add('hola')
    print (utensilios)
    print "utensilios.add(1) "
    utensilios.add(1)
    print (utensilios)
    print "utensilios.add('asd') "
    utensilios.add('asd')
    print (utensilios)
    print "comprobamos que al anadir un elemento lo deja sin orden aparante"
    print "Practica un poco emulando el ejemplo mostrado"
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(33)"
    print " "
def sets3():
    print "ELIMINAR ELEMENTOS  en [set.remove()]"
    print "Seguimos con la misma lista de estos ejemplos con el mismo contenido :"
    print "utensilios = ['tenedor','cuchillo','cuchara','cuchara','cuchillo','tenedor']"
    utensilios = ['tenedor','cuchillo','cuchara','cuchara','cuchillo','tenedor']
    print "Le pasamos el set para eliminar items duplicados"
    print "utensilios=set(utensilios)"
    utensilios=set(utensilios)
    print (utensilios)
    print "Ahora elimina un item por su propio valor cuchara en caso de que coincida"
    print "utensilios.remove('cuchara') "
    utensilios.remove('cuchara')
    print (utensilios)
    print "Ahora elimina un item por su propio valor cuchillo en caso de que coincida"
    print "utensilios.remove('cuchillo') "
    utensilios.remove('cuchillo')
    print (utensilios)
    print "Ahora elimina un item por su propio valor tenedor en caso de que coincida"
    print "utensilios.remove('tenedor') "
    utensilios.remove('tenedor')
    print (utensilios)
    print "Recrea el ejemplo por ti mismo para que lo experimentes de tu propia mano"
    print "Cuando creas que has practicado lo suficiente hazmelo saber escribiendo continuar(34)"
def sets4():
    print "BUSCAR ELEMENTOS  IN[set]"
    print "Si necesitamos saber si tenemos cierto valor o no lo tenemos en una lista/tupla podemos hacerlos de la siguiente manera:"
    print "Seguimos con la lista usada en estos ultimos ejemplos:"
    print "defino de la siguiente manera utensilios = ['tenedor','cuchillo','cuchara','cuchara','cuchillo','tenedor']"
    utensilios = ['tenedor','cuchillo','cuchara','cuchara','cuchillo','tenedor']
    print (utensilios)
    print "'asd' in utensilios"
    print "Estamos preguntado si asd esta dentro del objeto utensilios en casi verdadero devolvera True en caso contrario devolvera False"
    print 'asd' in utensilios
    print "tambien podemos usar not in para preguntarle justamete lo contrario"
    print "'lapiz' not in utensilios"
    print "En caso de que no este lapiz en utensilios devolera un True de lo contrario devolvera False"
    print 'lapiz' not in utensilios
    print "Realiza unas pruebas para comprobarlo por ti mismo."
    print ""
print "============================================================================================="
print "                    TUTORIAL PYTHON SOBRE TUPLAS LISTAS Y DICCIONARIOS"
print "=============================================================================================="
print "                               (TUPLAS) [LISTAS] Y {DICCIONARIOS}"
print "Son tipos de datos como los arrays pero con particularidades que iremos explicando de forma detallada."
print "Los tipos de datos que pueden albergar pueden ser de cualquier tipo: int,boolean,string,objetos, listas,tuplas,diccionarios "
print "Para empezar con el tutorial escribe el tipo de dato por el cual quieres investigar, las opciones son: tuplas,listas o diccionarios"
print "Mi recomendacion esque empieces por las tuplas, continues con las listas y terminas con los diccionarios"
print "Por donde vas a empezar ?? typea tuplas, listas o indice "
nombre = raw_input()
print nombre
if nombre == 'tuplas' :
    tuplas()
if nombre == 'listas' :
    accion_listas()
if nombre == 'indice':
    indice()
