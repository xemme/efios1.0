# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:45:50 2020

@author: xemme
"""

import EfiosBrain
import vocab_Efios
import specialScripts
import signif_info_append
import schedule
from datetime import date

def emotePerFind(i):
     return float(((signif_info_append.memRead(i+5).split(" "))[1]))
        

if __name__ == "__main__":
    today = date.today()
    i=0
    
    # emotePer = [signif_info_append.memRead(5), signif_info_append.memRead[6], signif_info_append.memRead(7), signif_info_append.memRead(8)]
    emotePer = [0, 0, 0, 0]
    for i in range(0, 4):
        emotePer[i] = float(((signif_info_append.memRead(i+5).split(" "))[1]))
    
    #Time Checker for Schedule
    schedule.every(5).minutes.do(specialScripts.checkSched) 
    print("Hello!\nText to me just like you would a human.")
    while(1):
        if str(signif_info_append.memRead(0)) == "name\n":
            specialScripts.niceToMeetYou()
        else:
            data = input()
            specialScripts.dataInp(data)
            
            
            if data == 0:
                continue
            if str(data.lower()) in vocab_Efios.closeEfios:
                specialScripts.reply("Good bye, "+ signif_info_append.memRead(0))
                break
            
            EfiosBrain.Think(data.lower().replace('?', ''), signif_info_append.memRead(0), today, emotePer)