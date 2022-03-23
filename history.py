# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[5,3,4,6,7,8]

def createPlots():
 plt.barh(x,y)

 print("Seeing how branching effects the repository")
 
def main():
    createPlots()
    createPlots()

if __name__ == "__main__":
    main()