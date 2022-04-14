#!/usr/bin/env python3

import random
import sys

#name="Agra"

if len(sys.argv) == 1 :
    print("Error : Missing Character Name")
    quit()

name=sys.argv[1]

random.seed(a=name, version=2)

Str1=random.randint(1,6)
Str2=random.randint(1,6)
Dex1=random.randint(1,6)
Dex2=random.randint(1,6)
Wil1=random.randint(1,6)
Wil2=random.randint(1,6)

HP1=random.randint(0,5)
Pip1=random.randint(0,5)
BG1=random.randint(0,5)
BG2=random.randint(0,5)

Bis=random.randint(0,5)
Coa=random.randint(0,5)
PD1=random.randint(0,5)
PD2=random.randint(0,5)

Job = [["Test Subject",   "Kitchen Forager","Cage Dweller", "Hedge Witch",    "Leatherworker","Street Tough"     ],
      [ "Menicant Priest","Beetleherd",     "Ale Brewer",   "Fishermouse",    "Blacksmith",   "Wireworker"       ],
      [ "Woodcutter",     "Bat Cultist",    "Tin Miner",    "Trash Collector","Wall Rover",   "Merchant"         ],
      [ "Raft Crew",      "Worm Wrangler",  "Sparrow Rider","Sewer Guide",    "Prison Guard", "Fungus Farmer"    ],
      [ "Dam Builder",    "Cartographer",   "Trap Thief",   "Vagabond",       "Grain Farmer", "Message Runner"   ],
      [ "Troubadour",     "Gambler",        "Sap Tapper",   "Bee Keeper",     "Librarian",    "Pauper Noblemouse"]]

ItemA = [["Spell: Magic Missile","Shield & Jerkin (Light Armour)","Spell: Be Understood", "Spell: Heal","Shield & Jerkin (Light Armour)","Dagger (Light, d6)"],
        [ "Spell: Restore", "Hireling: Loyal Beetle", "Hireling: Drunken Torchbearer","Net", "Hammer (Medium, d6/d8)", "Wire, Spool"       ],
        [ "Axe (Medium, d6/d8)", "Spell: Darkness", "Pickaxe (Medium, d6/d8)", "Trashhook (Heavy, d10)", "Fishhook", "Hireling: Pack Rat"],
        [ "Hammer (Medium, d6/d8)", 'Pole, 6"', "Fishhook", "Metal File", 'Chain, 6"', "Dried Mushroom (as Rations)"],
        [ "Shovel", "Quill & Ink", "Block of Cheese", "Tent", "Spear (Heavy, d10)", "Bedroll"],
        [ "Musical Instrument", "Set of Loaded Dice", "Bucket", "Jar of Honey", "Scrap of Obscure Book", "Felt Hat"]]

ItemB = [["Lead Coat (Heavy Armour)", "Cookpots", "Bottle of Milk", "Incense Stick", "Shears", "Flask of Coffee"],
        [ "Holy Symbol", 'Pole, 6"', "Small Barrel of Ale", "Needle (Light, d6)", "Metal File", "Electric Lantern"],
        [ "Twine, Roll", "Bag of Bat Teeth", "Lantern", "Mirror", "Thread, Spool", "20p IOU from a Noblemouse"],
        [ "Wooden Spikes", "Soap", "Goggles", "Thread, Spool", "Spear (Heavy, d10)", "Spore Mask"],
        [ "Wooden Spikes", "Compass", "Glue", "Treasure Map, Dubious", "Whistle", "Documents, Sealed"],
        [ "Disguise Kit", "Mirror", "Wooden Spikes", "Net", "Quill & Ink", "Perfume"]]

PD = [["a scarred body", "a corpulent body", "a skeletal body", "a willowy body", "a tiny body", "a massive body"],
     [ "war paint", "foreign clothes", "elegant clothes", "patched clothes", "fashionable clothes", "unwashed clothes"],
     [ "a missing ear", "lumpy face", "a beautiful face", "a round face", "a delicate face", "an elongated face"],
     [ "groomed fur", "dreadlocks", "dyed fur", "shaved fur", "frizzy fur", "silky fur"],
     [ "night-black eyes", "an eye-patch", "blood-red eyes", "wise eyes", "sharp eyes", "luminous eyes"],
     [ "a cropped tail", "a whip-like tail", "a tufted tail", "a stubby tail", "a prehensile tail", "a curly tail" ]]

Sig=["Star","Wheel","Acorn","Storm","Moon","Mother"]
Dis=["Brave but reckless","Industrious but unimaginative","Inquisitive but stubborn","Generous but wrathful","Wise but mysterious","Nurturing but worrying"]
Col=["chocolate","black","white","tan","grey","blue"]
Pat=["solid","brindle","patchy","banded","marbled","flecked"]

BGC=""

Str=str(Str1+Str2)
Dex=str(Dex1+Dex2)
Wil=str(Wil1+Wil2)

Att = {
    "Str": Str1+Str2,
    "Dex": Dex1+Dex2,
    "Wil": Wil1+Wil2
}

print()

print("Str=" + str(Att["Str"]))
print("Dex=" + str(Att["Dex"]))
print("Wil=" + str(Att["Wil"]))

while True:
    print("Do you want to swap any of these? [Y/N]")
    swap=input()
    if swap == "N" :
        break
    if swap == "Y" : 
        print("What is the first stat you wish to swap? [Str/Dex/Wil]")    
        swap1=input()
        if not swap1 in Att.keys():
            print("Please input Str, Dex, or Wil.")
            continue
        else :
            print("What do you want to swap it with? [Str/Dex/Wil]")
            swap2=input()
        if not swap2 in Att.keys():
            print("Please input Str, Dex, or Wil.")
            continue
        else :
            swapi = Att[swap1]
            Att[swap1] = Att[swap2]
            Att[swap2] = swapi
            break
    elif swap != "N" : 
        print("Y or N only please.")

Mat=max(Att["Str"],Att["Dex"],Att["Wil"])
print()

while Mat <= 9 :
    print("Would you prefer " + ItemA[BG1][BG2] + "[A] or " + ItemB[BG1][BG2] + "[B]?")
    pre1=input()
    if pre1 == "A" :
        BGC=ItemA[BG1][BG2]
        break
    if pre1 == "B" :
        BGC=ItemB[BG1][BG2]
        break
    else : 
        print("Input A or B")
        BGC=""
        continue

print()

print("What we﻿apon do you choose?")
Wpn1=input()

print ()

print(name + " the " + Job[HP1][Pip1])

print()

print("Str=" + str(Att["Str"]))
print("Dex=" + str(Att["Dex"]))
print("Wil=" + str(Att["Wil"]))

print()

print("HP=" + str(HP1+1))

print()

print("Torches")
print("Rations")
if BGC != "" :
    print(str(BGC))
if Wpn1 != "" :
    print(str(Wpn1))
print("Pips=" + str(Pip1+1))

print()

print("Born under the sign of the " + Sig[Bis])
print(Dis[Bis])
print("With a coat of " + Pat[Coa] + " " + Col[Coa])
print("and " + PD[PD1][PD2])

print ()

print("fin")
