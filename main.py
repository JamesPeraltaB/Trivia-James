
iniciar_trivia=True
#iniciamos la variable en True
intentos=0

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'



import random
import time

puntaje = random.randint(0, 11)

print(RED+"Estas preparado para el cuestionario que decidira tu futuro")
print("Seras puesto a prueba y juzgado por ello, empecemos!"+RESET)
print(GREEN+"Comenzaras con",puntaje,"puntos"+RESET)

while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  puntaje = 0

  print(CYAN+"\nIntento número:", intentos)
  input("Presiona Enter para continuar"+RESET)

  nombre=input(BLUE+"Ingresa tu nombre, hijo de Adam: "+RESET)

  print(CYAN+"\n Bienvenido/a",nombre, "por tus pecados has caido en esta tierra, y ahora tendrás que probar que eres digno/a de volver de donde se te fue expulsado, responde con cautela, escribe la letra correcta y presiona 'Enter' para enviar tu respuesta: \n"+RESET)

  print(YELLOW+"I. ¿Cuál es la ley de formalización y promoción de la pequeña mineria y mineria artesanal? "+RESET)
  print("a) 27651")
  print("b) 27015")
  print("c) 27506")
  print("d) 26783")

  respuesta_1=input(MAGENTA+"\nTu respuesta: "+RESET).lower()

  while respuesta_1 not in ("a","b","c","d","Genesis"):
    respuesta_1 = input(BLUE+"Solo se te está permitido responder a, b, c o d. Ten cuidado con lo que eliges, elige de nuevo: "+RESET).lower()
    
  if respuesta_1 =="Genesis":
    puntaje+=1000
    print(RED+"Conoces la llave del origen de todo, eh?"+RESET)

  
  if respuesta_1 =="b":
    puntaje-=10
    print(RED+"Incorrecto!",nombre, "debes leer un poco más")
  elif respuesta_1 =="c":
    puntaje-=9
    print("Correc....Incorrecto",nombre,"no llegaras muy lejos asi")
  elif respuesta_1 =="d":
    puntaje-=8
    print("Incorrecto!",nombre, "el camino de la salvación se aleja de ti, hijo de Adam"+RESET)
  else:
    puntaje+=1
    print(BLUE+"Lo has hecho bien, por ahora,",nombre,"\n"+RESET)
  if puntaje == 1:
    print(GREEN+"Tienes",puntaje,"punto\n"+RESET)
  else:
    print(GREEN+"Tienes",puntaje,"puntos\n"+RESET)

  time.sleep(3)

  print(YELLOW+"II. ¿Cuál es la ley de concesiones mineras en zonas urbanas y de expansión urbana? "+RESET)
  print("a) 27651")
  print("b) 27015")
  print("c) 27506")
  print("d) 26783")

  respuesta_2=input(MAGENTA+"\nTu respuesta: "+RESET).lower()

  while respuesta_2 not in ("a","b","c","d","Apocalipsis"):
    respuesta_2 = input(BLUE+"Solo se te está permitido responder a, b, c o d. No eres muy precavido, cierto? elige de nuevo: "+RESET).lower()

  if respuesta_2 =="Apocalipsis":
    puntaje+=1000
    print("Entiendes los mensajes del fin, o todo son mentiras...")

  if respuesta_2 =="a":
    puntaje-=10
    print(RED+"Incorrecto!",nombre, "debes leer un poco más")
  elif respuesta_2 =="c":
    puntaje-=10
    print("Correc....Incorrecto",nombre,"no llegaras muy lejos asi")
  elif respuesta_2 =="d":
    puntaje-=10
    print("Incorrecto!",nombre, "el camino de la salvación se aleja de ti, hijo de Adam"+RESET)
  else:
    puntaje+=1
    print(BLUE+"Lo has hecho bien, por ahora,",nombre,"\n"+RESET)

  if puntaje == 1:
    print(GREEN+"Tienes",puntaje,"punto\n"+RESET)
  else:
    print(GREEN+"Tienes",puntaje,"puntos\n"+RESET)

  time.sleep(3)
  
  print(YELLOW+"III. ¿Cuál es la ley del canon? "+RESET)
  print("a) 27651")
  print("b) 27015")
  print("c) 27506")
  print("d) 26783")

  respuesta_3=input(MAGENTA+"\nTu respuesta: "+RESET).lower()

  while respuesta_3 not in ("a","b","c","d","Quita los 7 sellos"):
    respuesta_3 = input(BLUE+"Solo se te está permitido responder a, b, c o d. Ya deberías saber lo que sucede. Elige de nuevo: "+RESET)

  if respuesta_3 =="Quita los 7 sellos":
    puntaje+=1000
    print("Ya fueron quitados, hace mucho, todos estan sentenciados")

  if respuesta_3 =="a":
    print(RED+"Incorrecto!",nombre, "debes leer un poco más")
    puntaje =puntaje/2
  
  elif respuesta_3 =="b":
    print("Correc....Incorrecto",nombre,"no llegaras muy lejos asi")
    puntaje= puntaje -100

  elif respuesta_3 =="d":
    print("Incorrecto!",nombre, "el camino de la salvación se aleja de ti, hijo de Adam"+RESET)
    puntaje =puntaje -50
  else:
    puntaje+=1
    print(BLUE+"Entiendes que es lo que está pasando verdad?,",nombre,"\n"+RESET)

  time.sleep(3)

  if puntaje <=0:
    print(RED+"Tu alma sera tomada", nombre,"tienes",puntaje,"puntos"+RESET)
  else:
    print(GREEN+"Felicidades",nombre,"tienes",puntaje, "puntos, pero no te serviran de nada para el fin de todo"+RESET)


  print(RED+"\n¿Deseas intentar salvar la humanidad nuevamente?")
  repetir_trivia = input(RED+"Ingresa 'si' para repetir, o cualquier tecla para rendirte: "+RESET).lower()

  if repetir_trivia != "si":  # != significa "distinto"
   print(GREEN+"\nEspero",nombre, "que hayas entendido el mensaje, nos veremos cuando seamos uno solo!"+RESET)
   iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.

lista1=[respuesta_1,respuesta_2,respuesta_3]
print(MAGENTA+"Tus respuestas fueron",lista1)
print(MAGENTA+"\nLas respuestas son: "+RESET)
preguntas=(RED+"de formalizacion y promocion de la pequeña mineria y mineria artesanal","de concesiones mineras en zonas urbanas y de expansion urbana","del canon")
respuestas=("27651","27015","27506")
for number in range(0,3):
  print(RED+"La Ley ",preguntas[number],"es la numero",respuestas[number]+RESET)
input(YELLOW+"Presiona Enter para continuar"+RESET)