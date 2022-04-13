import random
import sys

name="Agra"
#name=sys.argv[1]

random.seed(a=name, version=2)

Str1=random.randint(1,6)
Str2=random.randint(1,6)
Dex1=random.randint(1,6)
Dex2=random.randint(1,6)
Wil1=random.randint(1,6)
Wil2=random.randint(1,6)

HP1=random.randint(0,5)
Pip1=random.randint(0,5)

Bis=random.randint(0,5)
Coa=random.randint(0,5)
PD1=random.randint(0,5)
PD2=random.randint(0,5)

Job = [["Test Subject",   "Kitchen Forager","Cage Dweller", "Hedge Witch",    "Leatherworker","Street Tough"     ],
      [ "Menicant Priest","Beetleherd",     "Ale Brewer",   "Fishermouse",    "Blacksmith",   "Wireworker"       ],
      [ "Woodcutter",     "Bat Cultist",    "Tin Miner",    "Trash Collector","Wall Rover",   "Merchant"         ],
      [ "Raft Crew",      "Worm Wrangler",  "Sparrow Rider","Sewer Guide",    "Prison Guard", "Fungus Farmer"    ],
      [ "Dam Builder",    "Cartographer",   "Trap Thief",   "Vagabond",       "Grain Farmer", "Message Runner"   ],
      [" Troubadour",     "Gambler",        "Sap Tapper",   "Bee Keeper",     "Librarian",    "Pauper Noblemouse"]]

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



print(name + " the " + Job[HP1][Pip1])

print()

print("Str=" + str(Str1+Str2))
print("Dex=" + str(Dex1+Dex2))
print("Wil=" + str(Wil1+Wil2))
print()
print("HP=" + str(HP1+1))

print()

print("Torches")
print("Rations")
print(ItemA[HP1][Pip1])
print(ItemB[HP1][Pip1])
print("Pips=" + str(Pip1+1))

print()

print("Born under the sign of the " + Sig[Bis])
print(Dis[Bis])
print("With a coat of " + Pat[Coa] + " " + Col[Coa])
print("and " + PD[PD1][PD2])

print ()

print("fin")
