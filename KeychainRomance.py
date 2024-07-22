import time
import thumby
import math
import random
import ujson
import gc
import sys

#SAVING THE GAME

thumby.saveData.setName("KeychainRomance")



thumby.display.setFPS(60)
thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)

thumby.display.drawText("check 1", 0, 0, 1)
thumby.display.update()

# print(gc.mem_free())

spriteData = __import__("/Games/KeychainRomance/spritedata")

# print(gc.mem_free())

titleSprite = thumby.Sprite(72, 40, spriteData.titleSprite)
pressSprite = thumby.Sprite(32, 8, spriteData.pressSprite1+spriteData.pressSprite2)
newGameCursor = thumby.Sprite(72, 8, spriteData.newGameCursor1+spriteData.newGameCursor2)
menuCursor = thumby.Sprite(8, 8, spriteData.newGameCursor1)
loadingEyes = thumby.Sprite(72, 23, spriteData.loadingEyes)
callPhone = thumby.Sprite(22, 40, spriteData.callPhone)
phoneFace = thumby.Sprite(16, 21, spriteData.phoneFaceClosed+spriteData.phoneFaceOpen)
textMessages = thumby.Sprite(14, 10, spriteData.textMessage1+spriteData.textMessage2+spriteData.textMessage3)
tinyCursor = thumby.Sprite(5, 5, spriteData.tinyCursor)
tinyCursor2 = thumby.Sprite(5, 5, spriteData.tinyCursor)
goOutSprite = thumby.Sprite(22, 22, spriteData.goOutSprite)
phoneSprite = thumby.Sprite(22, 22, spriteData.phoneSprite)
statusSprite = thumby.Sprite(22, 22, spriteData.statusSprite)
shopSprite = thumby.Sprite(22, 22, spriteData.shopSprite)
tinyArrow = thumby.Sprite(3, 5, spriteData.tinyArrow)
downArrow = thumby.Sprite(5, 3, spriteData.downArrow)

icedCreamSprite = thumby.Sprite(24, 24, spriteData.icedCreamSprite)
greasyChipsSprite = thumby.Sprite(24, 24, spriteData.greasyChipsSprite)
sourPoopiesSprite = thumby.Sprite(24, 24, spriteData.sourPoopiesSprite)
fancyChocolateSprite = thumby.Sprite(24, 24, spriteData.fancyChocolateSprite)
kitchenKnifeSprite = thumby.Sprite(24, 24, spriteData.kitchenKnifeSprite)
combatKnifeSprite = thumby.Sprite(24, 24, spriteData.combatKnifeSprite)
tankBookSprite = thumby.Sprite(24, 24, spriteData.tankBookSprite)
scifiNovelSprite = thumby.Sprite(24, 24, spriteData.scifiNovelSprite)
rockAlbumSprite = thumby.Sprite(24, 24, spriteData.rockAlbumSprite)
rnbAlbumSprite = thumby.Sprite(24, 24, spriteData.rnbAlbumSprite)
toyGunSprite = thumby.Sprite(24, 24, spriteData.toyGunSprite)
toyBugSprite = thumby.Sprite(24, 24, spriteData.toyBugSprite)
realBugSprite = thumby.Sprite(24, 24, spriteData.realBugSprite)
snowGlobeSprite = thumby.Sprite(24, 24, spriteData.snowGlobeSprite)
prettyFlowersSprite = thumby.Sprite(24, 24, spriteData.prettyFlowersSprite)
wildFlowerSprite = thumby.Sprite(24, 24, spriteData.wildFlowerSprite)
fakeSkullSprite = thumby.Sprite(24, 24, spriteData.fakeSkullSprite)
wrestlingTicketSprite = thumby.Sprite(24, 24, spriteData.wrestlingTicketSprite)
rockTicketSprite = thumby.Sprite(24, 24, spriteData.rockTicketSprite)
morbidKnightsSprite = thumby.Sprite(24, 24, spriteData.morbidKnightsSprite)
thumbySprite = thumby.Sprite(24, 24, spriteData.thumbySprite)

del spriteData

del sys.modules['/Games/KeychainRomance/spritedata']

gc.collect()

thumby.display.fill(0)
thumby.display.drawText("Sprites Loaded", 0, 0, 1)
thumby.display.update()

print(gc.mem_free())

gc.collect()


class player:
    def __init__(self, money, totalDates):
        self.money = money
        self.totalDates = totalDates
        
class location:
    def __init__(self, name, label, sprite):
        self.name = name
        self.label = label
        self.sprite = sprite
    def name(self):
        return self.name
    def label(self):
        return self.label
    def sprite(self):
        return self.sprite
        
gc.collect()

thumby.display.fill(0)
thumby.display.drawText("Classes Loaded", 0, 0, 1)
thumby.display.update()

print(gc.mem_free())

gumchBurger = location("Burgers", "Burgers", None)
whipCat = location("Bar", "Bar", None)
localPark = location("Day Park", "Park", None)
rockVenue = location("Rock Venue", "Venue", None)
wrestlingRing = location("Wrestling", "Wrestling", None)
niceRestaurant = location("Restaurant", "Restaurant", None)
girlHome = location("Home", "Home", None)
bigMall = location("Mall", "Mall", None)

locationList = ["Empty", gumchBurger, whipCat, localPark, rockVenue, wrestlingRing, niceRestaurant, girlHome, bigMall]

thumby.display.fill(0)
thumby.display.drawText("Locations Loaded", 0, 0, 1)
thumby.display.update()

class stuff:
    def __init__(self, name, kind, price, sprite):
        self.name = name
        self.type = kind
        self.price = price
        self.sprite = sprite
    def name(self):
        return self.name
    def price(self):
        return self.price
    def sprite(self):
        return self.sprite
        
icedCream = stuff("Iced Cream", "Food", 10, icedCreamSprite)
greasyChips = stuff("Greasy Chips", "Food", 15, greasyChipsSprite)
sourPoopies = stuff("Sour Poopies", "Food", 10, sourPoopiesSprite)
fancyChocolate = stuff("Fancy Gal Choco", "Food", 30, fancyChocolateSprite)
kitchenKnife = stuff("Kitchen Knife", "Stuff", 50, kitchenKnifeSprite)
combatKnife = stuff("Combat Knife", "Stuff", 50, combatKnifeSprite)
tankBook = stuff("Book on Tanks", "Stuff", 50, tankBookSprite)
scifiNovel = stuff("Sci-Fi Novel", "Stuff", 50, scifiNovelSprite)
rockAlbum = stuff("Rock Album", "Stuff", 50, rockAlbumSprite)
rnbAlbum = stuff("R'n'B Album", "Stuff", 50, rnbAlbumSprite)
toyGun = stuff("Toy Gun", "Stuff", 50, toyGunSprite)
toyBug = stuff("Toy Bug", "Stuff", 50, toyBugSprite)
realBug = stuff("Real Bug", "Stuff", 50, realBugSprite)
snowGlobe = stuff("Snowglobe", "Stuff", 50, snowGlobeSprite)
prettyFlowers = stuff("Pretty Flowers", "Stuff", 50, prettyFlowersSprite)
wildFlower = stuff("Wild Flower", "Stuff", 50, wildFlowerSprite)
fakeSkull = stuff("Fake Skull", "Stuff", 50, fakeSkullSprite)
wrestlingTicket = stuff("Wrestling Ticket", "Stuff", 100, wrestlingTicketSprite)
rockTicket = stuff("Rock Ticket", "Stuff", 50, rockTicketSprite)
morbidKnights2 = stuff("MorbidKnights 2", "Stuff", 75, morbidKnightsSprite)
toyThumby = stuff("Thumby", "Stuff", 50, thumbySprite)


currentInventory = {icedCream : 0, greasyChips : 0, sourPoopies : 0, fancyChocolate : 0, kitchenKnife : 0, combatKnife : 0, tankBook : 0, scifiNovel : 0, toyGun : 0, toyBug : 0, realBug : 0, snowGlobe : 0, prettyFlowers : 0, wildFlower : 0, fakeSkull : 0, morbidKnights2 : 0, rockTicket : 0, wrestlingTicket : 0, toyThumby : 0}
shopList = [icedCream, greasyChips, sourPoopies, fancyChocolate, kitchenKnife, combatKnife, tankBook, scifiNovel, rockAlbum, rnbAlbum, toyGun, toyBug, realBug, snowGlobe, fakeSkull, toyThumby, prettyFlowers, wildFlower, rockTicket, morbidKnights2, wrestlingTicket]

