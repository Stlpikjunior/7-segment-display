import tkinter as tk
from datetime import datetime


win = tk.Tk()
canvas = tk.Canvas(win, width=800, height=800, bg="black")
canvas.pack()


class line:
    def __init__(self, point: tuple, s: int, b: int, canvas, colour, state):  # nemali by sme pouzivat global - dbig dsmall = dx dy
        self.coords = point
        x,y = point[0],point[1]
        self.state = state
        self.s = s
        self.b = b
        self.canvas = canvas
        self.colour = colour
        if state == 'v':
            self.id = canvas.create_polygon(x,y,x+s/2,y-s/2,x+s,y, x+s, y+b, x+s/2, y+b+s/2,x, y+b, fill=colour, outline="")
        elif state == 'h':
            self.id = canvas.create_polygon(x, y, x+b, y, x+b+s/2, y+s/2, x+b, y+s, x, y+s, x-s/2, y+s/2, fill=colour, outline="")


    def on(self):# zober id objektu a zmen farbu na colour
       self.canvas.itemconfig(self.id, fill=self.colour)


    def off(self):  # zober id objekty a zmen farbu naspat na white
       self.canvas.itemconfig(self.id, fill="black")




class segment:
   def __init__(self, point: tuple, small: int, big: int, canvas, colour: str):
       self.parts = []
       self.colour = colour
       sx = point[0]
       sy = point[1]  # nemusi byt self lebo zaniknu pri zaniknuuti konstruktoru
       self.coords = point
       self.parts.append(line((sx + small, sy), small, big, canvas, colour, 'h'))  # segment0
       self.parts.append(line((sx + small + big, sy + small), small, big, canvas, colour, 'v'))  # segment1
       self.parts.append(line((sx + small, sy + small + big), small, big, canvas, colour, 'h'))
       self.parts.append(line((sx, sy + small), small, big, canvas, colour, 'v'))
       self.parts.append(line((sx + small + big, sy + 2 * small + big), small, big, canvas, colour, 'v'))
       self.parts.append(line((sx + small, sy + 2 * big + 2 * small), small, big,   canvas, colour, 'h'))
       self.parts.append(line((sx, sy + 2 * small + big), small, big, canvas, colour, 'v'))




   def reset(self):
       for part in self.parts:  # zhasni ty mrcha
           part.off()


   def error(self):
       for part in self.parts:  # zhasni ty mrcha
           part.on()


   def display(self, number: int):
       if number == 0:
           self.error()
           self.parts[2].off()
       if number == 1:
           self.reset()
           self.parts[1].on()
           self.parts[4].on()
       elif number == 2:
           self.error()
           self.parts[3].off()
           self.parts[4].off()
       elif number == 3:
           self.error()
           self.parts[3].off()
           self.parts[6].off()
       elif number == 4:
           self.error()
           self.parts[0].off()
           self.parts[5].off()
           self.parts[6].off()
       elif number == 5:
           self.error()
           self.parts[1].off()
           self.parts[6].off()
       elif number == 6:
           self.error()
           self.parts[1].off()
       elif number == 7:
           self.error()
           self.parts[2].off()
           self.parts[3].off()
           self.parts[6].off()
           self.parts[5].off()
       elif number == 8:
           self.error()
       elif number == 9:
           self.error()
           self.parts[6].off()


class Clock:
   def __init__(self, point: tuple,small: int, big: int, canvas, colour):
       # bude sa menit x  ova suradnica
       self.numms = []
       self.coords = point
       self.coordzies = []
       self.small = small
       self.big = big
       self.point = point
       self.canvas = canvas
       self.colour = colour
       for i in range(0,6,2):
           self.coordzies.append(segment((self.point[0] + i * (self.small*2 +self.big+20), self.point[1]), self.small,self.big,  self.canvas, self.colour))
           self.coordzies.append(segment((self.point[0] + i * (2 * self.small + self.big+20) + (3*self.small + self.big), self.point[1]), self.small,self.big, self.canvas, self.colour))

           if i <4:
               self.hi = canvas.create_oval( #omnoho prehladnejsie pri komplikovanejsich suradniciach
                   self.point[0] + i * (2 * self.small + self.big+20) + 5*self.small + 2*self.big+10,
                   self.point[1]+(2 * self.small + self.big)/2-5,
                   self.point[0] + i * (2 * self.small + self.big+20) + 5*self.small + 2*self.big+20,
                   self.point[1]+(2 * self.small + self.big)/2+5, fill = 'OrangeRed2')
               self.lo = canvas.create_oval(
                   self.point[0] + i * (2 * self.small + self.big + 20) + 5 * self.small + 2 * self.big + 10,
                   self.point[1] + self.small+ self.big + (2 * self.small + self.big) / 2 - 5,
                   self.point[0] + i * (2 * self.small + self.big + 20) + 5 * self.small + 2 * self.big + 20,
                   self.point[1] + self.small+ self.big +(2 * self.small + self.big) / 2 + 5, fill='OrangeRed2')

   def hodziny(self):
       cas = datetime.now().strftime('%H%M%S')
       for i in range(6):
           cisliica = cas[i]
           self.coordzies[i].display(int(cisliica))

       win.after(1000, skuska.hodziny)




cas = datetime.now().strftime('%H%M%S')
skuska = Clock((50,50), 10, 40, canvas, "OrangeRed2")
skuska.hodziny()
win.mainloop()
