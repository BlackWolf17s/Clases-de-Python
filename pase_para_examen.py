# -*- coding: utf-8 -*-
"""Pase_para_examen.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QMFKzKkYCL2QjQebVcbFkfUpsOgcnzXX
"""

#Le pregunta a los jugadores que quieren
jugador_1 = int (input('Jugador uno, (1) Piedra, (2) Papel, (3) Tijera, (4) Lagarto, (5) Spock '))
jugador_2 = int (input('Jugador dos, (1) Piedra, (2) Papel, (3) Tijera, (4) Lagarto, (5) Spock '))

#Analiza las opciones si el jugador uno elige Piedra.
if jugador_1 == 1 and jugador_2 == 1:
  print('\nEmpate')
if jugador_1 == 1 and jugador_2 == 2:
  print('\nPapel envuelve Piedra')
  print('\nJugador 2 gana')
if jugador_1 == 1 and jugador_2 == 3:
  print('\nPiedra rompe Tijeras')
  print('\nJugador 1 gana')
if jugador_1 == 1 and jugador_2 == 4:
  print('\nPiedra aplasta Lagarto')
  print('\nJugador 1 gana')
if jugador_1 == 1 and jugador_2 == 5:
  print('\nSpock vaporiza Piedra')
  print('\nJugador 2 gana')

#Analiza las opciones si el jugador uno elige Papel.
if jugador_1 == 2 and jugador_2 == 1:
  print('\nPapel envuelve Piedra')
  print('\nJugador 1 gana')
if jugador_1 == 2 and jugador_2 == 2:
  print('\nEmpate')
if jugador_1 == 2 and jugador_2 == 3:
  print('\nTijera corta Papel')
  print('\nJugador 2 gana')
if jugador_1 == 2 and jugador_2 == 4:
  print('\nLagarto devora Papel')
  print('\nJugador 2 gana')
if jugador_1 == 2 and jugador_2 == 5:
  print('\nPapel desautoriza Spock')
  print('\nJugador 1 gana')

#Analiza las opciones si el jugador uno elige Tijeras.
if jugador_1 == 3 and jugador_2 == 1:
  print('\nPiedra rompe Tijeras')
  print('\nJugador 2 gana')
if jugador_1 == 3 and jugador_2 == 2:
  print('\nTijeras corta Papel')
  print('\nJugador 1 gana')
if jugador_1 == 3 and jugador_2 == 3:
  print('\nEmpate')
if jugador_1 == 3 and jugador_2 == 4:
  print('\nTijeras decapita Lagarto')
  print('\nJugador 1 gana')
if jugador_1 == 3 and jugador_2 == 5:
  print('\nSpock rompe Tijeras')  
  print('\nJugador 2 gana')

#Analiza las opciones si el jugador uno elige Lagarto.
if jugador_1 == 4 and jugador_2 == 1:
  print('\nPiedra aplasta Lagarto')
  print('\nJugador 2 gana')
if jugador_1 == 4 and jugador_2 == 2:
  print('\nLagarto devora Papel')
  print('\nJugador 1 gana')
if jugador_1 == 4 and jugador_2 == 3:
  print('\nTijeras decapita Lagarto')
  print('\nJugador 2 gana')
if jugador_1 == 4 and jugador_2 == 4:
  print('\nEmpate')
if jugador_1 == 4 and jugador_2 == 5:
  print('\nLagarto envenena Spock')
  print('\nJugador 1 gana')

#Analiza las opciones si el jugador uno elige Spock.
if jugador_1 == 5 and jugador_2 == 1:
  print('\nSpock vaporiza Piedra')
  print('\nJugador 1 gana')
if jugador_1 == 5 and jugador_2 == 2:
  print('\nPapel desautoriza Spock')
  print('\nJugador 2 gana')
if jugador_1 == 5 and jugador_2 == 3:
  print('\nSpock rompe Tijeras')
  print('\nJugador 1 gana')
if jugador_1 == 5 and jugador_2 == 4:
  print('\nLagarto envenena Spock')
  print('\nJugador 2 gana')
if jugador_1 == 5 and jugador_2 == 5:
  print('\nEmpate')