fishingnet_inventory = 0
flaregun_inventory = 0
packofwater_inventory = 0
first_aid_kit_inventory = 0
yousleep = "You Sleep"
lowBalence ="Balence too low. To continue with story press x"
from glob import glob
import keyboard
import time
buyer_option='''
"Fishing net: 5$(press 2 to buy)",
"Flare gun: 2$(press 3 to buy)"
"5 pack of water 6$(press 4 to buy)",
"First Aid kit: 3$(press 7 to buy)",
'''

def buy():
    playermoney = 20
    fishingnet_inventory = 0
    flaregun_inventory = 0
    packofwater_inventory = 0
    first_aid_kit_inventory = 0    
    while True:
        if keyboard.read_key() == "3" and playermoney > 2:
            playermoney= playermoney-2 
            flaregun_inventory = flaregun_inventory + 1
            print(f"You have {playermoney} dollars. Press X to stop shopping")          
        if playermoney <= 2 and keyboard.read_key() == "3":
            print(lowBalence) 
            if keyboard.read_key() == "x":
                break          
        if keyboard.read_key() == "2" and playermoney > 5:
            playermoney= playermoney-5
            print(f"You have {playermoney} dollars. Press X to stop shopping")
            fishingnet_inventory = fishingnet_inventory+1          
        if playermoney <= 5 and keyboard.read_key() == "2":
            print(lowBalence)      
            if keyboard.read_key() == "x":
                break          
        if keyboard.read_key() == "4" and playermoney > 6:
            playermoney= playermoney-6 
            print(f"You have {playermoney} dollars. Press X to stop shopping")
            packofwater_inventory = packofwater_inventory+1         
        if playermoney <= 6 and keyboard.read_key() == "4":
            print(lowBalence)    
            if keyboard.read_key() == "x":
                break              
        if keyboard.read_key() == "7" and playermoney > 3:
            playermoney= playermoney-3 
            print(f"You have {playermoney} dollars. Press X to stop shopping")  
            first_aid_kit_inventory = first_aid_kit_inventory+1       
        if playermoney <= 6 and keyboard.read_key() == "7":
            print(lowBalence)
        if keyboard.read_key() == "x":
            break              
                               
   

def investigate():
    print("Anthony: Bears are really common in this area. Luckly, I have bear spray if the situation presents itself")
    time.sleep(4)
    print("As you and Anthony start apporaching the sound, you see a bright flash of light")
    time.sleep(4)
    print("Anthony: WOAH, what is that??!")
    time.sleep(4)
    print("You start to feel lighter, as if you are floating")
    time.sleep(2)
    print("Dear god. They are here")
    time.sleep(3)
    print("You suddenly realize that you being abucted by aliens")
    time.sleep(2)
    print("Unfortunately it is too late and you are abducted by aliens, never to be seen again")
def dontinvestigate():
    print("You decide its not worth investigating, but it sounds strangly ominous")
    time.sleep(4)
    print("Anthony: Geez, I sure worked up the appetite")
    time.sleep(4)
    if fishingnet_inventory <= 0:
      print("Anthony: Shame we dont have any fishing nets")
      time.sleep(4)
      print("Anthony:However, that shouldnt stop us from completing this journey")
      
