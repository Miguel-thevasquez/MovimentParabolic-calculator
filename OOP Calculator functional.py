# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 08:15:14 2023

@author: Miguel Angel
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#variable def---------------------------------------------
T = "0"
#functions------------------------------------------------
class Calc:
    def add(self,x, y):
        return x+y
    def sub(self,x, y):
        return x-y
    def mult(self,x, y):
        return x*y
    def div(self,x, y):
        return x/y


#---------------------------------------------------------
while T !="Exit":
    S = str.capitalize(input("select between:\n 1.plus\n 2.sub\n 3.mult\n 4.div\n 5.showcase\n 6.close\n" + "==> "))
    if S in ("1","2","3","4","5") or S in ("Plus","Sub","Mult","Div","Showcase","Close"):
        if S == "1" or S =="Plus" :
            x = int(input("set n1\n"))
            y = int(input("set n2\n"))
            print("--------------------------\n NUMBER IS\n " + str(Calc.add( 0,x,y))+"\n--------------------------\n")
        elif S == "2" or S =="Sub" :
            x = int(input("set n1\n"))
            y = int(input("set n2\n"))
            print("--------------------------\n NUMBER IS\n " + str(Calc.sub(0,x,y))+"\n--------------------------\n")
        elif S == "3" or S =="Mult" :
            x = int(input("set n1\n"))
            y = int(input("set n2\n"))
            print("--------------------------\n NUMBER IS\n " + str(Calc.multi(0,x,y))+"\n--------------------------\n")
        elif S == "4" or S == "Div" :
            x = int(input("set n1\n"))
            y = int(input("set n2\n"))
            print("--------------------------\n NUMBER IS\n " + str(Calc.div(0,x,y))+"\n--------------------------\n")
        elif S == "5" or S == "Showcase":
            x = int(input("set n1\n"))
            y = int(input("set n2\n"))
            print("--------------------------\n NUMBER ON + IS " + str(Calc.add(0,x, y)) + "\n NuMBER ON - IS " + str(Calc.sub(0,x, y)) + "\n NUMBER ON * IS " + str(Calc.mult(0,x, y)) + "\n NUMBER ON / IS " + str(Calc.div(0, x, y)) +"\n--------------------------\n")
        
        elif S == "Close" or S== "6":
            T = "Exit"
            break