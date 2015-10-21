import smtplib
import time
from time import gmtime, strftime, localtime
from random import randint


username = "premiumfelinefactoids@gmail.com"
password = "pirate4ever"
fromaddr = "Cat Facts"


recipients = [4065706601, 4065704684]
#recipients = [4065706601]
facts = []

#Setup the server
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)

def initialize():
    getFacts()
    formatRecipients()

def getFacts():
    f = open('catfacts.txt', 'r')
    for fact in f:
        facts.append(fact)

def formatRecipients():
    for i,recipient in enumerate(recipients):
        recipients[i] = str(recipient) + "@vtext.com"

def getRandomFact():
    if(len(facts) == 0):
        getFacts()

    index = randint(0, len(facts))

    return facts[index]

def getTime():
    return time.time()

def show_Full_Time():
    return strftime("%a, %d %b %Y %H:%M:%S", localtime())

def showTime(startTime, endTime):
    timeUsed = endTime - startTime
    hoursHold = int(timeUsed / 3600)
    minutesHold = int(timeUsed / 60 - int(hoursHold * 60))
    secondsHold = int(timeUsed - int(minutesHold * 60))
    formattedTime = str(hoursHold) + ":" + str(minutesHold) + ":" + str(secondsHold)
    return formattedTime

def sendMessage(body):
    for number in recipients:
        server.sendmail(fromaddr, number, body)
        print body + " was sent to " + number + "!"

initialize()

for x in range (0, 20):
    sendMessage(getRandomFact())
    time.sleep(30)

server.quit()