import variablesforfirstgame
import time
import keyboard
print("Hello and welcome to the Amazon Rainforest. I'm your tour guide, Anthony. Do your mind telling us your name?")
time.sleep(2)
playername=input("Enter name: ")
print(f"Anthony: Alright, {playername} lets start preparing for our journey!")
time.sleep(1)
print("Anthony: I'll give you 20 dollars to spend with at the marketplace")
time.sleep(2)
print(variablesforfirstgame.buyer_option)
variablesforfirstgame.buy()
print("Anthony: Great work, lets start our journey.")
time.sleep(2)
print("As you and Anthony continue up the trail, you hear a humming noise behind you.")
time.sleep(2)
print("Should you investigate(1)or continue walking(2)?")
if keyboard.read_key() == "1":
        variablesforfirstgame.investigate()
if keyboard.read_key() == "2":
        variablesforfirstgame.dontinvestigate()
time.sleep(2) 
variablesforfirstgame.first_night()
            
