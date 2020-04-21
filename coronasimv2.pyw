
import tkinter as tk
from tkinter import *
import webbrowser

import time
from random import choices
#import psutil
import os
import gc
#optimization 
clear = lambda: os.system('clear')  
#varibles
population = 0
infected = 0
houses = 10
nextfam = 10
nextfam2 = 10
numberholder = 1
numinfam = "[1]"
day = 1
atrisk = 0
atriskchance = .124 
dead = 0
mr = 3.4
endpop = 0
#https://www.infoplease.com/us/comprehensive-census-data-state/demographic-statistics-342
#booleansy
done = False
popdone = False
#population arrays
family = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
infect = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
peepinfam = [1, 2, 3, 4, 5]
chance = [0.05, 0.35, 0.3, 0.2, 0.1]
#transmission arrays, second value is infect chance
air = [0, 1]
airchance = [0.8, 0.2]
touch = [0, 1]
touchchance = [0.8, 0.2]
addfac = 0.03
#Visulization Variables
TGREEN =  '\033[32m' # Green Text
TRED =  '\033[31m' # Green Text
TWHITE = '\033[37m'

def infect():
  global done
  global nextfam
  global addfac
  global day
  if nextfam == 10:
    
    done = True;
    
  airchance[1] += addfac
  touchchance[1] += addfac                                            
  #infected + nextfam -----------------------------------
  nextfam = nextfam2 + 1
  day += 1
  print(TRED + "An infection has occured!")
  if done == False:
   time.sleep(1)
   print("")
   print("Running transmit again...")
   transmit()
  if done == True:
    clear()
    deathscan()

def popcalc():
  global population
  global numinfam 
  global numberholder
  global popdone
  
 
  numberholder = str(family[0])[1:-1] + str(family[1])[1:-1] + str(family[2])[1:-1] + str(family[3])[1:-1] + str(family[4])[1:-1] + str(family[5])[1:-1] + str(family[6])[1:-1] + str(family[7])[1:-1] + str(family[8])[1:-1] + str(family[9])[1:-1]
  numb = 0
  newnumb = 0
  for x in range(0, 10):
    
    numinfam = numberholder[numb]
    newnumb = int(numinfam)
    population = population + newnumb
    
    
    
    numb += 1
  print("Population: ", population)
  popdone = True



def noevent():
  global day
  
  day += 1
  print(TGREEN + "No infections occured")
  time.sleep(1)
  print("Running transmit() again...")
  transmit()
  if done == True:
    clear()
    deathscan()


def deathscan():
  global population
  global endpop
  global mr
  global atrisk
  global dead
  print("Running Deathscan() and at risk estimates")
  #at risk
  x = population / 100 
  y = x*12
  
  #death
  z = x*mr
  dead = round(z,0)
  #remaining population
  endpop = round(population - dead, 0)
  time.sleep(1)
  atrisk = round(y, 0)
  
  print(TWHITE + "Done, loading End Certificate")
  time.sleep(1)
  EndCertif()

def EndCertif():
  global population
  global endpop
  global mr
  global atrisk
  global dead
  time.sleep(1)
  clear()
  print("End Certificate (stats):")
  print("Starting Population: ", population)
  print("Deaths: ", dead)
  print("End Population: ", endpop)
  print("Days (duration of sim): ", day)
  print("Member of Population at risk: ", atrisk)
  print("--------------------")
  #print("Utilizing ", psutil.cpu_percent(), "% of CPU power" )
  #print('Memory precentage used:', psutil.virtual_memory()[2])
 
  time.sleep(2)
  exit()
#-----------------------------
def transmit():
  global done
  if done == False:
    day + 1
    #airborne factor
    airsim = choices(air, airchance)
    if airsim == [1]:
      infect()
    else:
      print(airsim)
      noevent()  
    
    #touchy factor
    #touchsim = choices(touch, touchchance)
    #if touchsim == 1:
      #infect()
    #else:
      #noevent()

def simset():
  
  time.sleep(1)
  print("Setting Family(s)")
 #set people in family
  family[0], family[1], family[2], family[3], family[4], family[5], family[6], family[7], family[8], family[9] = choices(peepinfam, chance), choices(peepinfam, chance), choices(peepinfam, chance), choices(peepinfam, chance), choices(peepinfam, chance), choices(peepinfam, chance), choices(peepinfam, chance), choices(peepinfam, chance), choices(peepinfam, chance), choices(peepinfam, chance)
  
    
  
  time.sleep(1)
  popcalc()
  stats = input("Would you like to see individual family populations? (y/n)")
  if stats == "y":
   print("Family[0]:", family[0])
   time.sleep(0.5)
   print("Family[1]:", family[1])
   time.sleep(0.5)
   print("Family[2]:", family[2])
   time.sleep(0.5)
   print("Family[3]:", family[3])
   time.sleep(0.5)
   print("Family[4]:", family[4])
   time.sleep(0.5)
   print("Family[5]:", family[5])
   time.sleep(0.5)
   print("Family[6]:", family[6])
   time.sleep(0.5)
   print("Family[7]:", family[7])
   time.sleep(0.5)
   print("Family[8]:", family[8])
   time.sleep(0.5)
   print("Family[9]:", family[9])
   time.sleep(1)
  else:
    print("")

def start():   
 print("-Coronavirus Simulator-")
 time.sleep(1)
 #print("Utilizing ", psutil.cpu_percent(), "% of CPU power" )
 #print('Memory precentage used:', psutil.virtual_memory()[2])
 
 print("By: Theo Gillespie, David Marsh")
 time.sleep(1)
 print("Running Setup")
 simset()
 print("-Setup Complete-")
 time.sleep(1)
 begin = input("Would you like to begin transmission[]? (y/n)")
 if begin == "y":
  clear()
  print("Running transmit[]")
  transmit()

 if begin == "n":
   print("then why are you using this???")
   EndCertif()

def GUI():
  def callback(url):
    webbrowser.open_new(url)

  root= tk.Tk()

  canvas1 = tk.Canvas(root, width = 600, height =500)
  canvas1.pack()
 
  entry1 = tk.Entry (root) 
  label1 = tk.Label(root, text="Enter number of sims to run")
  canvas1.create_window(150, 100, window=label1)
  canvas1.create_window(150, 140, window=entry1)
  link1 = tk.Label(root, text="Discord", fg="blue", cursor="hand2")
  link1.pack()
  link1.bind("<Button-1>", lambda e: callback("https://discord.gg/zyw7W9m"))
  canvas1.create_window(400, 50, window=link1)
  link1 = tk.Label(root, text="Website", fg="grey", cursor="hand2")
  link1.pack()
  link1.bind("<Button-1>", lambda e: callback(""))
  canvas1.create_window(460, 50, window=link1)
  root.title('Coronasim')

  def runsim ():  
    x1 = entry1.get()
    run["state"] = DISABLED

    runtext = tk.Label(root, text="Running {} sims...".format(x1))
    canvas1.create_window(200, 230, window=runtext)

    start()
    
    
  run = tk.Button(text='Run Sim', command=runsim)
  canvas1.create_window(150, 180, window=run)



  root.mainloop()

#when the code actually starts
gc.enable()
GUI()
#start()

