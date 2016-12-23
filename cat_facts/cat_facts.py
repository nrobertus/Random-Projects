
import smtplib
import time
from time import gmtime, strftime, localtime
from random import randint

username = "premiumfelinefactoids@gmail.com"
password = "catfacts4ever"
fromaddr = "Cat Facts"

server = smtplib.SMTP("smtp.gmail.com:587")
interval = 30
fact_limit = 60
facts = ["In 1987 cats overtook dogs as the number one pet in America.","Cats that live together sometimes rub each others heads to show that they have no intention of fighting. Young cats do this more often, especially when they are excited.","Mother cats teach their kittens to use the litter box.","The way you treat kittens in the early stages of it's life will render it's personality traits later in life.","Contrary to popular belief, the cat is a social animal. A pet cat will respond and answer to speech , and seems to enjoy human companionship.","When well treated, a cat can live twenty or more years but the average life span of a domestic cat is 14 years.","Neutering a cat extends its life span by two or three years.","Cats, especially older cats, do get cancer. Many times this disease can be treated successfully.","Cats can't taste sweets.","Cats must have fat in their diet because they can't produce it on their own.","Some common houseplants poisonous to cats include: English Ivy, iris, mistletoe, philodendron, and yew.","Tylenol and chocolate are both poisionous to cats.","Many cats cannot properly digest cow's milk. Milk and milk products give them diarrhea.","The average cat food meal is the equivalent to about five mice.","Cats can get tapeworms from eating fleas. These worms live inside the cat forever, or until they are removed with medication. They reproduce by shedding a link from the end of their long bodies. This link crawls out the cat's anus, and sheds hundreds of eggs. These eggs are injested by flea larvae, and the cycles continues. Humans may get these tapeworms too, but only if they eat infected fleas. Cats with tapeworms should be dewormed by a veterinarian.","Cats can get tapeworms from eating mice. If your cat catches a mouse it is best to take the prize away from it.","A form of AIDS exists in cats.","The color of the points in Siamese cats is heat related. Cool areas are darker.","Siamese kittens are born white because of the heat inside the mother's uterus before birth. This heat keeps the kittens' hair from darkening on the points.","People who are allergic to cats are actually allergic to cat saliva or to cat dander. If the resident cat is bathed regularly the allergic people tolerate it better.","Studies now show that the allergen in cats is related to their scent glands. Cats have scent glands on their faces and at the base of their tails. Entire male cats generate the most scent. If this secretion from the scent glands is the allergen, allergic people should tolerate spayed female cats the best.","Cats do not think that they are little people. They think that we are big cats. This influences their behavior in many ways.","Cats are subject to gum disease and to dental caries. They should have their teeth cleaned by the vet or the cat dentist once a year.","Many people fear catching a protozoan disease, Toxoplasmosis, from cats. This disease can cause illness in the human, but more seriously, can cause birth defects in the unborn. Toxoplasmosis is a common disease, sometimes spread through the feces of cats. It is caused most often from eating raw or rare beef. Pregnant women and people with a depressed immune system should not touch the cat litter box. Other than that, there is no reason that these people have to avoid cats.","The ancestor of all domestic cats is the African Wild Cat which still exists today.","In ancient Egypt, killing a cat was a crime punishable by death.","In ancient Egypt, mummies were made of cats, and embalmed mice were placed with them in their tombs. In one ancient city, over 300,000 cat mummies were found.","In the Middle Ages, during the Festival of Saint John, cats were burned alive in town squares.","The first cat show was in 1871 at the Crystal Palace in London.","Today there are about 100 distinct breeds of the domestic cat.","Like birds, cats have a homing ability that uses its biological clock, the angle of the sun, and the Earth's magnetic field. A cat taken far from its home can return to it. But if a cat's owners move far from its home, the cat can't find them.","Cats bury their feces to cover their trails from predators.","Cats sleep 16 to 18 hours per day. When cats are asleep, they are still alert to incoming stimuli. If you poke the tail of a sleeping cat, it will respond accordingly.","Besides smelling with their nose, cats can smell with an additional organ called the Jacobson's organ, located in the upper surface of the mouth.","The chlorine in fresh tap water irritates sensitive parts of the cat's nose. Let tap water sit for 24 hours before giving it to a cat.","Abraham Lincoln loved cats. He had four of them while he lived in the White House.","Julius Ceasar, Henri II, Charles XI, and Napoleon were all afraid of cats.","Cats have an average of 24 whiskers, arranged in four horizontal rows on each side.","The word 'cat' in various languages: French: chat; German: katze; Italian: gatto; Spanish/Portugese: gato; Yiddish: kats; Maltese: qattus; Swedish/Norwegian: katt; Dutch: kat; Icelandic: kottur; Greek: catta; Hindu: katas; Japanese:neko; Polish: kot; Ukranian: kotuk; Hawiian: popoki; Russian: koshka; Latin: cattus; Egyptian: mau; Turkish: kedi; Armenian: Gatz; Chinese: mio; Arabic: biss; Indonesian: qitta; Bulgarian: kotka; Malay: kucing; Thai/Vietnamese: meo; Romanian: pisica; Lithuanian: katinas; Czech: kocka; Slovak: macka; Armenian: gatz; Basque: catua; Estonian: kass; Finnish: kissa; Swahili: paka.","Statistics indicate that animal lovers in recent years have shown a preference for cats over dogs!","Cats can be taught to walk on a leash, but a lot of time and patience is required to teach them. The younger the cat is, the easier it will be for them to learn.","Purring not always means happiness. Purring could mean a cat is in terrible pain such as during childbirth. Kittens will purr to their mother to let her know they are getting enough milk while nursing. Purring is a process of inhaling and exhaling, usually performed while the mouth is closed. But don't worry, if your cat is purring while your gently petting her and holding her close to you - that is a happy cat!","The catnip plant contains an oil called hepetalactone which does for cats what marijuana does to some people. Not all cats react to it those that do appear to enter a trancelike state. A positive reaction takes the form of the cat sniffing the catnip, then licking, biting, chewing it, rub & rolling on it repeatedly, purring, meowing & even leaping in the air.","Of all the species of cats, the domestic cat is the only species able to hold its tail vertically while walking. All species of wild cats hold their talk horizontally or tucked between their legs while walking.","A happy cat holds her tail high and steady.","Almost 10% of a cat's bones are in its tail, and the tail is used to maintain balance.","Cat families usually play best in even numbers. Cats and kittens should be aquired in pairs whenever possible.","Baking chocolate is the most dangerous chocolate to your cat.","You check your cats pulse on the inside of the back thigh, where the leg joins to the body. Normal for cats: 110-170 beats per minute.","Jaguars are the only big cats that don't roar.","A cats field of vision is about 185 degrees.","Cats have individual preferences for scratching surfaces and angles. Some are horizontal scratchers while others exercise their claws vertically.","The Maine Coone is the only native American long haired breed.","The Maine Coon is 4 to 5 times larger than the Singapura, the smallest breed of cat.","Tabby cats are thought to get their name from Attab, a district in Baghdad, now the capital of Iraq.","Retractable claws are a physical phenomenon that sets cats apart from the rest of the animal kingdom. I n the cat family, only cheetahs cannot retract their claws.","Not every cat gets 'high' from catnip. Whether or not a cat responds to it depends upon a recessive gene: no gene, no joy.","A cat can sprint at about thirty-one miles per hour.","In ancient Egypt, when a family cat died, all family members would shave their eyebrows as a sign of mourning.","Cats have been domesticated for half as long as dogs have been.","A cat's whiskers are thought to be a kind of radar, which helps a cat gauge the space it intends to walk through.","A cat can spend five or more hours a day grooming himself.","All cats have three sets of long hairs that are sensitive to pressure - whiskers, eyebrows,and the hairs between their paw pads.","Both humans and cats have identical regions in the brain responsible for emotion.","A cat's brain is more similar to a man's brain than that of a dog.","A cat has more bones than a human; humans have 206, and the cat - 230.","Cats have 30 vertebrae--5 more than humans have."]