class girl:
    def __init__(self, name, sprite, fullSprite, maskSprite, affinity, totalDates, phoneChance, likeLocations, likeGifts, specialGift, relationshipLevel):
        self.name = name
        self.sprite = sprite
        self.fullSprite = fullSprite
        self.maskSprite = maskSprite
        self.affinity = affinity
        self.totalDates = totalDates
        self.phoneChance = phoneChance
        self.likeLocations = likeLocations
        self.likeGifts = likeGifts
        self.specialGift = specialGift
    def name(self):
        return self.name
    def sprite(self):
        return self.sprite
    def fullSprite(self):
        return self.fullSprite
    def maskSprite(self):
        return self.maskSprite

girlNadia = girl("Nadia", None, None, None, 0, 0, 100, (wrestlingRing, girlHome, gumchBurger, niceRestaurant), (icedCream, greasyChips, fancyChocolate, wildFlower, prettyFlowers), wrestlingTicket, 0)
girlGrape = girl("Grape", None, None, None, 0, 0, 100, (whipCat, gumchBurger, rockVenue), (toyGun, combatKnife, rockAlbum, fakeSkull, sourPoopies), tankBook, 0)
girlMarlene = girl("Marlene", None, None, None, 0, 0, 100, (rockVenue, whipCat, gumchBurger), (rockAlbum, rockTicket, greasyChips), wildFlower, 0)
girlAllene = girl("Allene", None, None, None, 0, 0, 100, (localPark, girlHome, niceRestaurant), (toyBug, realBug, scifiNovel, icedCream), snowGlobe, 0)
girlAku = girl("Aku", None, None, None, 0, 0, 100, (bigMall, gumchBurger, rockVenue, wrestlingRing), (rockTicket, wrestlingTicket, combatKnife, realBug, sourPoopies, greasyChips), fakeSkull, 0)
girlRisol = girl("Risol", None, None, None, 0, 0, 100, (niceRestaurant, girlHome, whipCat), (prettyFlowers, scifiNovel, fancyChocolate, rnbAlbum, icedCream), kitchenKnife, 0)
girlGamer = girl("Gamer", None, None, None, 0, 0, 100, (girlHome, gumchBurger, bigMall), (greasyChips, toyThumby, sourPoopies, scifiNovel), morbidKnights2, 0)

    

thumby.display.fill(0)
thumby.display.drawText("Girls Loaded", 0, 0, 1)
thumby.display.update()

player = player(100, 0) # (Money, Dates)
callList = []
recentlyCalled = [None]
currentCall = 0







gc.collect()

def getGirlGraphics(girl):
    if(girl != None):
        girlFullSprite = None
        import Games.KeychainRomance.charactersprites
        spriteName = f"{girl.name}FullSprite"
        fullSprite = getattr(Games.KeychainRomance.charactersprites, spriteName)
        girl.sprite = fullSprite
        if(girl == girlNadia):
            girlFullSprite = thumby.Sprite(44, 80, fullSprite)
        elif(girl == girlGamer):
            girlFullSprite = thumby.Sprite(45, 80, fullSprite)
        elif(girl == girlGrape):
            girlFullSprite = thumby.Sprite(42, 80, fullSprite)
        elif(girl == girlAllene):
            girlFullSprite = thumby.Sprite(72, 80, fullSprite)
        elif(girl == girlMarlene):
            girlFullSprite = thumby.Sprite(60, 80, fullSprite)
        elif(girl == girlAku):
            girlFullSprite = thumby.Sprite(77, 80, fullSprite)
        elif(girl == girlRisol):
            girlFullSprite = thumby.Sprite(57, 80, fullSprite)
        girl.fullSprite = girlFullSprite
        spriteName = f"{girl.name}MaskSprite"
        maskSprite = getattr(Games.KeychainRomance.charactersprites, spriteName)
        girl.maskSprite = maskSprite
        Games.KeychainRomance.charactersprites.clear_data()
        gc.collect()

def getDateScript(script, girlName):
    returnScript = None
    if (girlName == "Nadia"):
        with open("Games/KeychainRomance/nadiascripts.json", "r") as file:
            data = ujson.load(file)
            returnScript = data[script]
            del data
    elif (girlName == "Grape"):
        with open("Games/KeychainRomance/grapescripts.json", "r") as file:
            data = ujson.load(file)
            returnScript = data[script]
            del data
    elif (girlName == "Allene"):
        with open("Games/KeychainRomance/allenescripts.json", "r") as file:
            data = ujson.load(file)
            returnScript = data[script]
            del data
    elif (girlName == "Marlene"):
        with open("Games/KeychainRomance/marlenescripts.json", "r") as file:
            data = ujson.load(file)
            returnScript = data[script]
            del data
    elif (girlName == "Aku"):
        with open("Games/KeychainRomance/akuscripts.json", "r") as file:
            data = ujson.load(file)
            returnScript = data[script]
            del data
    elif (girlName == "Risol"):
        with open("Games/KeychainRomance/risolscripts.json", "r") as file:
            data = ujson.load(file)
            returnScript = data[script]
            del data
    elif (girlName == "Gamer"):
        with open("Games/KeychainRomance/gamerscripts.json", "r") as file:
            data = ujson.load(file)
            returnScript = data[script]
            del data
    else:
        print("Unsuccessful Date Script Grab")
    gc.collect()
    return(returnScript)
    
        
def getLocationGraphics(location):

    if(location != None):
        locationSprite = None
        if((location == gumchBurger) or (location == whipCat)):
            import Games.KeychainRomance.locationdata1
            locationName = f"{location.label}Sprite"
            locationSprite = getattr(Games.KeychainRomance.locationdata1, locationName)
            location.sprite = locationSprite
            Games.KeychainRomance.locationdata1.clear_data()
        elif((location == wrestlingRing) or (location == niceRestaurant)):
            import Games.KeychainRomance.locationdata2
            locationName = f"{location.label}Sprite"
            locationSprite = getattr(Games.KeychainRomance.locationdata2, locationName)
            location.sprite = locationSprite
            Games.KeychainRomance.locationdata2.clear_data()
        elif((location == rockVenue) or (location == localPark)):
            import Games.KeychainRomance.locationdata3
            locationName = f"{location.label}Sprite"
            locationSprite = getattr(Games.KeychainRomance.locationdata3, locationName)
            location.sprite = locationSprite
            Games.KeychainRomance.locationdata3.clear_data()
        elif((location == girlHome) or (location == bigMall)):
            import Games.KeychainRomance.locationdata4
            locationName = f"{location.label}Sprite"
            locationSprite = getattr(Games.KeychainRomance.locationdata4, locationName)
            location.sprite = locationSprite
            Games.KeychainRomance.locationdata4.clear_data()
    gc.collect()
        



def waitForInput():
    okToPress = False
    while(1):
        if(thumby.actionPressed() is False):
            okToPress = True
        if((okToPress is True) and thumby.actionPressed()):
            break

def narrationText(currentString):
    textCounter = 0
    printSpeed = 1
    textXPos = 1
    textYPos = 1
    xLimit = 72 #Point at which the text wraps
    yLimit = 36 #Lowest Point of the screen that can be written to
    currentWord = 0
    while(1):
        if(currentWord < len(currentString)):
            if(currentWord >= (len(currentString))):
                waitForInput()
                break
            elif(textYPos > yLimit):
                textYPos = 1
                waitForInput()
                thumby.display.fill(0)
            elif((len(currentString[currentWord]) * 4) + textXPos > xLimit):
                textXPos = 1
                textYPos += 6
            else:
                for letter in currentString[currentWord]:
                    snip = thumby.display.drawText(currentString[currentWord][textCounter], textXPos, textYPos, 1)
                    textXPos += 4
                    textCounter += 1
                    thumby.display.update()
                snip = thumby.display.drawText(" ", textXPos, textYPos, 1)
                if(currentWord < len(currentString)):
                    textXPos += 4
                    textCounter = 0
                    currentWord += 1
        elif(currentWord >= len(currentString)):
            waitForInput()
            break

