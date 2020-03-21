#Librerias
import sys
from clear_screen import clear
from termcolor import colored, cprint

#Variables globales
jugadores = []

#Class definitions
class Jugador:
  def __init__(self, nombre):
      self.nombre = nombre
      self.puntaje = 0
      self.puntajeAnterior = 0

  def get_nombre(self):
    return self.nombre

  def get_puntaje(self):
    return self.puntaje

  def sumarPuntaje(self, ingreso):
    self.puntaje += int(ingreso) 

  def guardarPuntajeAnterior(self):
      self.puntajeAnterior += self.puntaje


def correcionActivada():
    global jugadorActual

    print ("CORRECIÓN ACTIVADA")
    jugadorActual -= 1    
    jugadores[jugadorActual].puntaje = jugadores[jugadorActual].puntajeAnterior
    _correccionActivada == True

def validarIngreso(ingreso):
  global jugadorActual
  global _correccionActivada

  while _correccionActivada == True:
      if not ingreso.isnumeric():
        print("La corrección se encuentra activada, por favor ingrese un puntaje para finalizarla")
        print("")
      else:
        _correccionActivada == False

  if str(ingreso) == "m":
    correcionActivada()
    return False

  if not ingreso.isnumeric():
    print("Caracter Inválido")
    print("")
    return False

  if int(ingreso) % 50 != 0:
    print("El valor no es multiplo de 50, se activo la correción automática")
    correcionActivada()
    return False

  if int(ingreso) < 0:
    print("Caracter Inválido")    
    return False

  return True

def guardarValor(ingreso):
    
  jugadores[jugadorActual].guardarPuntajeAnterior()

  #Verifico que haya iniciado e ingreso valor
  if int(ingreso) >= 750 or jugadores[jugadorActual].puntaje != 0:    
    jugadores[jugadorActual].sumarPuntaje(int(ingreso))

def imprimirTabla(maxPlayerNameLenght):

  jcount = 0
  color = "green"

  jugadoresCopyForTable = jugadores
  jugadoresCopyForTable = sorted(jugadores, key=lambda x: x.puntaje, reverse=True)
  puntajeJugadorAnterior = jugadoresCopyForTable[jcount].get_puntaje()

  while jcount < len(jugadoresCopyForTable):

    spaceToAdd = ""
    jugNamelen = len(jugadoresCopyForTable[jcount].get_nombre())
    if jugNamelen < maxPlayerNameLenght:
        spaceToAdd = " " * (maxPlayerNameLenght - jugNamelen)

    puntJugNameLen = len(str(jugadoresCopyForTable[jcount].get_puntaje()))

    stringLine = jugadoresCopyForTable[jcount].get_nombre() + spaceToAdd 
    stringLine += " : | " 
    stringLine += "0" * (4 - puntJugNameLen)
    stringLine += str(jugadoresCopyForTable[jcount].get_puntaje()) 
    stringLine += " | " 
    stringLine += str(puntajeJugadorAnterior - int(jugadoresCopyForTable[jcount].get_puntaje()))

    cprint (stringLine, color)
    
    if jcount == 0:
      color = "yellow"
    else:
      color = "white"

    puntajeJugadorAnterior = int(jugadoresCopyForTable[jcount].get_puntaje())
    jcount += 1

  print ("")

def CrearJugadores():

  maxPlayerNameLenght = 0

  cantJug = input("Cantidad jugadores: ")

  if not cantJug.isnumeric():
    cprint("Caracter Inválido", "yellow")
    CrearJugadores()

  i = 0
  while i < int(cantJug):
    name = input("Nombre: ")    

    if len(name) > maxPlayerNameLenght:
        maxPlayerNameLenght = len(name)

    jugadores.append(Jugador(name))
    i += 1
    
  clear()
  return maxPlayerNameLenght
    
def isNaN(num):
    return num != num


# ------------- Programa -------------------
  
_correccionActivada = False
jugadorActual = 0
maxPlayerLenght = CrearJugadores()

while True:

    ingreso = input("Puntaje que sacó: " + str(jugadores[jugadorActual].get_nombre()) + " ")

    if str(ingreso) == "":
        print("El jugador no ha sumado puntos")
        ingreso = 0

    if ingreso != 0 and not validarIngreso(ingreso):
        continue

    #Verificar victoria
    if jugadores[jugadorActual].puntaje + int(ingreso) == 10000:
        text = colored("FELICIDADES, " + str(jugadores[jugadorActual].get_nombre()) + "! Has ganado :D", 'red', attrs=['reverse', 'blink'])
        print(text)
        break;
  
    if jugadores[jugadorActual].puntaje + int(ingreso) > 10000:
        cprint("Estuviste muy cerca, " + str(jugadores[jugadorActual].get_nombre()) + ", Pero te pasaste D:",'yellow')
    else:
        guardarValor(ingreso)

    #Continuo el ciclo con el jugador siguiente
    if jugadorActual >= len(jugadores) - 1:
        jugadorActual = 0
        clear()
        imprimirTabla(maxPlayerLenght)
    else:
        jugadorActual += 1




  





  





