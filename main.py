#CREDITS to Lyriax
#22 January 2021
#3rd party use allowed!

import random

#Auswahl zwischen Spielen zwischen 100 und 1000
rangeSelect = input("Spiegeln und ergänzen mit 100, 1000 oder 1000 spielen [100/1000/10000]: ")
if not(rangeSelect == "100" or rangeSelect == "1000"):
  print("Falsche Zahl eingegeben")
if rangeSelect == "100":
  startingnumber = random.randint(1,99)
  playing = True


  if len(str(startingnumber)) == 1:
    startingnumber = "0"+str(startingnumber)

  y = startingnumber

  while playing == True:
    x = input("Spiegel die Zahl " + str(y) + ": ")
    while int(x) != int(str(y)[::-1]):
      if int(x) != int(str(y)[::-1]):
        print("Probier es nochmal!")
        x = input("Spiegel die Zahl " + str(y) + ": ")
    
    print("Richtig!")
    y = x
    
    x = input("Ergänze " + str(y) + " auf 100: ")

    while int(x) != 100 - int(y):    
      if int(x) != 100 - int(y):
        print("Probier es nochmal!")
        x = input("Ergänze " + str(y) + " auf 100: ")
    
    print("Richtig!")
    y = int(x)

if rangeSelect == "1000":
  startingnumber = random.randint(1,999)
  playing = True


  if len(str(startingnumber)) == 2:
    startingnumber = "0"+str(startingnumber)

  y = startingnumber

  while playing == True:
    x = input("Spiegel die Zahl " + str(y) + ": ")
    while int(x) != int(str(y)[::-1]):
      if int(x) != int(str(y)[::-1]):
        print("Probier es nochmal!")
        x = input("Spiegel die Zahl " + str(y) + ": ")
    
    print("Richtig!")
    y = x
    
    x = input("Ergänze " + str(y) + " auf 1000: ")

    while int(x) != 1000 - int(y):    
      if int(x) != 1000 - int(y):
        print("Probier es nochmal!")
        x = input("Ergänze " + str(y) + " auf 1000: ")
    
    print("Richtig!")
    y = int(x)

if rangeSelect == "10000":
  startingnumber = random.randint(1,9999)
  playing = True


  if len(str(startingnumber)) == 3:
    startingnumber = "0"+str(startingnumber)

  y = startingnumber

  while playing == True:
    x = input("Spiegel die Zahl " + str(y) + ": ")
    while int(x) != int(str(y)[::-1]):
      if int(x) != int(str(y)[::-1]):
        print("Probier es nochmal!")
        x = input("Spiegel die Zahl " + str(y) + ": ")
    
    print("Richtig!")
    y = x
    
    x = input("Ergänze " + str(y) + " auf 10000: ")

    while int(x) != 10000 - int(y):    
      if int(x) != 10000 - int(y):
        print("Probier es nochmal!")
        x = input("Ergänze " + str(y) + " auf 10000: ")
    
    print("Richtig!")
    y = int(x)