def introductionAnimation(girl):
    girlSprite = girl.fullSprite
    color = 1
    circles = 6
    speed = 11
    girlx = (72 - girlSprite.width)//2
    t0 = time.ticks_ms()
    bobRateY = 1000 #set the rate of the animation change
    bobRangeY = ((girlSprite.height / 2) - 20) #set the amount of pixels to move
    bobOffsetY = int((math.sin(t0 / bobRateY) * bobRangeY)) - 20
    for c in range (0, circles):
        x = random.randrange(72)
        y = random.randrange(40)
        for r in range (0, 83):
            if (r % speed == 0):    
                thumby.display.drawLine(x-r+1,y,x+r-1,y,color)
                for i in range(1,r):
                    a = int(math.sqrt(r*r-i*i)) # Pythagoras!
                    thumby.display.drawLine(x-a,y+i,x+a,y+i,color) # Lower half
                    thumby.display.drawLine(x-a,y-i,x+a,y-i,color) # Upper half
                if (c >= 5):
                    thumby.display.blit(girl.sprite, girlx, 0, girlSprite.width, girlSprite.height, 0, 0, 0)
                thumby.display.update()
        if (speed > 2):
            speed -= 2
        if color == 1:
            color = 0
        else:
            color = 1
    while(1):
        t0 = time.ticks_ms()
        bobOffsetY = int((math.sin(t0 / bobRateY) * bobRangeY)) - 20
        thumby.display.fill(0)
        thumby.display.blit(girl.sprite, girlx, bobOffsetY, girlSprite.width, girlSprite.height, 0, 0, 0)
        thumby.display.update()
        if (thumby.actionPressed()):
            break
    for n in range (0, girlx):
        girlx += 1
        t0 = time.ticks_ms()
        bobOffsetY = int((math.sin(t0 / bobRateY) * bobRangeY)) - 20
        thumby.display.fill(0)
        thumby.display.blit(girl.sprite, girlx, bobOffsetY, girlSprite.width, girlSprite.height, 0, 0, 0)
        thumby.display.update()
    thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
    tinyCursor2.y = 0
    tinyCursor2.x = random.randrange(23)
    tinyCursor.y = 0
    tinyCursor.x = random.randrange(23)
    okToPress = False
    while(1):
        if(thumby.actionPressed() is False):
            okToPress = True
        t0 = time.ticks_ms()
        bobOffsetY = int((math.sin(t0 / bobRateY) * bobRangeY)) - 20
        thumby.display.fill(0)
        thumby.display.blit(girl.sprite, girlx, bobOffsetY, girlSprite.width, girlSprite.height, 0, 0, 0)
        if(tinyCursor.y < 41):
            tinyCursor.y += 1
        else:
            tinyCursor.y = 0
            tinyCursor.x = random.randrange(23)
        if(tinyCursor2.y < 41):
            tinyCursor2.y += 2
        else:
            tinyCursor2.y = 0
            tinyCursor2.x = random.randrange(23)
        thumby.display.drawSprite(tinyCursor)
        thumby.display.drawSprite(tinyCursor2)
        thumby.display.drawFilledRectangle(0, 32, 72, 8, 0)
        thumby.display.drawText(girl.name.upper(), 0, 33, 1)
        thumby.display.update()
        if (thumby.actionPressed() and okToPress is True):
            break
    circles = 2
    speed = 6
    for c in range (0, circles):
        x = random.randrange(72)
        y = random.randrange(40)
        for r in range (0, 83):
            if (r % speed == 0):    
                thumby.display.drawLine(x-r+1,y,x+r-1,y,color)
                for i in range(1,r):
                    a = int(math.sqrt(r*r-i*i)) # Pythagoras!
                    thumby.display.drawLine(x-a,y+i,x+a,y+i,color) # Lower half
                    thumby.display.drawLine(x-a,y-i,x+a,y-i,color) # Upper half
                if (c == 0):
                    thumby.display.blit(girl.sprite, girlx, bobOffsetY, girlSprite.width, girlSprite.height, 0, 0, 0)
                    thumby.display.drawFilledRectangle(0, 32, 72, 8, 0)
                    thumby.display.drawText(girl.name.upper(), 0, 33, 1)
                thumby.display.update()
        if color == 1:
            color = 0
        else:
            color = 1

def drawGal(girl):
    thumby.display.fill(0)
    girlmask = girl.maskSprite
    girlsprite = girl.fullSprite
    girlsprite.x = int((thumby.display.width) - ((girlsprite.width - 32) / 2) - (32)) #characters x position
    thumby.display.drawSprite(girlsprite)
    thumby.display.drawFilledRectangle(0, 0, 42, 40, 0)

def dateText(girl, currentString):
    thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
    textCounter = 0
    printSpeed = 1
    textXPos = 1
    textYPos = 1
    xLimit = 42 #Point at which the text wraps
    yLimit = 36 #Lowest Point of the screen that can be written to
    currentWord = 0
    drawGal(girl)
    while(1):
        if(currentWord < (len(currentString))):
            if(len(currentString[currentWord]) > 10):
                chunkOne = currentString[currentWord][0:9] + "-"
                chunkTwo = currentString[currentWord][9:len(currentString[currentWord])]
                currentString.insert(currentWord, chunkTwo)
                currentString.insert(currentWord, chunkOne)
                del currentString[currentWord + 2]
            if(currentWord >= (len(currentString))):
                waitForInput()
                break
            elif(textYPos > yLimit):
                textYPos = 1
                waitForInput()
                thumby.display.drawFilledRectangle(0, 0, 42, 36, 0)
            elif((len(currentString[currentWord]) * 4) + textXPos > xLimit):
                textXPos = 1
                textYPos += 6
            else:
                for letter in currentString[currentWord]:
                    snip = thumby.display.drawText(currentString[currentWord][textCounter], textXPos, textYPos, 1)
                    textXPos += 4
                    textCounter += 1
                    thumby.display.update()
                snip = thumby.display.drawText(" ", textXPos, textYPos, 1)
                if(currentWord < len(currentString)):
                    textXPos += 4
                    textCounter = 0
                    currentWord += 1
        elif(currentWord >= (len(currentString))):
            waitForInput()
            break

def waitForInputPhone(phoneScreen):
    okToPress = False
    while(1):
        if(thumby.actionPressed() is False):
            isTexting(phoneScreen)
            thumby.display.update()
            okToPress = True
        if((okToPress is True) and thumby.actionPressed()):
            break
        
def phoneCall(currentString, phoneScreen):
    textCounter = 0
    printSpeed = 1
    textXPos = 1
    textYPos = 1
    xLimit = 42 #Point at which the text wraps
    yLimit = 36 #Lowest Point of the screen that can be written to
    currentWord = 0
    thumby.display.drawFilledRectangle(0, 0, 42, 40, 0)
    thumby.display.drawSprite(callPhone)
    while(1):
        if(currentWord < (len(currentString))):
            if(len(currentString[currentWord]) > 10):
                chunkOne = currentString[currentWord][0:9] + "-"
                chunkTwo = currentString[currentWord][9:len(currentString[currentWord])]
                currentString.insert(currentWord, chunkTwo)
                currentString.insert(currentWord, chunkOne)
                del currentString[currentWord + 2]
            if(currentWord >= (len(currentString))):
                waitForInputPhone(phoneScreen)
                break
            elif(textYPos > yLimit):
                textYPos = 1
                waitForInputPhone(phoneScreen)
                thumby.display.drawFilledRectangle(0, 0, 42, 36, 0)
            elif((len(currentString[currentWord]) * 4) + textXPos > xLimit):
                textXPos = 1
                textYPos += 6
            else:
                for letter in currentString[currentWord]:
                    snip = thumby.display.drawText(currentString[currentWord][textCounter], textXPos, textYPos, 1)
                    textXPos += 4
                    textCounter += 1
                    isTexting(phoneScreen)
                    thumby.display.update()
                snip = thumby.display.drawText(" ", textXPos, textYPos, 1)
                if(currentWord < len(currentString)):
                    textXPos += 4
                    textCounter = 0
                    currentWord += 1
        elif(currentWord >= (len(currentString))):
            waitForInputPhone(phoneScreen)
            break
        thumby.display.update()
        