welcomeMessages = ["Welcome to Cat Facts!", "You will now receive " + str(fact_limit) + " Cat Facts in " + str(interval) + " second intervals!", "Prepare for a delightful onslaught of feline factoids!"]
recipients = []
facts = []

suffix = ""

def initialize():
    #getFacts()
    getRecipient()

    server.starttls()
    server.login(username,password)

def getRecipient():
    input = raw_input("Enter a number to CatFacts (single number or multiple) :  ")
    input = input.split(' ')
    for recipient in input:
        recipients.append(str(recipient))
    input = raw_input("Type 'A' for AT&T and 'V' for Verizon: ")
    if(input == 'A'):
        suffix = "@txt.att.net"
    elif(input == 'V'):
        suffix = "@vtext.com"
    else:
        print "Invalid carrier. Exiting"
        sys.exit();
    formatRecipients(suffix)

def sendGreeting():
    for message in welcomeMessages:
        sendMessage(message)
        time.sleep(interval)

def sendFacts():
    for x in range (0, fact_limit):
        print ("\n------Fact " + str(x+1) + " of " + str(fact_limit) + "------")
        sendMessage(getRandomFact())
        time.sleep(interval)

def getFacts():
    if len(facts) == 0:
        f = open('catfacts.txt', 'r')
        for fact in f:
            facts.append(fact)

def formatRecipients(given_suffix):
    for i,recipient in enumerate(recipients):
        recipients[i] = str(recipient) + given_suffix

def getRandomFact():
    if(len(facts) == 0):
        getFacts()
    index = randint(0, (len(facts)-1))
    return facts[index]

def getTime():
    return strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

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
        print "--Sent to: " + str(number) + " at " + str(getTime()) + "--"
        print body

initialize()

sendGreeting()

sendFacts()

server.quit()
cat_facts.py
Displaying cat_facts.py.
