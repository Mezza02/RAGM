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
print("""What is your name, young one?""")
name = input("<~ ")
while 1:

    action = input("<~ ").lower()

    if (action == "h"):

        sendHelp()
