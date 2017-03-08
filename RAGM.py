#      -=+=- Ragm -=+=-
# By RYArrowsmith and Mezza_02
health = 10
gold = 20
action = ""
name = ""

def sendHelp():

    print("""
-=+=- Ragm Help -=+=-

Controls:
- h: Help - Displays this message.
""")
    return

print("""Welcome to Ragm!""")
print("=================")
HELP = input("Press S to start or H for help")
if HELP == "H":
    print("=================")
    print("Commands:")
    print("      w = Forward")
    print("      a = Left")
    print("      s = Go back")
    print("      d = Right")
    print("      i = Inventory")
    print("      y = Yes")
    print("      n = No")
    print("      r = Run")
    print("      f = Fight")
    print("=================")
    HELP = input()

else:
    print("")

print("=================")

print("Let's Begin!!")
print("=================")
print("")
print("")
print("")
print("")
print("")
print("=================")
print("""What is your name, young one?""")
name = input("<~ ")
while 1:

    action = input("<~ ").lower()

    if (action == "h"):

        sendHelp()
        
        
        
    
