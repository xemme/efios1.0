# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 22:48:49 2020

@author: xemme
"""

def closef(file):
    file.close()
    
def errorCheck(lines):
    if 9 == int(len(lines)):
        print("Passing")
    elif int(len(lines)) > 9 or int(len(lines)) < 9:
        print("Error: File Length Wrong")
    
def memChange(attr, l):
    file = open("signif_info.txt", "r")
    lines = file.readlines()
    
    # errorCheck(lines)
    
    file.close()
    lines[l] = attr+"\n"
    file = open("signif_info.txt", "w")
    for i in range(len(lines)):
        file.write(lines[i])
    file.close()
    
def memRead(l):
    file = open("signif_info.txt", "r")
    lines = file.readlines()
    if l == 0:
        firstLast = lines[l].split(" ")
        return firstLast[0]
    file.close()
    return lines[l]
