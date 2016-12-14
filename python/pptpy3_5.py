#Juego: Piedra, Papel o tijera creado por drohne 2016 
import random
import time
def jugarDeNuevo():
    otra= "s"
    while otra == "s":
         
        print('quieres jugar de nuevo?? s(si) /n (no)' )
        otra= input()
        eleccion(otra)
        
def eleccion(s):
    if opcionJ == "s":

        print('Piensa y elige tu jugada')
        print('Para elegir piedra pulsa 1')
        print('Para elegir papel pulsa 2')
        print('Para elegir tijera pulsa 3')
        numeroJ=input()
        print('Muy bien pues vamos haya vamos !!!...')
        time.sleep(2)
        print('...Piedra...')
        time.sleep(2)
        print('...Papel... y ...')
        time.sleep(2)
        print('..tijera...!!!')
        time.sleep(1)
        numeroM = random.randint(1, 3)
        reglas(numeroJ,numeroM)
        

            
    else :
        print('Vale'+ NomJugon + 'en otra ocasion entonces !!')
        
def reglas(numeroJ,numeroM):
    
    if str(numeroJ) == "1" and str(numeroM) == "3" :
        numeroJ_T= "piedra" 
        print(nombreJ + ' Gana !!!' + ' con ' + numeroJ_T)
              
    elif str(numeroJ) == "2" and str(numeroM) == "1" :
        numeroJ_T= "papel"
        print(nombreJ + ' Gana !!!' + ' con ' + numeroJ_T)
                 
    elif str(numeroJ) == "3" and str(numeroM) == "2" :
        numeroM_T="tijera"
        print(nombreJ + ' Gana !!!' + ' con ' + numeroJ_T)       
    
    elif str(numeroJ) == "1" and  str(numeroM) == "1" :
         numeroM_T="piedra"
         print(nombreJ + ' y ' + nombreM + ' empatan con ' + numeroM_T)
        
    elif str(numeroJ) == "2" and  str(numeroM) == "2" :
         numeroM_T="papel"
         print(nombreJ + ' y ' + nombreM + ' empatan con ' + numeroM_T)
        
    elif  str(numeroJ) == "3" and  str(numeroM) == "3" :
         numeroM_T="tijera"
         print(nombreJ + ' y ' + nombreM + ' empatan con ' + numeroM_T)
        
    else  :
        numeroM_T="tijera"
        print(nombreM + ' Gana con ' + numeroM_T )
    jugarDeNuevo()


nombreM= "drohne"
print('Hola, cual es tu nombre?')
nombreJ= input() 
print('un placer ' + nombreJ + ' mi nombre es ' + nombreM + ',¿ Te apetece jugar a piedra, papel o tijera ? s(si) /n (no)')
opcionJ= input()
eleccion(opcionJ)
jugarDeNuevo()


