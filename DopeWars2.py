# Dope Wars clone in Python

from sys import exit
import random

from __future__ import print_function
import fixpath

from colorama import init, Fore, Back, Style

init ()

prompt = Fore.GREEN + " > " + Fore.RESET

Cash = 2000.00
CoatTotal = 100
CoatSpaceUsed = 0
IOU = 2000.00
Day = 1 
Savings = 0.00

Drugs = ["Heroin", "Cocaine", "LSD", "Ludes", "Extasy", "Weed", "Krokodil"]
Hoods = ["Manhattan", "Brooklyn", "Coney Island", "Central Park", "Bronx", "New Jersey"]

#Drugs Base Price

HeroinBasePrice = 100
CocaineBasePrice = 5000
LSDBasePrice = 100
LudesBasePrice = 300
ExtasyBasePrice = 1000
WeedBasePrice = 150
KrokodilBasePrice = 20

#Drug Inventory on coat

HeroinInventory = 0
CocaineInventory = 0
LSDInventory = 0
LudesInventory = 0
ExtasyInventory = 0
WeedInventory = 0
KrokodilInventory = 0

#Initialize Random Generator
random.seed()

print'''
\033[1;32;40m Welcome to DopeWars homie!!!
\033[0;37;40m How about making some money? \n 
'''

def AskDays():
	print'''\033[1;33;40m
	1. New 5 day Game
	2. New 30 day Game
	3. new 60 day Game
	\033[0;37;40m
	'''
	
	dayschoice = raw_input(prompt)
	
	if dayschoice == "1":
		return ("5")
	elif dayschoice == "2":
		return ("30")
	elif dayschoice == "3":
		return ("60")
	else:
		return (False)

def DaySummary (day, cash, coatspaceused, coattotal, iou, savings):

	print '\033[1;33;40m***********************************************'
	print ' Hey Yo homey! How are you today! Day %d of %d ' % (day, int(DaysChoice))
	print '***********************************************'
	print 'Cash: %d' % cash
	print 'Coat: %d / %d' % (coatspaceused, coattotal)
	print 'IOU: $%d' % iou 
	print 'Savings: $%d' % savings
	print '***********************************************\n \n\033[0;37;40m'

def RandomizeDrugPrice (DrugBasePrice, low, high):

	# random factor range between Low and High / 10 * DrugBasePrice
	DrugPrice = DrugBasePrice * (random.uniform (low, high) / 10)

	return (DrugPrice)

def DailyDrugPrice ():

	heroin = RandomizeDrugPrice (HeroinBasePrice, 2, 25)
	cocaine =  RandomizeDrugPrice (CocaineBasePrice, 2, 25)
	lsd = RandomizeDrugPrice (LSDBasePrice, 2, 25)
	ludes = RandomizeDrugPrice (LudesBasePrice, 2, 25)
	extasy = RandomizeDrugPrice (ExtasyBasePrice, 2, 25)
	weed = RandomizeDrugPrice (WeedBasePrice, 2, 25)
	krokodil = RandomizeDrugPrice (KrokodilBasePrice, 1, 40)

	print '\033[1;32;40m+++++++++++++++++++++++++++++++'
	print ' Dope Prices today!'
	print '+++++++++++++++++++++++++++++++'
	print '+ Heroin:   $ %d' % heroin 
	print '+ Cocaine:  $ %d' % cocaine
	print '+ LSD:      $ %d' % lsd
	print '+ Ludes:    $ %d' % ludes
	print '+ Extasy:   $ %d' % extasy
	print '+ Weed:     $ %d' % weed
	print '+ Krokodil: $ %d' % krokodil
	print '+++++++++++++++++++++++++++++++\033[0;37;40m '

	return (heroin, cocaine, lsd, ludes, extasy, weed, krokodil)