def first_night():
    print("Many hours pass by")
    time.sleep(4)
    print("Anthony: Its starting to get dark. We should start setting up our tents")
    time.sleep(4)
    print("You are about to help Anthony set up his tent until you hear him shrek in pain")
    time.sleep(4)
    print("Anthony: ARRGGGHH")
    time.sleep(4)
    print("As you come to Anthony's aid, you see blood all over his arm")
    time.sleep(4)
    print("Anthony:Son of a bit*h! An orangutan bit me!!")
    time.sleep(4)
    if first_aid_kit_inventory > 0:
        global use_kit
        use_kit = input("Should you use a first aid kit on Anthony:(yes/no)")
        if use_kit == "yes":
            print("You decide to your medkit on Anthony")
        if use_kit == "no":
            print("You decide against using your medkit") 
            time.sleep(1)
            print("However, the infection gets worse and he handicap")
            time.sleep(1.5)
    if first_aid_kit_inventory <= 0:
        print("Unfortunately, you dont have a first aid kit. You are helpless and are unable to do anything")
    time.sleep(4)
    print("Anthony: I dont think we should continue. At the brink of dawn we should start heading back")
    time.sleep(4)
    print("You and Anthony set up camp and start a fire")
    time.sleep(3)
    print(yousleep)
    time.sleep(3)
    print(yousleep)
    time.sleep(3)
    print(yousleep)
    print("You are woken up to the sound of your tent rustling")
    time.sleep(4)
    print("You realize you are in the midst of a storm")
    time.sleep(4)
    print("You are worried for Anthony, but you are too lazy to check on him")
    time.sleep(3)
    global checkonanthony
    checkonanthony = input("Should you check on Anthony? (yes/no")
    if checkonanthony == ("yes"):
        print("You finally give in and decide to check on Anthony")
        time.sleep(3)
        print("However, as you are about to open your tent Anthony dives in yours")
    if checkonanthony == ("no"):
        print("You are confident that Anthony is ok, and start to fall back to sleep")
        time.sleep(3)
        print(yousleep)     
        time.sleep(3)
        print(yousleep)
        time.sleep(3)
        print("You are woken up by Anthony, who is breathing heavy ontop of you")
    print("Anthony:JESUS CHRIST")
    time.sleep(3)
    print("Anthony: A GIANT TREE JUST FELL ON ME!")
    time.sleep(3)
    print("You consult Anthony, and give him time to re-gather his thoughts")
    time.sleep(3)
    print("You try to pay attention to what he is saying, but start to feel dizzy")
    time.sleep(3)
    print("Anthony: ...And I barely made it out....thank god for... are you esohnsj?")
    time.sleep(3)
    print("You wake in the morning to Anthony examing you")
    time.sleep(3)
    print("Anthony: Great! Your back. You were out for while. Guess ya must of been tired from all the walking.")
    time.sleep(2)
    print("You and Anthony start packing your things and leaving the campsite")
    time.sleep(2)
    print("As you walk back home, you notice Anthony is struggling to keep up with you")
    time.sleep(2)
    print("Many hours pass...")
    time.sleep(2)
    print("Anthony is starting to really slow you down")
    time.sleep(2)
    if flaregun_inventory > 0:
     print("Anthony: Maybe we should start using that flaregun")
     global useflaregun
     time.sleep(2)
     useflaregun = input("Should you use flare gun?(yes/no)")
     if useflaregun == "yes":
        print("You decide to use your flare gun, but nobody sees it")
     if useflaregun == "no":
        print("You decide against it.")
    time.sleep(3)
    print("You start to become worryed that Anthony will drain all your resources")
    global killAnthony
    killAnthony = input("Should you kill Anthony(yes/no)?")
    if killAnthony == "yes":
        print("You decide to wait for right moment")
        time.sleep(2)
        print("Anthony says that he needs to pee, and you reluctantly agree")
        time.sleep(4)
        print("You silently grab a rock")
        time.sleep(4)
        print("You hit Anthony as hard as you can and he drops unconscious")
        time.sleep(4)
        print("You continue to violently beat Anthony until you are confindent he is dead.")
        time.sleep(4)
        print("You dump his body in a river, annd clean you clothes are hand of the blood")
        time.sleep(4)
        print("You make up a cover story that Anthony was bitten by a snake and continue your trek back")
        time.sleep(4)
        print("Many days pass by, however you dont lose hope and continue to push forward")
        time.sleep(4)
        print("Just as you finsh that last of your supplies, you find a village which calls for help and nurses you")
        time.sleep(4)
        print("You reached the good ending. Killing Anthony was the right choice or else you would of straved to death")
    if killAnthony == "no":
        print("You decide against it and scold yourself for thinking such things")
        time.sleep(4)
        print("However, you make less and less progress.")
        time.sleep(4)
        print("At some point, you and Anthony go off trail and get lost")
        time.sleep(3)
        print("You use the last of your resources and die due to dehydration")  
        time.sleep(4)
        print("You got the bad ending.")    