def eventHandler(event, girl, location): #event[action][sentence][textCounter]
    gc.collect()
    print(gc.mem_free())
    getGirlGraphics(girl)
    getLocationGraphics(location)
    action = 0
    sentence = 0
    textCounter = 0
    # printSpeed = 1
    # textXPos = 1
    # textYPos = 1
    # xLimit = 72 #Point at which the text wraps
    # yLimit = 36 #Lowest Point of the screen that can be written to
    currentString = event[action][sentence].split()
    chosenGift = None
    thumby.display.fill(0)
    thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
    snip = thumby.display.drawText("", 0, 0, 1)
    while(1):
        if(type(event[action][sentence]) == int):
            while(1):
                action += 1
                if(event[action][sentence] == "%MERGE%"):
                    break
        elif(event[action][sentence] == "%MERGE%"):
                action += 1
        elif(event[action][sentence] == "%NARRATION%"):
            while(1):
                action += 1
                thumby.display.fill(0)
                if(type(event[action][sentence]) == str):
                    if(event[action][sentence][textCounter] != "%"):
                        currentString = event[action][sentence].split()
                        narrationText(currentString)
                else:
                    break
                if(event[action][sentence][textCounter] == "%"):
                    break
        elif(event[action][sentence] == "%DATETEXT%"):
            while(1):
                action += 1
                if(type(event[action][sentence]) == str):
                    if(event[action][sentence][textCounter] != "%"):
                        currentString = event[action][sentence].split()
                        dateText(girl, currentString)
                else:
                    break
                if(event[action][sentence][textCounter] == "%"):
                    break
        elif(event[action][sentence] == "%TEXTING%"):
            while(1):
                action += 1
                if(event[action][sentence][textCounter] != "%"):
                    currentString = event[action][sentence].split()
                    phoneCall(currentString, textMessages)
                elif(event[action][sentence][textCounter] == "%"):
                    break
        elif(event[action][sentence] == "%PHONECALL%"):
            while(1):
                action += 1
                if(event[action][sentence][textCounter] != "%"):
                    currentString = event[action][sentence].split()
                    phoneCall(currentString, phoneFace)
                elif(event[action][sentence][textCounter] == "%"):
                    break
        elif(event[action][sentence] == "%LOCATION%"):
            locationViewer(location, None)
            action += 1
        elif(event[action][sentence] == "%LOCATIONGIRL%"):
            locationViewer(location, girl)
            action += 1
        elif(event[action][sentence] == "%CIRCLEMEET%"):
            action += 1
            introductionAnimation(girl)
            thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
        elif(event[action][sentence] == "%CHOICE%"):
            action += 1
            listOfChoices = []
            while(type(event[action][sentence]) != int):
                listOfChoices.append(event[action][sentence])
                action += 1
            decision = makeChoice(*listOfChoices)
            thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
            while(1):
                if(event[action][sentence] == decision):
                    action += 1
                    break
                action += 1
        elif(event[action][sentence] == "%ADD1%"):
            girl.affinity += 1
            action += 1
        elif(event[action][sentence] == "%ADD2%"):
            girl.affinity += 2
            action += 1
        elif(event[action][sentence] == "%GIFT%"):
            chosenGift = giveGift()
            action += 1
        elif(event[action][sentence] == "%DONE%"):
            if(girl != None):
                girl.fullSprite = None
                girl.sprite = None
                girl.maskSprite = None
            if(location != None):
                location.sprite = None
            moduleName = ('Games.KeychainRomance.locationdata1', 'Games.KeychainRomance.locationdata2', 'Games.KeychainRomance.datescripts1', 'Games.KeychainRomance.datescripts2', 'Games.KeychainRomance.datescripts3', 'Games.KeychainRomance.datescripts4', 'Games.KeychainRomance.charactersprites')
            for i in moduleName:
                if i in sys.modules:
                    del sys.modules[i]
                    print(f"Successful {i} Deletion")
            player.money += 5
            gc.collect()
            saveGame()
            if(chosenGift != None):
                return(chosenGift)
            break
        else:
            print("Incorrect script syntax!")
            thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
            thumby.display.drawText("Error.", 0, 0, 1)
            thumby.display.drawText("Let Dev know!", 0, 7, 1)
            thumby.display.update()
            time.sleep(2)
            while(1):
                if(thumby.actionPressed()):
                    break
            break
                
        thumby.display.update()

def displayStats(girl):
    getGirlGraphics(girl)
    drawGal(girl)
    thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
    thumby.display.drawText(girl.name, 1, 1, 1)
    thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
    thumby.display.drawText("Care:   " + str(girl.affinity), 1, 29, 1)
    thumby.display.drawText("Dates:  " + str(girl.totalDates), 1, 35, 1)
    thumby.display.update()
    waitForInput()
    thumby.display.drawFilledRectangle(0, 0, 42, 40, 0)
    if(girl != None):
        girl.fullSprite = None
        girl.sprite = None
        girl.maskSprite = None
        print("sprites clear")
    moduleName = ('Games.KeychainRomance.locationdata1', 'Games.KeychainRomance.locationdata2', 'Games.KeychainRomance.locationdata3', 'Games.KeychainRomance.locationdata4', 'Games.KeychainRomance.datescripts1', 'Games.KeychainRomance.datescripts2', 'Games.KeychainRomance.datescripts3', 'Games.KeychainRomance.datescripts4', 'Games.KeychainRomance.charactersprites')
    for i in moduleName:
        if i in sys.modules:
            del sys.modules[i]
            print(f"Successful {i} Deletion")

def getAverageGirlAffinity():
    affinityCollector = 0
    for gal in callList:
        affinityCollector += gal.affinity
    affinityCollector = affinityCollector/len(callList)
    return affinityCollector

def screen_wipe():
    wipeHeight = 0
    for i in range(20):
        thumby.display.drawFilledRectangle(0, wipeHeight, 72, 2, 1)
        wipeHeight += 2
        thumby.display.update()
        # time.sleep(0.005)
    wipeHeight = 0
    for i in range(20):
        thumby.display.drawFilledRectangle(0, wipeHeight, 72, 2, 0)
        wipeHeight += 2
        thumby.display.update()
    time.sleep(0.5)


def loadGame():
    if (thumby.saveData.hasItem("hasSave")):
        namelist = thumby.saveData.getItem("listOfGirls")
        listOfAllGirls = [girlNadia, girlGrape, girlAllene, girlMarlene, girlAku, girlRisol, girlGamer]
        for gal in listOfAllGirls:
            if gal.name in namelist:
                callList.append(gal)
        girlNadia.affinity = int(thumby.saveData.getItem("nadiaAffinity"))
        girlGrape.affinity = int(thumby.saveData.getItem("grapeAffinity"))
        girlAllene.affinity = int(thumby.saveData.getItem("alleneAffinity"))  
        girlMarlene.affinity = int(thumby.saveData.getItem("marleneAffinity"))
        girlAku.affinity = int(thumby.saveData.getItem("akuAffinity"))
        girlRisol.affinity = int(thumby.saveData.getItem("risolAffinity"))
        girlGamer.affinity = int(thumby.saveData.getItem("gamerAffinity"))
        player.money = int(thumby.saveData.getItem("playerMoney"))
        player.totalDates = int(thumby.saveData.getItem("playerDates"))
        print("Loaded")

def saveGame():
    thumby.saveData.setItem("hasSave", True)
    namelist = []
    for gal in callList:
        namelist.append(gal.name)
    itemList = {}
    thumby.saveData.setItem("listOfGirls", namelist)
    for key, value in currentInventory.items():
        itemList[key.name] = value
    thumby.saveData.setItem("inventory", itemList)
    thumby.saveData.setItem("nadiaAffinity", girlNadia.affinity)
    thumby.saveData.setItem("grapeAffinity", girlGrape.affinity)
    thumby.saveData.setItem("alleneAffinity", girlAllene.affinity)
    thumby.saveData.setItem("marleneAffinity", girlMarlene.affinity)
    thumby.saveData.setItem("akuAffinity", girlAku.affinity)
    thumby.saveData.setItem("risolAffinity", girlRisol.affinity)
    thumby.saveData.setItem("gamerAffinity", girlGamer.affinity)
    thumby.saveData.setItem("playerMoney", player.money)
    thumby.saveData.setItem("playerDates", player.totalDates)
    
    thumby.saveData.save()