def cash2drugs (heroin, cocaine, lsd, ludes, extasy, weed, krokodil):
	global Cash
	global CoatTotal
	global CoatSpaceUsed
	global HeroinInventory
	global CocaineInventory
	global LSDInventory
	global LudesInventory
	global ExtasyInventory
	global WeedInventory
	global KrokodilInventory

	heroinshots = (Cash / heroin)
	cocainshots = (Cash / cocaine)
	lsdshots = (Cash / lsd)
	ludesshots = (Cash / ludes)
	extasyshots = (Cash / extasy)
	weedshots = (Cash / weed)
	krokodilshots = (Cash / krokodil)
	
	print '** You have $ %d **, you can buy:\n' % Cash 
	print '  1. Heroin %d shots' % heroinshots 
	print '  2. Cocaine %d shots' % cocainshots
	print '  3. LSD %d shots' % lsdshots
	print '  4. Ludes %d shots' % ludesshots
	print '  5. Extasy %d shots' % extasyshots
	print '  6. Weed %d shots' % weedshots
	print '  7. Krokodil %d shots' % krokodilshots
	print '  \n    Spaces left on your coat: %r' %  int (CoatTotal - CoatSpaceUsed)

	print '\n Select drug:'
	selection = raw_input(prompt)

	if selection == '1':
		print 'Heroin shots? %d Max' % heroinshots
		hshots = int (raw_input(prompt))
		while hshots > heroinshots:
			hshots = int (raw_input(prompt))
		print '*** Thats $ %d dollars dude!!' % (hshots * heroin)
		HeroinInventory = HeroinInventory + hshots
		Cash = Cash - (hshots * heroin)
		CoatSpaceUsed = CoatSpaceUsed + HeroinInventory
		return (True)
	elif selection == '2':
		print 'Cocaine shots? %d Max' % cocainshots
		cshots = int (raw_input(prompt))
		while cshots > cocaineshots:
			cshots = int (raw_input(prompt))
		print '*** Thats $ %d dollars dude!!' % (cshots * cocaine)
		CocaineInventory = CocaineInventory + cshots
		Cash = Cash - (cshots* cocaine)
		CoatSpaceUsed = CoatSpaceUsed + CocaineInventory
		return (True)
	elif selection == '3':
		LSDInventory = LSDInventory + lsdshots
		Cash = Cash - (lsdshots * lsd)
		CoatSpaceUsed = CoatSpaceUsed + LSDInventory
		return (True)
	elif selection == '4':
		LudesInventory = ludeshots + LudesInventory
		CoatSpaceUsed = CoatSpaceUsed + LudesInventory
		Cash = Cash - (ludesshots * ludes)
		return (True)
	elif selection == '5':
		ExtasyInventory = ExtasyInventory + extasyshots
		Cash = Cash - (extasyshots * extasy)
		CoatSpaceUsed = CoatSpaceUsed + ExtasyInventory
		return (True)
	elif selection == '6':
		WeedInventory = WeedInventory + weedshots
		Cash = Cash - (weedshots * weed)
		CoatSpaceUsed = CoatSpaceUsed + WeedInventory
		return (True)
	elif selection == '7':
		KrokodilInventory = KrokodilInventory + krokodilshots
		Cash = Cash - (krokodilshots * krokodil)
		CoatSpaceUsed = CoatSpaceUsed + KrokodilInventory
		return (True)
	else:
		return (False)

def BuyDrugs (heroin, cocaine, lsd, ludes, extasy, weed, krokodil):
	print "\n \n  *** Do you wanna buy drugs?"
	buy = raw_input(prompt)
	if buy == "y":
		cash2drugs (heroin, cocaine, lsd, ludes, extasy, weed, krokodil)
	else:
		print 'Cool Dude, no problemo!! \n'		

def TotalInventory ():
	print '''
		Dude, 
			your dirty coat has:

	'''
	print 'Heroin Shots %d' % HeroinInventory
        print 'Cocaine Shots %d' % CocaineInventory
        print 'LSDShots %d' % LSDInventory
        print 'Ludes Shots %d' % LudesInventory
        print 'Extasy Shots %d' % ExtasyInventory
        print 'Weed Shots %d' % WeedInventory
        print 'Krokodil Shots %d' % KrokodilInventory


def TravelToHood ():
	print '''
		\033[1;35;40m Yo, Where do ya' wanna go?\033[0;37;40m

		\033[1;36;40m1. Manhattan
		2. Brooklyn
		3. Coney Island
		4. Central Park
		5. The Bronx
		6. New Jersey
		\033[0;37;40m
	'''
	hood = raw_input(prompt)
	if hood == "1":
		print 'Traveling to Manhattan....'
		return ("1")
	elif hood == "2":
		print 'Traveling to Brooklin....'
		return ("2")
	elif hood == '3':
		print 'Traveling to Coney Island....'
		return ("3")
	elif hood == '4':
		print 'Traveling to Central Park....'
		return ("4")
	elif hood == '5':
		print 'Traveling to The Bronx....'
		return ("5")
	elif hood == '6':
		print 'Traveling to New Jersey....'
		return ("6")
	else:
		return (false)


# **** MAIN GAME ****
# Ask and Get number of days for the game

DaysChoice = AskDays()

while DaysChoice not in ["5", "30", "60"]:
	DaysChoice = AskDays()

print "\033[0;31;47m You have %s days to make a lot of money \033[0;37;40m" % DaysChoice 

n = 0 
Days = int(DaysChoice)

while n < Days:
	
	# How are you toAday?

	HoodChoice = TravelToHood()
	while HoodChoice not in ["1", "2", "3", "4", "5", "6"]:
		HoodChoice = TravelToHood()

	DaySummary (n + 1, Cash, CoatSpaceUsed, CoatTotal, IOU, Savings)
	Heroin, Cocaine, LSD, Ludes, Extasy, Weed, Krokodil = DailyDrugPrice ()
	TotalInventory ()
	BuyDrugs (Heroin, Cocaine, LSD, Ludes, Extasy, Weed, Krokodil)
	n += 1

print "\n- Dope stash -\n"
for num in Drugs:
	print num

print "\n- Hoods -\n"
for num in Hoods:
	print num
