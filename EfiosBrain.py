# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:29:32 2020

@author: xemme
"""
import specialScripts
import vocab_Efios

def Think(data, name, day, emotePer): 
    
    specialScripts.anyDa(data, vocab_Efios.changeName, vocab_Efios.approvSt, emotePer)
    specialScripts.anyDa(data, vocab_Efios.thx, vocab_Efios.noProb, emotePer)
    specialScripts.anyDa(data, vocab_Efios.greetHello, vocab_Efios.greetRes, emotePer)
    specialScripts.anyDa(data, vocab_Efios.emoteNegRes, vocab_Efios.emoteNegResEFIOS, emotePer)
    specialScripts.anyDa(data, vocab_Efios.emotePosRes, vocab_Efios.approvSt, emotePer)
    specialScripts.anyDa(data, vocab_Efios.moodConf, vocab_Efios.agreeState, emotePer)
    specialScripts.anyDa(data, vocab_Efios.sched, vocab_Efios.retSched, emotePer)
    specialScripts.convB(data, vocab_Efios.emoteHello, vocab_Efios.emotePosRes, "How are you?")
    specialScripts.launchWeb(data, vocab_Efios.cmd, vocab_Efios.services)
    specialScripts.launchMaps(data, vocab_Efios.find)
    specialScripts.timeCheck(data, vocab_Efios.timeState, day)
    
    
    
    