def isTexting(phoneScreen):
    ms0 = (time.ticks_ms() // 650)
    textMessages.x = 54
    textMessages.y = 7
    phoneFace.x = 53
    phoneFace.y = 6
    phoneScreen.setFrame(ms0)
    thumby.display.drawSprite(phoneScreen)
    
        
def giveGift():
    for item in currentInventory:
        if currentInventory[item] != 0:
            isInventoryEmpty = False
            break
        else:
            isInventoryEmpty = True
    if isInventoryEmpty is False:
        itemNames = [key for key, value in currentInventory.items() if value != 0]
        choiceCursorPosition = 0
        okToPress = False
        tinyCursor.x = 1
        tinyCursor.y = 22
        currentShop = 0
        while(1):
            thumby.display.fill(0)
            thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
            thumby.display.drawText("Give A Gift?", 1, 1, 1)
            if(thumby.actionPressed() == 0):
                okToPress = True
            if(thumby.buttonU.justPressed() and currentShop >= 1):
                currentShop -= 1
            if(thumby.buttonD.justPressed() and currentShop < len(itemNames) - 1):
                currentShop += 1
            if(len(itemNames) > 1 and currentShop > 1):
                thumby.display.drawText(stuff.name(itemNames[currentShop - 2]), 8, 10, 1)
            if(len(itemNames) >= 2 and currentShop >= 1):
                thumby.display.drawText(stuff.name(itemNames[(currentShop - 1)]), 8, 16, 1)
            thumby.display.drawText(stuff.name(itemNames[currentShop]), 8 , 22, 1)
            if(len(itemNames) >= 2 and currentShop < (len(itemNames) - 1)):
                thumby.display.drawText(stuff.name(itemNames[(currentShop + 1)]), 8, 28, 1)
            if(len(itemNames) > 1 and currentShop < (len(itemNames) - 2)):
                thumby.display.drawText(stuff.name(itemNames[currentShop + 2]), 8, 34, 1)
            if(len(itemNames) == 1):
                thumby.display.drawText(stuff.name(itemNames[currentShop]), 8, 22, 1)
            thumby.display.drawSprite(tinyCursor)
            if(okToPress is True):
                if(thumby.buttonB.pressed()):
                    screen_wipe()
                    chosenGift = None
                    break
                if(thumby.buttonA.pressed()):
                    chosenGift = itemNames[currentShop]
                    currentInventory[chosenGift] -= 1
                    screen_wipe()
                    thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                    break
            thumby.display.update()
        thumby.display.setFont("/lib/font5x7.bin", 3, 5, 1)
        return(chosenGift)
    else:
        print("Broke Ass")
        return(None)

def shopYesNo(item):
    choiceCursorPosition = 0
    okToPress = False
    menuCursor.y = 21
    item.sprite.x = 44
    item.sprite.y = 12
    while(1):
        thumby.display.fill(0)
        thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)    
        thumby.display.drawText("Buy This?", 1, 1, 1)
        thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1) 
        thumby.display.drawText("MONEY: " + str(player.money), 1, 9, 1)
        thumby.display.drawText("COST: " + str(item.price), 1, 15, 1)
        thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
        thumby.display.drawText("Yes", 10, 21, 1)
        thumby.display.drawText("No", 10, 29, 1)
        menuCursor.x = 0
        thumby.display.drawSprite(menuCursor)
        thumby.display.drawSprite(item.sprite)
        thumby.display.update()
        if(thumby.actionPressed() == 0):
            okToPress = True
        if(okToPress is True):
            if(thumby.buttonD.justPressed() and choiceCursorPosition == 0):
                choiceCursorPosition += 1
                menuCursor.y += 8
            if(thumby.buttonU.justPressed() and choiceCursorPosition == 1):
                choiceCursorPosition -= 1
                menuCursor.y -= 8
            if(thumby.buttonA.pressed() and choiceCursorPosition == 0):
                if(player.money >= item.price):
                    player.money -= item.price
                    currentInventory[item] += 1
                    okToPress = False
                else:
                    thumby.display.fill(0)
                    thumby.display.drawText("You can't", 1, 1, 1)
                    thumby.display.drawText("afford this.", 1, 9, 1)
                    thumby.display.update()
                    waitForInput()
                    okToPress = False
            if(thumby.buttonB.pressed() or (thumby.buttonA.pressed() and choiceCursorPosition == 1)):
                print(choiceCursorPosition)
                print("backing out")
                break
    # return choiceCursorPosition
        
def chooseLocation(): #choose from locationList
    choiceCursorPosition = 0
    okToPress = False
    tinyCursor.x = 1
    tinyCursor.y = 17
    currentLocation = 1
    while(1):
        thumby.display.fill(0)
        thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
        if(thumby.actionPressed() == 0):
            okToPress = True
        if(thumby.buttonU.justPressed() and currentLocation >= 2):
            currentLocation -= 1
        if(thumby.buttonD.justPressed() and currentLocation < len(locationList) - 1):
            currentLocation += 1
        if(len(locationList) > 2 and currentLocation > 2):
            thumby.display.drawText(stuff.name(locationList[currentLocation - 2]), 8, 1, 1)
        if(len(locationList) >= 3 and currentLocation >= 2):
            thumby.display.drawText(stuff.name(locationList[(currentLocation - 1)]), 8, 9, 1)
        thumby.display.drawText(stuff.name(locationList[currentLocation]), 8 , 17, 1)
        if(len(locationList) >= 3 and currentLocation < (len(locationList) - 1)):
            thumby.display.drawText(stuff.name(locationList[(currentLocation + 1)]), 8, 25, 1)
        if(len(locationList) > 2 and currentLocation < (len(locationList) - 2)):
            thumby.display.drawText(stuff.name(locationList[currentLocation + 2]), 8, 33, 1)
        if(len(locationList) == 1):
            thumby.display.drawText(stuff.name(locationList[currentLocation]), 8, 17, 1)
        if(len(locationList) > 1):
            thumby.display.drawSprite(tinyCursor)
        if(okToPress is True):
            if(thumby.buttonA.pressed()):
                chosenLocation = locationList[currentLocation]
                screen_wipe()
                break
        thumby.display.update()
    return(chosenLocation)
    

    
def makeChoice(*choices):
    screenDivision = 40 // (len(choices) + 1)
    choiceCursorPosition = 1
    okToPress = False
    menuCursor.y = screenDivision - 3
    thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)        
    while(1):
        textYPos = screenDivision - 3
        thumby.display.fill(0)
        for choice in choices:
            thumby.display.drawText(choice, 10, textYPos, 1)
            textYPos += screenDivision
        if(thumby.actionPressed() == 0):
            okToPress = True
        if(okToPress):
            if(thumby.buttonD.justPressed() and choiceCursorPosition < len(choices)):
                choiceCursorPosition += 1
                menuCursor.y += screenDivision
            if(thumby.buttonU.justPressed() and choiceCursorPosition > 1):
                choiceCursorPosition -= 1
                menuCursor.y -= screenDivision
            if(thumby.buttonA.pressed()):
                break
         
        thumby.display.drawSprite(menuCursor)
        thumby.display.update()
    return choiceCursorPosition
    

def locationViewer(locationChoice, girl):
    locationImage = locationChoice.sprite
    if girl != None:
        girlSprite = girl.sprite
        girlFull = girl.fullSprite
        girlMask = decompressImage(girl.maskSprite)
    if locationChoice.label == "Wrestling" or locationChoice.label == "Burgers" or locationChoice.label == "Restaurant" or locationChoice.label == "Mall" or locationChoice.label == "Home":
        locationImage = thumby.Sprite(144, 80, decompressImage(locationImage))
    else:
        locationImage = thumby.Sprite(144, 80, locationImage)
    isViewing = 1
    girlX = 0
    okToPress = False
    while(isViewing == 1):
        if(thumby.actionPressed() == 0):
            okToPress = True
        if(thumby.actionPressed() and okToPress is True):
            isViewing = 0
        t0 = time.ticks_ms() #get time in milliseconds
        thumby.display.fill(0) #fills the canvas in with black
        bobRateY = 1000 #set the rate of the animation change
        bobRangeY = ((locationImage.height / 2) - 20) #set the amount of pixels to move
        bobOffsetY = math.sin(t0 / bobRateY) * bobRangeY
        bobRateX = 2000 #set the rate of the animation change
        bobRangeX = ((locationImage.width / 2) - 36) #set the amount of pixels to move
        bobOffsetX = math.sin(t0 / bobRateX) * bobRangeX
        locationImage.x = int(round(thumby.display.width/2) - (locationImage.width/2) + bobOffsetX)
        locationImage.y = int(round((thumby.display.height/2) - (locationImage.height/2) + bobOffsetY))
        # Display the bitmap using bitmap data, position, and bitmap dimensions
        thumby.display.drawSprite(locationImage)
        if(girl != None):
            girlX = int(round(bobOffsetX/2) + (440/girlFull.width))
            thumby.display.blitWithMask(girlSprite, girlX, locationImage.y, girlFull.width, 80, 0, 0, 0, girlMask)
        thumby.display.update()
    screen_wipe()


