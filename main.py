#CREDITS to Lyriax
#22 January 2021
#3rd party use allowed!

import random

rangeSelect = 100
rangeSelect = input("Spiegeln und ergänzen mit 100 oder 1000 spielen [100/1000]: (BISHER NUR 100 MÖGLICH!)")
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
        print("Du bist dumm!")
        x = input("Spiegel die Zahl " + str(y) + ": ")
    
    print("Richtig!")
    y = x
    
    x = input("Ergänze " + str(y) + " auf 100: ")

    while int(x) != 100 - int(y):    
      if int(x) != 100 - int(y):
        print("Du bist dumm!")
        x = input("Ergänze " + str(y) + " auf 100: ")
    
    print("Richtig!")
    y = int(x)