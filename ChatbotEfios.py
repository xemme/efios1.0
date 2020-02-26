 # -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 19:11:18 2019

@author: xemme
"""

import os
from signif_info_append import memChange 
from signif_info_append import memRead
import vocab_Efios
from specialScripts import reply
from selenium import webdriver
import webbrowser
from datetime import datetime
from datetime import date
from time import gmtime, strftime
import pandas as pd
import random

# def reply(reply):
#     name = memRead()
#     repList = reply.split(" ")
#     repList[0].capitalize()
#     for i in range(len(repList)):
#         if repList[i] == name.lower():
#             repList[i].capitalize()
#         elif repList[i] == 'i':
#             repList[i].capitalize()
#         elif repList[i] == 'efios':
#             repList[i].capitalize()
#     print(str(reply).replace('[', '').replace(']', '').replace('\'', '').replace(',', '').replace('\"', ''))
    
# def randRes(re):
#     return random.choice(re)
    
# def anyDa(inp, statem, sel):
#     response = randRes(sel)
#     if inp in statem:
#         reply(response)
#     if response=='Here is something to get your mind off it.':
#         webbrowser.open_new("http://make-everything-ok.com/")

# def convB(inp, statem, sel, askBack):
#     if inp in statem:
#         reply(randRes(sel) + "\n" + askBack)
        
# def nameDef(aprvMsg):
#     name="Human"
#     reply("What should I call you, "+name+"?")
#     name = input()
#     memChange(name, 0)
#     reply(memRead() +", "+ randRes(aprvMsg))
#     return name
    
# def launchWeb(inp, statem, sel):
#     listcmd = inp.split(" ")
    
#     if listcmd[0] in statem:
#         service = listcmd[1]
#         if service in sel:
#             url = ("https://www."+ service +".com/")
#             reply('Launching ' + service)
#             webbrowser.open_new(url)
            
#     elif listcmd[0] in sel:
#         service = listcmd[0]
#         if service in sel:
#             url = ("https://www."+ service +".com/")
#             reply('Launching ' + service)
#             webbrowser.open_new(url)

# def launchMaps(inp, statem):
#     name = memRead()
#     listcmd = inp.split(" ")
#     location = []
#     if len(listcmd)>=2:
#         if listcmd[0]+" "+listcmd[1] in statem:
#             for i in range(len(listcmd)-2):
#                 loc = listcmd[i+2]
#                 location.append(loc)
#             locf = str(location).replace('[', '').replace(']', '').replace('\'', '').replace(',', '')
#             reply("Hold on "+ name +", I will show you where " + locf + " is.")
#             url = "https://www.google.nl/maps/place/" + locf + "/&amp;"
#             webbrowser.open_new(url)
#         elif listcmd[0]=='find':
#             for i in range(len(listcmd)-1):
#                 loc = listcmd[i+1]
#                 location.append(loc)
#             locf = str(location).replace('[', '').replace(']', '').replace('\'', '').replace(',', '')
#             reply("Hold on "+ name +", I will show you where " + locf + " is.")
#             url = "https://www.google.nl/maps/place/" + locf + "/&amp;"
#             webbrowser.open_new(url)

# def qAsk(abYou, inclLow, uninclHigh, plsInput, hapLvl, decEff, stopH):
#     reply(abYou)
#     while(1):
#         i=input()
#         if int(i) in range(inclLow,uninclHigh):
#             print("ok")
#             decEff = decEff*int(i)/10
#             hapLvl = hapLvl + hapLvl*decEff
#             #unhapLvl = 100 - hapLvl
#             #print("Happiness Level: "+str(hapLvl)+"\nUn-Happiness Level: "+str(unhapLvl)+"\n")
#             break
#         else:
#             print(plsInput)
#             continue
#     return hapLvl 

# def rememEvent(eventName, eventFreq, xxday):
#     event = ["","",""]
#     event[0] = eventName
#     event[1] = eventFreq
#     event[2] = str(str(xxday.day)+strftime("%H:%M", gmtime()))
#     return event
#     # Write to text document
    
# def detMood(hapLvl):
#     i = 0
#     plsInputTen = "Please input a value of 1-10."
#     plsInpTwo = "Please input a value of 1-2."
#     plsInpThr = "Please input a value of 1-3."
#     reply("On a scale of 1-10, with 1 being lowest and 10 being highest...")
    
#     hapLvl = qAsk("How would you describe your mood?", 1, 11, plsInputTen, hapLvl, 0.2, 11)
    
#     hapLvl = qAsk("How would you decribe your overall mood in the last month?", 1, 11, plsInputTen, hapLvl, 0.15, 11)
    
#     hapLvl = qAsk("How do you think your family think you feel daily?", 1, 11, plsInputTen, hapLvl, 0.12, 11)
    
#     reply("With 1 as NO and 2 as YES, unless otherwise stated..")
    
#     qAsk("Are you generally a happy person?", 1, 11, plsInputTen, hapLvl, 0.2, 11)
    
#     hapLvl = qAsk("Would you often talk to others if you felt happy or sad?", 1, 3, plsInpTwo, hapLvl, 0.13, 3)
#     if i == 1:
#         hapLvl = qAsk("How often do you talk to others a month? (1.Often, 2.Not often, 3.Very often)", 1, 4, plsInpThr, hapLvl, 0.12, 4)
        
#     qAsk("Are you in a relationship?", 1, 3, plsInpTwo, hapLvl, 0.2, 3)
#     if i == 1:
#         hapLvl = qAsk("How often do you see your partner in a week? (1.Often, 2.Not often, 3.Very often)", 1, 4, plsInpThr, hapLvl, 0.2, 11)
#         hapLvl = qAsk("How often do you and your partner argue? (1.Often, 2.Not often, 3.Very often)", 1, 4, plsInpThr, hapLvl, 0.1, 11)
#         # 5:1 Ratio
#     else:
#         hapLvl = qAsk("Are you dating?", 1, 3, plsInpTwo, hapLvl, 0.1, 11)
#         #Happy single?
#     hapLvl = qAsk("How many hours per day do you spend socialising?", 0, 25, "Please input a value of 0-24", hapLvl, 0.0833, 26)
#     #6 or 7 hours needed 12 times likely as joyful
#     reply("Thank you.")
#     return hapLvl

def Efios(data, name, day):
    hapLvl = 50
    unhapLvl = 50
    
    # initQ = ['who', 'what', 'when', 'where']
    # greetHello = ['hi there', 'hey', 'what is the craic', "hello", "hi", "hey there"]
    # greetRes = ['hey there', 'hello', 'how can I help?', 'what can I do for you?', 'what\'s up?', 'can I help?']
    # emoteHello = ['how are you']
    # emoteNegRes = ['not so good', 'bad', 'tired', 'not good', 'unhappy', 'lonely']
    # emotePosRes = ['good','fine', 'my CPU has never felt better.', 'happy', 'terrific', 'living the dream']
    # emoteNegResEFIOS = ['I encourage you to call a friend.', 'I encourage you to enjoy a hobby!', 'Here is something to get your mind off of it.']
    # agreeState = ['Okay!', 'I don\'t see why not', 'Agreed', 'Yes', 'Sure', 'Of course']
    # approvSt = ['I love that', 'That\'s great', 'Terrific!', 'Sounds good']
    # yes = ["yes", "yeah", "there is", "indeed", "correct"]
    # no = ["no", "no way", "negative", "nope", "incorrect"]
    # cncl = ["cancel", "exit", "leave", "ignore"]
    # timeState = ['The time is {}'.format(strftime("%H:%M", gmtime())), 'It is {}'.format(strftime("%H:%M", gmtime())), '{}'.format(strftime("%H:%M", gmtime()))]
    # cmd = ['open', 'play', 'start', 'launch']
    # services = ['youtube', 'google', 'spotify', 'sulis', 'instagram']
    # find = ['where is', 'find', 'pin point']
    
    # anyDa(data, vocab_Efios.greetHello, vocab_Efios.greetRes)
    # anyDa(data, vocab_Efios.emoteNegRes, vocab_Efios.emoteNegResEFIOS)
    # anyDa(data, vocab_Efios.emotePosRes, vocab_Efios.approvSt)
    # convB(data, vocab_Efios.emoteHello, vocab_Efios.emotePosRes, "How are you?")
    # launchWeb(data, vocab_Efios.cmd, vocab_Efios.services)
    # launchMaps(data, vocab_Efios.find)
    
    # if "gollum" in data:
    #     reply("Smeagol")
        
    # if "configure mood" in data:
    #     anyDa(data, "Configure mood", agreeState)
    #     hapLvl = detMood(hapLvl)
    #     unhapLvl = (hapLvl-100)
    #     print("Happiness Level: "+str(hapLvl)+"\nUn-Happiness Level: "+str(unhapLvl))
        
    # if "change name" in data:
    #     name = nameDef(approvSt)
    
    # if "time" in data:
    #     convB("what time is it", data, timeState, "Is there something important soon?")
    #     conf = input()
    #     if conf in no:
    #         reply("Okay.")
    #     if conf in yes:
    #         reply("Would you like me to remember this event, "+name+"?")
    #         conf = input()
    #         if conf in yes:
    #             while(1):
    #                 reply("Okay, what do you want to title this event?")
    #                 event = input()
    #                 reply("How often does "+event+" occur?")
    #                 freq = input()
    #                 if "month" or "monthly" in freq:
    #                     newEvnt = rememEvent(event, freq, day)
    #                     break
    #                 if "week" or "weekly" in freq:
    #                     newEvnt = rememEvent(event, freq, day)
    #                     break
    #                 if "day" or "daily" in freq:
    #                     newEvnt = rememEvent(event, freq, day)
    #                     break
    #                 if "hour" or "hourly" in freq:
    #                     newEvnt = rememEvent(event, freq, day)
    #                     break
    #                 if event in cncl:
    #                     reply("Okay, I won\'t remember it.")
    #                     break
    #         reply(event+ ", I will remind you from now on, "+name)
    
    
if __name__ == "__main__":
    print("Hello, I am EFIOS")
    hapLvl = 50
    unhapLvl = 50
    today = date.today()
    memRead()
    while(1):
        data = input()
        
        if data == 0:
            continue
        if 'goodbye' in str(data.lower()) or 'good bye' in str(data.lower()):
            reply("Good bye, "+ memRead())
            break
        
        Efios(data.lower(), memRead(), today)