#Image Decompression
def decompressImage(array):
    counter = None
    currentNumber = None
    newArray = ([0])

    for index, i in enumerate(array):
        if index == 0 or (index % 2) == 0:
            counter = i
        if index % 2 != 0:
            currentNumber = i
            for x in range(counter):
                newArray.append(currentNumber)
    
    newArray.pop(0)
    return bytearray(newArray)

def shiftIcons(leftIcon, centerIcon, rightIcon, undrawnOption, direction):
    undrawnOption.y = 14
    if direction == 0:
        offestDirection = -1
        undrawnOption.x = 89
    else:
        offestDirection = 1
        undrawnOption.x = -39
    for i in range(32):
        thumby.display.fill(0)
        tinyArrow.mirrorX = 0
        tinyArrow.x = 1
        tinyArrow.y = 2
        thumby.display.drawSprite(tinyArrow)
        tinyArrow.mirrorX = 1
        tinyArrow.x = 68
        thumby.display.drawSprite(tinyArrow)
        leftIcon.x += offestDirection
        centerIcon.x += offestDirection
        rightIcon.x += offestDirection
        undrawnOption.x += offestDirection
        thumby.display.drawSprite(leftIcon)
        thumby.display.drawSprite(centerIcon)
        thumby.display.drawSprite(rightIcon)
        thumby.display.drawSprite(undrawnOption)
        thumby.display.update()




print(gc.mem_free())

#--------------------------------------------------------------------------------------------------------------------
#
#                               THE GAME LOOP STARTS HERE
#
#--------------------------------------------------------------------------------
gamestate = 1 #Initializes the gamestate as title
returnToMenu = False
initiateEvent = False

