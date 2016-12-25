from random import randint

doors = []

iterations = 1000000
wins = 0
losses = 0
win_percentage = 0


####################
##    Classes     ##
####################
class door:
        def __init__(self, id):
            self.open = False
            self.winner = False
            self.selected = False
            self.id = id

####################
##    Printing    ##
####################

def printDoors():
    print "========================================"
    for door in doors:
        print "Door  " + str(door.id)
        print "Open: " + str(door.open)
        print "Winner: " + str(door.winner)
        print "Selected: " + str(door.selected)
    print "========================================"

def printResults(type):
    global wins
    global losses
    global win_percentage
    print "==================================="
    print "Type: " + type
    print "Iterations: " + str(iterations)
    print "Wins: " + str(wins)
    print "Losses: " + str(losses)
    print "Win percentage: " + str(win_percentage)
    print "==================================="


####################
##    Door ops    ##
####################


def createDoors():
    doors.append(door(1))
    doors.append(door(2))
    doors.append(door(3))


def destroyDoors():
    doors[:] = []

def selectWinner():
    if(len(doors) == 3):
        rand = randint(0, 2)
        doors[rand].winner = True;

def selectDoor():
    if(len(doors) == 3):
        rand = randint(0, 2)
        doors[rand].selected = True;

def openDoor():
    unselected = []
    if(len(doors)==3):
        for door in doors:
            if(door.selected == False):
                unselected.append(door)
        if(unselected[0].winner == False and unselected[1] == False):
                rand = randint(1, 2)
                unselected[rand].open = True

        else:
            if unselected[0].winner == False:
                unselected[0].open = True
            else:
                unselected[1].open = True

def switch():
    unopened = []
    if(len(doors)==3):
        for door in doors:
            if(door.open == False):
                unopened.append(door)
        if unopened[0].selected == True:
            unopened[0].selected = False
            unopened[1].selected = True
        else:
            unopened[1].selected = False
            unopened[0].selected = True

####################
##    System      ##
####################

def evaluate():
    if(len(doors) == 3):
        for door in doors:
            if door.selected == True and door.winner == True:
                global wins
                wins += 1
            elif door.selected == True and door.winner == False:
                global losses
                losses += 1
        global win_percentage
        win_percentage = 100 * float(wins)/float(iterations)

def runTest(test_type):
    for i in range(iterations):
        createDoors()
        selectWinner()
        selectDoor()
        openDoor()
        if test_type == "switch":
            switch()
        evaluate()
        destroyDoors()
    printResults(test_type)
    reset()

def reset():
    global wins
    wins = 0
    global losses
    losses = 0
    global win_percentage
    win_percentage = 0

####################
##    Operation   ##
####################

runTest("switch")
runTest("stay")
