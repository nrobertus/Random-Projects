import csv
import numpy as np
values = np.array([])
with open('monopoly.csv', 'rb') as inputFile:
	reader = csv.reader(inputFile, delimiter=' ', quotechar='|')
	for row in reader:
		values = np.append(values, row)
while(True):
	newValue = raw_input('\'NEW\' for new entry, \'INV\' for inventory, \'EXIT\' to terminate: ')
	if(newValue == "INV"):
		values = np.array([])
		with open('monopoly.csv', 'rb') as inputFile:
			reader = csv.reader(inputFile, delimiter=' ', quotechar='|')
			for row in reader:
				values = np.append(values, row)
		for item in values:
			print item
	elif(newValue == 'EXIT'):
		break
	elif(newValue == 'NEW'):
		newValue = raw_input('Enter a new Monopoly ID: ')
		if(len(newValue) != 4):
			print "Invalid Monopoly ID"
		else:
			itemFound = False
			for item in values:
				if(item == newValue):
					itemFound = True
			if(itemFound == False):
				print "Item not in inventory."
				print "Do you wish to add", newValue, "to the inventory? (Y\N)"
				response = raw_input(":")
				if(response == 'Y'):
					with open('monopoly.csv', 'wb') as inputFile:	
						writer = csv.writer(inputFile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
						for item in values:
							writer.writerow([item])
						writer.writerow([newValue])
					print "\nItem added to inventory\n"
				elif(response == 'N'):
					print "\nValue not added to inventory\n"
				else:
					print "Response not recognized"
			else:
				print "Item already in inventory"
	else:
		print "Invalid entry, please try again\n"