while(1):
    
    
    # with open("Saves/SavedGame/persistent.json", "r") as file:
    #     saveData = ujson.load(file)
    #     testaffinity = saveData["nadiaAffinity"]
    #     del saveData
    #     print(testaffinity)
    pressFlash = True
    isNewGame = False # Make this true later
    menuCursorInit = True
    menuCursorPosition = 0
    blackoutScreen = True
    loadNewCursor = True
    
    
    # TITLE SCREEN
    while(gamestate == 1):
        
        thumby.display.fill(0)
        titleSprite.x = 0
        titleSprite.y = 0
        thumby.display.drawSprite(titleSprite)

        if(thumby.actionPressed()):
            screen_wipe()
            gamestate = 2
            del titleSprite
            break
        ms0 = (time.ticks_ms() // 650)
        pressSprite.x = 14
        pressSprite.y = 32
        pressSprite.setFrame(ms0)
        thumby.display.drawSprite(pressSprite)
        thumby.display.update()
        
        
    # LOAD OR NEW GAME SCREEN
    while(gamestate == 2):
        
        #LOAD GAME
        

        if(thumby.actionPressed() and loadNewCursor is True):
            loadGame()
            
            returnToMenu = True
            isNewGame = False
            gamestate = 3
            
            
        # NEW GAME
        if(thumby.actionPressed() and loadNewCursor is False):
            gamestate = 3
            
            
        if(thumby.buttonU.pressed()):
            loadNewCursor = True
        if(thumby.buttonD.pressed()):
            loadNewCursor = False
        thumby.display.fill(0)
        thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
        if(loadNewCursor is True):
            newGameCursor.x = 0
            newGameCursor.y = 24

        elif(loadNewCursor is False):
            newGameCursor.x = 0
            newGameCursor.y = 32

        loadingEyes.x = 0
        loadingEyes.y = 0
        thumby.display.drawSprite(loadingEyes)
        ms0 = (time.ticks_ms() // 500)
        newGameCursor.setFrame(ms0)
        thumby.display.drawSprite(newGameCursor)
        thumby.display.drawText("LOAD GAME", 9, 24, 1)
        thumby.display.drawText("NEW GAME", 13, 32, 1)
        thumby.display.update()

        
    #MENU SCREEN
    while(gamestate == 3):
        gc.collect()
        print(gc.mem_free())
        menuOptions = (goOutSprite, phoneSprite, shopSprite, statusSprite)
        undrawnOption = None
        currentOption = 0
        thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
        if(isNewGame == True):
            if(blackoutScreen is True):
                blackoutScreen = False
                thumby.display.fill(0)
            introductionText = (["%NARRATION%"], ["Welcome to Keychain Romance!"], ["Try talking to some girls and making friends!"], ["Talking to girls often will open up new activities and locations!"], ["First, try selecting 'GO OUT' to go outside and walk around."], ["If you're lucky, you may run into someone who will want to hang out with you!"], ["If you want to hang out with them again, try contacting them on the 'PHONE'!"], ["But remember..."], ["People have their own lives and may not have time to see you at the moment!"], ["You might also want to go to the 'SHOP's and buy some gifts for your new friends!"], ["That's about it, so get out there and make an impact!"], ["Good luck ..."], ["and..."], ["Believe in yourself!"], ["%DONE%"])
            eventHandler(introductionText, None, None)
            del introductionText
            isNewGame = False
            okToPress = False
             
        if(returnToMenu is True):
            gc.collect()
            print(gc.mem_free())
            screen_wipe()
            returnToMenu = False
            okToPress = False
         
        while(1):
                
            gc.collect()
            thumby.display.fill(0)
            ms0 = (time.ticks_ms() // 300)
            if ms0 % 2 == 0:
                thumby.display.drawRectangle(23, 12, 26, 26, 1)
            menuOptions[currentOption].x = 25
            menuOptions[currentOption].y = 14
            tinyArrow.mirrorX = 0
            tinyArrow.x = 1
            tinyArrow.y = 2
            thumby.display.drawSprite(tinyArrow)
            tinyArrow.mirrorX = 1
            tinyArrow.x = 68
            thumby.display.drawSprite(tinyArrow)
            if(thumby.dpadPressed() is False):
                okToPress = True
            
            if currentOption == 0:
                thumby.display.drawText("GO", 30, 2, 1)
            elif currentOption == 1:
                thumby.display.drawText("PHONE", 21, 2, 1)
            elif currentOption == 2:
                thumby.display.drawText("SHOP", 24, 2, 1)
            elif currentOption == 3:
                thumby.display.drawText("STATUS", 18, 2, 1)
            
            if currentOption == 0:
                menuOptions[currentOption + 3].x = -7
                menuOptions[currentOption + 3].y = 14
                thumby.display.drawSprite(menuOptions[currentOption + 3])
                leftIcon = menuOptions[currentOption + 3]
            else:
                menuOptions[currentOption - 1].x = -7
                menuOptions[currentOption - 1].y = 14
                thumby.display.drawSprite(menuOptions[currentOption - 1])
                leftIcon = menuOptions[currentOption - 1]
            thumby.display.drawSprite(menuOptions[currentOption])
            centerIcon = menuOptions[currentOption]
            if currentOption == 3:
                menuOptions[currentOption - 3].x = 57
                menuOptions[currentOption - 3].y = 14
                thumby.display.drawSprite(menuOptions[currentOption - 3])
                rightIcon = menuOptions[currentOption - 3]
            else:
                menuOptions[currentOption + 1].x = 57
                menuOptions[currentOption + 1].y = 14
                thumby.display.drawSprite(menuOptions[currentOption + 1])
                rightIcon = menuOptions[currentOption + 1]
            # onScreenIcons = (leftIcon, centerIcon, rightIcon)
            if(okToPress is True):
                if thumby.buttonR.pressed():
                    okToPress = False
                    onScreenIcons = (leftIcon, centerIcon, rightIcon)
                    for item in menuOptions:
                        if item not in onScreenIcons:
                            undrawnOption = item
                    shiftIcons(leftIcon, centerIcon, rightIcon, undrawnOption, 0) #Zero Shifts Left
                    if currentOption == 3:
                        currentOption = 0
                    else:
                        currentOption += 1
                elif thumby.buttonL.pressed():
                    okToPress = False
                    onScreenIcons = (leftIcon, centerIcon, rightIcon)
                    for item in menuOptions:
                        if item not in onScreenIcons:
                            undrawnOption = item
                    shiftIcons(leftIcon, centerIcon, rightIcon, undrawnOption, 1) #One Shifts Right
                    if currentOption == 0:
                        currentOption = 3
                    else:
                        currentOption -= 1
                elif(thumby.buttonA.pressed() and currentOption == 0):
                    gamestate = 4
                    break
                elif(thumby.buttonA.pressed() and currentOption == 1):
                    gamestate = 5
                    currentCall = 0
                    initiateEvent = True
                    break
                elif(thumby.buttonA.pressed() and currentOption == 2):
                    gamestate = 6
                    initiateEvent = True
                    break
                elif(thumby.buttonA.pressed() and currentOption == 3):
                    gamestate = 7
                    initiateEvent = True
                    break
            thumby.display.update()

        
        
    #MEET OPTION
    while(gamestate == 4):
        
        # diceRoll = (time.ticks_ms() % 100)
        

#--------------------------------------------------------------------------------------------------------------------
#
#                               MEETING SCENES
#
#--------------------------------------------------------------------------------------------------------------------
       
        
        if(returnToMenu is False):
            
            # TEST SITUATION
            chosenGirl = girlRisol
            scriptName = f"{chosenGirl.name}Bar3"
            eventString = getDateScript(scriptName, chosenGirl.name)
            eventHandler(eventString, chosenGirl, whipCat)
            returnToMenu = True
            gamestate = 3
            break
            
            
            
            if(girlNadia.affinity == 0):
                chosenGirl = girlNadia
                scriptName = f"{chosenGirl.name}Meeting"
                eventString = getDateScript(scriptName, chosenGirl.name)
                eventHandler(eventString, chosenGirl, localPark)
                callList.append(girlNadia)
                locationList.append(localPark)
                girlNadia.affinity += 1
                saveGame()
                returnToMenu = True
                gamestate = 3
            elif(girlGrape.affinity == 0 and player.totalDates >= 1):
                chosenGirl = girlGrape
                scriptName = f"{chosenGirl.name}Meeting"
                eventString = getDateScript(scriptName, chosenGirl.name)
                eventHandler(eventString, chosenGirl, whipCat)
                callList.append(girlGrape)
                girlGrape.affinity += 1
                saveGame()
                returnToMenu = True
                gamestate = 3
            elif(girlAku.affinity == 0 and random.randrange(1, 8) == 7 and len(callList) >= 3):
                chosenGirl = girlAku
                scriptName = f"{chosenGirl.name}Meeting"
                eventString = getDateScript(scriptName, chosenGirl.name)
                eventHandler(eventString, chosenGirl, bigMall)
                callList.append(girlAku)
                girlAku.affinity += 1
                saveGame()
                returnToMenu = True
                gamestate = 3
            elif(girlRisol.affinity == 0 and girlAku.affinity >= 16):
                chosenGirl = girlRisol
                scriptName = f"{chosenGirl.name}Meeting"
                eventString = getDateScript(scriptName, chosenGirl.name)
                eventHandler(eventString, chosenGirl, bigMall)
                callList.append(girlRisol)
                girlRisol.affinity += 1
                saveGame()
                returnToMenu = True
                gamestate = 3
            elif(girlMarlene.affinity == 0 and currentInventory[rockTicket] >= 1 and girlGrape.relationshipLevel >= 1):
                currentInventory[rockTicket] -= 1
                chosenGirl = girlMarlene
                scriptName = f"{chosenGirl.name}Meeting"
                eventString = getDateScript(scriptName, chosenGirl.name)
                eventHandler(eventString, chosenGirl, rockVenue)
                callList.append(girlMarlene)
                girlMarlene.affinity += 1
                saveGame()
                returnToMenu = True
                gamestate = 3
            elif(girlGamer.affinity == 0 and player.totalDates >= 15 and random.randrange(1, 2) == 2):
                chosenGirl = girlGamer
                scriptName = f"{chosenGirl.name}Meeting"
                eventString = getDateScript(scriptName, chosenGirl.name)
                eventHandler(eventString, chosenGirl, rockVenue)
                girlGamer.affinity += 1
                saveGame()
                returnToMenu = True
                gamestate = 3
            elif(girlAllene.affinity == 0):
                averageGirlAffinity = getAverageGirlAffinity()
                if averageGirlAffinity >= 10:
                    chosenGirl = girlAllene
                    scriptName = f"{chosenGirl.name}Meeting"
                    eventString = getDateScript(scriptName, chosenGirl.name)
                    eventHandler(eventString, chosenGirl, girlHome)
                    callList.append(girlAllene)
                    girlAllene.affinity += 1
                    saveGame()
                    returnToMenu = True
                    gamestate = 3
            else:
                chosenGirl = None
                scriptName = f"{chosenGirl.name}Meeting"
                eventString = getDateScript(scriptName, chosenGirl.name)
                eventHandler(eventString, chosenGirl, None)
                callList.append(girlNadia)
                girlNadia.affinity += 1
                saveGame()
                returnToMenu = True
                gamestate = 3
            
    #CALL OPTION
    while(gamestate == 5):
        
        gc.collect()

        # diceRoll = (time.ticks_ms() % 100)
        if(initiateEvent):
            initiateEvent = False
            currentCall = 0
            okToPress = False
            screen_wipe()
        
        thumby.display.fill(0)
        menuCursor.y = 17
        menuCursor.x = 0
        phoneFace.x = 53
        phoneFace.y = 5
        callPhone.x = 50
        downArrow.x = 33
        downArrow.y = 36
        thumby.display.drawSprite(callPhone)
        thumby.display.drawSprite(menuCursor)
        thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
        thumby.display.drawText("Call who?", 1, 1, 1)
        thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
        

        if(thumby.actionPressed() == 0):
            okToPress = True
        if(okToPress is True):
            if(thumby.buttonB.pressed()):
                returnToMenu = True
                gamestate = 3
            if(thumby.buttonA.pressed() and len(callList) > 0):
                thumby.display.fill(0)
                chosenGirl = callList[currentCall]
                
                # if chosenGirl in recentlyCalled:
                #     callSomeoneElse = [["%NARRATION%"], ["You just called her recently... maybe you should hang out with someone else for now!"], ["%DONE%"]]
                #     eventHandler(callSomeoneElse, None, None)
                #     recentlyCalled[0] = None 
                #     break
                
                scriptType = "phoneCallpickUp"
                randScript = random.randrange(1, 4)
                scriptName = f"{chosenGirl.name}{scriptType}{randScript}"
                eventString = getDateScript(scriptName, chosenGirl.name)
                eventHandler(eventString, chosenGirl, None)
                chosenLocation = chooseLocation()
                if(chosenLocation in chosenGirl.likeLocations):
                    chosenGirl.affinity += 1
                scriptName = f"{chosenGirl.name}{scriptType}{chosenLocation.label}"
                eventString = getDateScript(scriptName, chosenGirl.name)
                eventHandler(eventString, chosenGirl, None)
                randScript = random.randrange(1, 4)
                scriptName = f"{chosenGirl.name}{chosenLocation.label}{randScript}"
                eventString = getDateScript(scriptName, chosenGirl.name)
                gift = eventHandler(eventString, chosenGirl, chosenLocation)
                if(gift != None):
                    scriptType = "Gift"
                    if(gift is chosenGirl.specialGift):
                        giftType = "Special"
                        chosenGirl.affinity += 4
                    elif(gift in chosenGirl.likeGifts):
                        giftType = "Good"
                        chosenGirl.affinity += 2
                    else:
                        giftType = "Neutral"
                        chosenGirl.affinity += 1
                    scriptName = f"{chosenGirl.name}{scriptType}{giftType}"
                    eventString = getDateScript(scriptName, chosenGirl.name)
                    eventHandler(eventString, chosenGirl, None)
                recentlyCalled[0] = chosenGirl
                chosenGirl.totalDates += 1
                player.totalDates += 1
                screen_wipe()

                
        if(thumby.buttonU.justPressed() and currentCall > 0):
            currentCall -= 1
        if(thumby.buttonD.justPressed() and currentCall < len(callList) - 1):
            currentCall += 1
        if(len(callList) > 1 and currentCall > 0):
            thumby.display.drawText(girl.name(callList[(currentCall - 1)]), 9, 9, 1)
        if(len(callList) != 0):
            thumby.display.drawText(girl.name(callList[currentCall]), 9 , 17, 1)
        if(len(callList) >= 2 and currentCall < (len(callList) - 1)):
            thumby.display.drawText(girl.name(callList[(currentCall + 1)]), 9, 25, 1)
        if(len(callList) > 2 and currentCall < (len(callList) - 2)):
            thumby.display.drawSprite(downArrow)
        if(len(callList) == 0):
            thumby.display.drawText("Empty", 9, 17, 1)
        thumby.display.update()
        
    #SHOP
    while(gamestate == 6):
    
        if(initiateEvent):
            initiateEvent = False
            currentShop = 0
            okToPress = False
            screen_wipe()
            
        thumby.display.fill(0)
        thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
        thumby.display.drawText("Buy Something?", 1, 1, 1)
        tinyCursor.x = 1
        tinyCursor.y = 22
        
        if(thumby.actionPressed() == 0):
            okToPress = True
        if(okToPress is True):
            if(thumby.buttonB.pressed()):
                returnToMenu = True
                gamestate = 3
            if(thumby.buttonA.pressed()):
                shopYesNo(shopList[currentShop])
                screen_wipe()
                thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
                
        if(thumby.buttonU.justPressed() and currentShop >= 2):
            currentShop -= 1
        if(thumby.buttonD.justPressed() and currentShop < len(shopList) - 1):
            currentShop += 1
        if(currentShop > 1):
            thumby.display.drawText(stuff.name(shopList[currentShop - 2]), 8, 10, 1)
        if(currentShop > 0):
            thumby.display.drawText(stuff.name(shopList[(currentShop - 1)]), 8, 16, 1)
        thumby.display.drawText(stuff.name(shopList[currentShop]), 8 , 22, 1)
        if(currentShop < (len(shopList) - 1)):
            thumby.display.drawText(stuff.name(shopList[(currentShop + 1)]), 8, 28, 1)
        if(currentShop < (len(shopList) - 2)):
            thumby.display.drawText(stuff.name(shopList[currentShop + 2]), 8, 34, 1)

        thumby.display.drawSprite(tinyCursor)
        thumby.display.update()
        
    #STATUS
    while(gamestate == 7):
        
        if(initiateEvent):
            menuCursorPosition = 0
            initiateEvent = False
            okToPress = False
            screen_wipe()
        
        if(thumby.actionPressed() == 0):
            okToPress = True
        if(okToPress is True):
            if(thumby.buttonB.pressed()):
                returnToMenu = True
                gamestate = 3
            if(thumby.buttonD.justPressed() and menuCursorPosition < 2):
                menuCursorPosition += 1
            if(thumby.buttonU.justPressed() and menuCursorPosition > 0):
                menuCursorPosition -= 1
            if(thumby.buttonA.pressed() and menuCursorPosition == 0):
                gamestate = 8
                initiateEvent = True
            if(thumby.buttonA.pressed() and menuCursorPosition == 1):
                gamestate = 9
                initiateEvent = True
            if(thumby.buttonA.pressed() and menuCursorPosition == 2):
                gamestate = 10          
                initiateEvent = True
            thumby.display.fill(0)
            if(menuCursorPosition == 0):
                menuCursor.y = 3           
            elif(menuCursorPosition == 1):
                menuCursor.y = 12           
            elif(menuCursorPosition == 2):
                menuCursor.y = 21          
            # elif(menuCursorPosition == 3):
            #     menuCursor.y = 30          
            menuCursor.x = 0
            

            thumby.display.drawSprite(menuCursor) 
            
        
            thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
            thumby.display.drawText("FRIENDS", 9, 3, 1)
            thumby.display.drawText("PLAYER", 9, 12, 1)
            thumby.display.drawText("INVENTORY", 9, 21, 1)
            # thumby.display.drawText("SETTINGS", 9, 30, 1)
            thumby.display.update()
        
    #FRIENDS    
    while(gamestate == 8):
        
        thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
        
        if(initiateEvent):
            initiateEvent = False
            okToPress = False
            screen_wipe()
            # if(len(callList) > 0):
            #     currentCall = 1
            # else:
            currentCall = 0
                
        if(thumby.actionPressed() is False):
            okToPress = True
        if(okToPress is True):
            if(thumby.buttonB.pressed()):
                initiateEvent = True
                gamestate = 7
            thumby.display.fill(0)
            menuCursor.y = 17
            if len(callList) > 0:
                if(thumby.buttonU.justPressed() and currentCall > 0):
                    currentCall -= 1
                if(thumby.buttonD.justPressed() and currentCall < len(callList) - 1):
                    currentCall += 1
                if(len(callList) > 1 and currentCall > 0):
                    thumby.display.drawText(girl.name(callList[(currentCall - 1)]), 9, 9, 1)
                thumby.display.drawText(girl.name(callList[currentCall]), 9 , 17, 1)
                if(len(callList) > 1 and currentCall < (len(callList) - 1)):
                    thumby.display.drawText(girl.name(callList[(currentCall + 1)]), 9, 25, 1)
            else:
                thumby.display.drawText("EMPTY", 9, 17, 1)
            
            thumby.display.drawSprite(menuCursor)
            thumby.display.update()
            
            if thumby.buttonA.pressed() and len(callList) > 0:
                gc.collect()
                chosenGirl = callList[currentCall]
                displayStats(chosenGirl)
                okToPress = False
                
    
    #PLAYER            
    while(gamestate == 9):
        
        if(initiateEvent):
            initiateEvent = False
            okToPress = False
            screen_wipe()
        
        if(thumby.actionPressed() == 0):
            okToPress = True
        if(okToPress is True):
            if(thumby.buttonB.pressed()):
                initiateEvent = True
                gamestate = 7
                # screen_wipe()
                break
            thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
            thumby.display.drawText("MONEY: " + str(player.money), 9, 1, 1)
            thumby.display.drawText("DATES: " + str(player.totalDates), 9, 9, 1)

            thumby.display.update()
    
    #INVENTORY MENU            
    while(gamestate == 10):
        
        if(initiateEvent):
            initiateEvent = False
            currentShop = 0
            okToPress = False
            screen_wipe()
        itemNames = [key for key, value in currentInventory.items() if value != 0]
        
        while(1):
        
            if(thumby.actionPressed() == 0):
                okToPress = True
            if(okToPress is True):
                if(thumby.buttonB.pressed()):
                    currentShop = 0
                    initiateEvent = True
                    gamestate = 7
                    break
    
            thumby.display.fill(0)
            thumby.display.setFont("/lib/font3x5.bin", 3, 5, 1)
            thumby.display.drawText("ITEMS:", 1, 1, 1)
            if(thumby.actionPressed() == 0):
                okToPress = True
            if len(itemNames) is not 0:
                if(thumby.buttonU.justPressed() and currentShop > 0):
                    currentShop -= 1
                if(thumby.buttonD.justPressed() and currentShop < len(itemNames) - 1):
                    currentShop += 1
                if(len(itemNames) > 2 and currentShop > 1):
                    thumby.display.drawText(stuff.name(itemNames[currentShop - 2]), 69, 10, 1)
                if(len(itemNames) > 1 and currentShop > 0):
                    thumby.display.drawText(stuff.name(itemNames[currentShop - 1]), 1, 16, 1)
                    thumby.display.drawText(str(currentInventory[itemNames[currentShop - 1]]), 69, 16, 1)
                thumby.display.drawFilledRectangle(0, 21, 72, 7, 1)
                thumby.display.drawText(stuff.name(itemNames[currentShop]), 1 , 22, 0)
                thumby.display.drawText(str(currentInventory[itemNames[currentShop]]), 69 , 22, 0)
                if(len(itemNames) > 1 and currentShop < (len(itemNames) - 1)):
                    thumby.display.drawText(stuff.name(itemNames[currentShop + 1]), 1, 28, 1)
                    thumby.display.drawText(str(currentInventory[itemNames[currentShop + 1]]), 69, 28, 1)
                if(len(itemNames) > 2 and currentShop < (len(itemNames) - 2)):
                    thumby.display.drawText(stuff.name(itemNames[currentShop + 2]), 1, 34, 1)
                    thumby.display.drawText(str(currentInventory[itemNames[currentShop + 2]]), 69, 34, 1)
                # if(len(itemNames) == 1):
                #     thumby.display.drawText(stuff.name(itemNames[currentShop]), 1 , 22, 1)
                #     thumby.display.drawText(str(currentInventory[itemNames[currentShop]]), 69 , 22, 1)
            else:
                thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)
                thumby.display.drawText("EMPTY", 9, 17, 1)
            
            thumby.display.update()
    