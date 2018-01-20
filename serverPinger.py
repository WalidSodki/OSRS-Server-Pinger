import os #os is used for the ping
import platform

f2p_list = [1, 8, 16, 26, 35, 81, 82, 83, 84, 85, 93, 94] #list of all the F2P servers

def servers():
    print(parameters)
    for i in range(1, 94): #there are currently 94 OSRS servers
        hostname = "oldschool"+ str(i) + ".runescape.com" #pinging server 1 through 94
        print("\n*** Pinging server: ", str(i), " hostname: ", hostname, "***") #displaying which server that is currently being pinged
        response = os.system("ping " + hostname) #get the ping
    return

def p2p():
    print('Only members (P2P) servers will be pinged.')
    for i in range (0, 94): #server 1 is F2P and can be skipped in the range
        if i in f2p_list: #if a server is part of the F2P list then skip it with continue
            continue

        hostname = "oldschool"+ str(i) + ".runescape.com"
        print("\n*** Pinging server: ", str(i), " hostname: ", hostname, "***")
        response = os.system("ping " + hostname)
    return


def f2p():
    print('Only Free to Play (F2P) servers will be pinged.')
    for i in range(0, len(f2p_list)):
        hostname = "oldschool"+ str(f2p_list[i]) + ".runescape.com"
        print("\n*** Pinging server: ", str(f2p_list[i]), " hostname: ", hostname, "***")
        response = os.system("ping " + hostname)
    return

def start(): #take input from user to what filter for the pinging should be used
    serverType = input("Do you want to ping ALL servers, Memebers only or Free to Play only? \n").lower()
    if 'all' in serverType:
        servers()
    elif 'mem' in serverType or 'p2p' in serverType or 'pay' in serverType:
        p2p()
    elif 'f' in serverType:
        print("Free to play (F2P) servers will now be pinged.")
        f2p()
    else:
        print("Sorry, I did not get that. Please try again.")
        start()


print ("Oldschool Runescape Ping Checker")
print ("By Walid Sodki \n")
start()
print ("\n*** Ping process is now done. ***")
