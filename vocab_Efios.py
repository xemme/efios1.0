# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:37:20 2020

@author: xemme
"""

from time import gmtime, strftime
from datetime import date

initQ = ['who', 'what', 'when', 'where']
greetHello = ['hi there', 'hey', 'what is the craic', "hello", "hi", "hey there"]
greetRes = ['hey there', 'hello', 'how can I help?', 'what can I do for you?', 'what\'s up?', 'can I help?']
emoteHello = ['how are you']
emoteNegRes = ['not so good', 'bad', 'tired', 'not good', 'unhappy', 'lonely']
emotePosRes = ['good','fine', 'my CPU has never felt better.', 'happy', 'terrific', 'living the dream']
emoteNegResEFIOS = ['I encourage you to call a friend.', 'I encourage you to enjoy a hobby!', 'Here is something to get your mind off of it.']
agreeState = ['Okay!', 'I don\'t see why not', 'Agreed', 'Yes', 'Sure', 'Of course']
approvSt = ['I love that', 'That\'s great', 'Terrific!', 'Sounds good']
yes = ["yes", "yeah", "there is", "indeed", "correct"]
no = ["no", "no way", "negative", "nope", "incorrect"]
cncl = ["cancel", "exit", "leave", "ignore"]
timeState = ['The time is {}'.format(strftime("%H:%M", gmtime())), 'It is {}'.format(strftime("%H:%M", gmtime())), '{}'.format(strftime("%H:%M", gmtime()))]
dayState = ['It is {}'.format(date.today()), 'Today is {}'.format(date.today()), '{}'.format(date.today())]
cmd = ['open', 'play', 'start', 'launch']
services = ['youtube', 'google', 'spotify', 'sulis', 'instagram']
find = ['where is', 'find', 'pin point']
changeName = ['change my name', 'call me', 'rename me', 'change name']
thx = ['thank you', 'thanks', 'thank you very much', 'sound']
noProb = ['Anytime', 'No problem', 'Of course', 'That\'s why I\'m here']
closeEfios = ['goodbye', 'good bye', 'see you', 'bye', 'sleep']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
moodConf = ['measure mood', 'measure stress', 'mood', 'configure mood', 'find happiness']
sched = ['do i have anything on', 'my class', 'am i free', 'where is my next class', 'class details', 'next lecture', 'what do I have now']
retSched = ['Your next class is ', 'You have ', '']