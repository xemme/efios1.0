# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:26:41 2020

@author: xemme
"""

from time import gmtime, strftime
from datetime import datetime 
import webbrowser
import random
import vocab_Efios
from EfiosCloud import retVal
import signif_info_append
    
def reply(reply):
    name = signif_info_append.memRead(0)
    repList = reply.split(" ")
    repList[0].capitalize()
    for i in range(len(repList)):
        if repList[i] == name.lower():
            repList[i].capitalize()
        elif repList[i] == 'i':
            repList[i].capitalize()
        elif repList[i] == 'efios':
            repList[i].capitalize()
    re = str(reply).replace('[', '').replace(']', '').replace('\'', '').replace(',', '').replace('\"', '')
    print(re)
    
def randRes(re):
    return random.choice(re)
    
def anyDa(inp, statem, sel, happiness):
    response = randRes(sel)
    if inp in statem:
        if inp in vocab_Efios.changeName:
            nameDef(sel)
        elif inp in vocab_Efios.moodConf:
            detMood(happiness)
            reply(response)
        else:
            reply(response)
        if response=='Here is something to get your mind off it.':
            url = "https://www.make-everything-ok.com"
            webbrowser.open_new(url)

def convB(inp, statem, sel, askBack):
    if inp in statem:
        reply(randRes(sel) + "\n" + askBack)
        
def nameDef(aprvMsg):
    name="Human"
    reply("What should I call you, "+name+"?")
    name = input()
    signif_info_append.memChange(name, 0)
    reply(signif_info_append.memRead(0) +", "+ randRes(aprvMsg))
    return name
    
def launchWeb(inp, statem, sel):
    listcmd = inp.split(" ")
    if listcmd[0] in statem:
        service = listcmd[1]
        url = ("https://www."+ service +".com/")
        reply('Launching ' + service)
        webbrowser.open_new(url)
            
    elif listcmd[0] in sel:
        service = listcmd[0]
        url = ("https://www."+ service +".com/")
        reply('Launching ' + service)
        webbrowser.open_new(url)

def launchMaps(inp, statem):
    name = signif_info_append.memRead(0)
    listcmd = inp.split(" ")
    location = []
    if len(listcmd)>=2:
        if listcmd[0]+" "+listcmd[1] in statem:
            for i in range(len(listcmd)-2):
                loc = listcmd[i+2]
                location.append(loc)
            locf = str(location).replace('[', '').replace(']', '').replace('\'', '').replace(',', '')
            reply("Hold on "+ name +", I will show you where " + locf + " is.")
            url = "https://www.google.nl/maps/place/" + locf + "/&amp;"
            webbrowser.open_new(url)
        elif listcmd[0]=='find':
            for i in range(len(listcmd)-1):
                loc = listcmd[i+1]
                location.append(loc)
            locf = str(location).replace('[', '').replace(']', '').replace('\'', '').replace(',', '')
            reply("Hold on "+ name +", I will show you where " + locf + " is.")
            url = "https://www.google.nl/maps/place/" + locf + "/&amp;"
            webbrowser.open_new(url)

def qAsk(abYou, inclLow, uninclHigh, plsInput, emotePer):
    reply(abYou)
    while(1):
        i=input()
        if int(i) in range(inclLow,uninclHigh):
            print("ok")
            
            return emotePer 
            break
        else:
            print(plsInput)
            continue

def rememEvent(eventName, eventFreq, xxday):
    event = ["","",""]
    event[0] = eventName
    event[1] = eventFreq
    event[2] = str(str(xxday.day)+strftime("%H:%M", gmtime()))
    return event
    # Write to text document
    
def detMood(hapLvl):
    i = 0
    plsInputTen = "Please input a value of 1-10."
    plsInpTwo = "Please input a value of 1-2."
    plsInpThr = "Please input a value of 1-3."
    reply("On a scale of 1-10, with 1 being lowest and 10 being highest...")
    
    hapLvl = qAsk("How would you describe your mood?", 1, 11, plsInputTen, hapLvl, 0.2, 11)
    
    hapLvl = qAsk("How would you decribe your overall mood in the last month?", 1, 11, plsInputTen, hapLvl, 0.15, 11)
    
    hapLvl = qAsk("How do you think your family think you feel daily?", 1, 11, plsInputTen, hapLvl, 0.12, 11)
    
    reply("With 1 as NO and 2 as YES, unless otherwise stated..")
    
    qAsk("Are you generally a happy person?", 1, 11, plsInputTen, hapLvl, 0.2, 11)
    
    hapLvl = qAsk("Would you often talk to others if you felt happy or sad?", 1, 3, plsInpTwo, hapLvl, 0.13, 3)
    if i == 1:
        hapLvl = qAsk("How often do you talk to others a month? (1.Often, 2.Not often, 3.Very often)", 1, 4, plsInpThr, hapLvl, 0.12, 4)
        
    qAsk("Are you in a relationship?", 1, 3, plsInpTwo, hapLvl, 0.2, 3)
    if i == 1:
        hapLvl = qAsk("How often do you see your partner in a week? (1.Often, 2.Not often, 3.Very often)", 1, 4, plsInpThr, hapLvl, 0.2, 11)
        hapLvl = qAsk("How often do you and your partner argue? (1.Often, 2.Not often, 3.Very often)", 1, 4, plsInpThr, hapLvl, 0.1, 11)
        # 5:1 Ratio
    else:
        hapLvl = qAsk("Are you dating?", 1, 3, plsInpTwo, hapLvl, 0.1, 11)
        #Happy single?
    hapLvl = qAsk("How many hours per day do you spend socialising?", 0, 25, "Please input a value of 0-24", hapLvl, 0.0833, 26)
    #6 or 7 hours needed 12 times likely as joyful
    reply("Thank you.")
    return hapLvl

def gollumTest(data):
    if "gollum" in data:
        reply("Smeagol")
        
def changeName(data, approvSt):
    if "change name" in data:
        name = nameDef(approvSt)

def timeCheck(data, timeState, day):
    if "time" in data:
        convB("what time is it", data, timeState, "Is there something important soon?")
        conf = input()
        if conf in vocab_Efios.no:
            reply("Okay.")
        if conf in vocab_Efios.yes:
            reply("Would you like me to remember this event, "+signif_info_append.memRead(0)+"?")
            conf = input()
            if conf in vocab_Efios.yes:
                while(1):
                    reply("Okay, what do you want to title this event?")
                    event = input()
                    reply("How often does "+event+" occur?")
                    freq = input()
                    if "month" or "monthly" in freq:
                        newEvnt = rememEvent(event, freq, day)
                        break
                    if "week" or "weekly" in freq:
                        newEvnt = rememEvent(event, freq, day)
                        break
                    if "day" or "daily" in freq:
                        newEvnt = rememEvent(event, freq, day)
                        break
                    if "hour" or "hourly" in freq:
                        newEvnt = rememEvent(event, freq, day)
                        break
                    if event in vocab_Efios.cncl:
                        reply("Okay, I won\'t remember it.")
                        break
            reply(event+ ", I will remind you from now on, "+signif_info_append.memRead(0))
    elif "day" in data:
        reply(randRes(vocab_Efios.dayState))
    elif 'day' in data and 'time' in data:
        reply(randRes(vocab_Efios.timeState) + " " + vocab_Efios.dayState[len(vocab_Efios.dayState)-1])
        
def niceToMeetYou():
    reply("Hello!\nI am very excited to meet you.\nMy name is EFIOS (ee-fee-ous).\nWhat\'s your name?")
    name = input()
    signif_info_append.memChange(name, 0)
    reply(signif_info_append.memRead(0).replace("\n", "")+", I like that.\nNice to meet you.\n")
    
def retTime(form):
    today = datetime.now()
    return today.strftime(form)

def checkSched():
    #day = retTime('%d/%m')
    day = '20/2'
    time = '16:02'
    #time = retTime('%H:%M')
    #print(time)
    for a in ['C', 'D', 'E', 'F', 'G', 'H', 'I']:
        val = retVal(a, '3')
        trf = str(val).find(day)
        if trf != -1:
            #print('Match')
            # Dates Match
            for i in range(5, 27):
                if i>=10:
                    targetT = str(retVal('B', str(i)))[13:-2]
                    print(targetT)
                    
                else:
                    targetT = str(retVal('B', str(i)))[12:-2]
                    
                currentMin = int(time[-2:])
                condMin = int(targetT[-2:])
                
                if time[:2] == targetT[:2] and currentMin < 59 and condMin == 30:
                    event = str(retVal(a, str(i+1)))[-23:-1].replace('\'', '').replace(' ', '')
                    return event
    #    else:
            #print('No Match')