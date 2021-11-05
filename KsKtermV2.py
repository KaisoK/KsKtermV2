from Functions import *

def menuInicio():

    subprocess.run("clear")
    print("-----KsKtermV1.1-----\n\n")
    print("Please, choose an option (1,2,3,4)\n")
    print("1. Session -> \n")
    print("2. Server -> \n")
    print("3. Tools -> \n")
    print("4. EXIT ->\n")
    print("--------------------")

    respuesta = input("\n-> ")

    if respuesta == "1":

        menuSessions()

    elif respuesta == "2":

        menuServers()

    elif respuesta == "3":

        menuTools()

    elif respuesta == "4":

        exitApp()

    else:

        noValidMain()

def menuSessions():

        subprocess.run("clear")
        print("--------------------\n")
        print("SESSIONS MENU\n\n")
        print("Please select the option deserved\n")
        print("1. SSH ->")
        print("2. FTP ->")
        print("3. TCP ->\n")
        print("\n4. Go Back ->")
        print("5. EXIT ->")
        print("\n--------------------")

        respuesta = input("\n-> ")

        if respuesta == "1":

            sshSession()

        elif respuesta == "2":

            ftpSession()
            
        elif respuesta == "3":

            tcpSession()

        elif respuesta == "4":

            backMain()

        elif respuesta == "5":

            exitApp()

        else:

            noValidSession()

def menuServers():

        subprocess.run("clear")
        print("--------------------\n")
        print("SERVERS MENU\n\n")
        print("Please select the option deserved\n")
        print("1. SSH ->")
        print("2. FTP ->")
        print("3. TCP ->\n")
        print("4. Go Back ->")
        print("5. EXIT ->\n")
        print("--------------------")

        respuesta = input("\n-> ")

        if respuesta == "1":

            sshServer()

        elif respuesta == "2":

            ftpServer()

        elif respuesta == "3":

            tcpServer()

        elif respuesta == "4":

            backMain()

        elif respuesta == "5":

            exitApp()

        else:

            noValid()

def menuTools():

    subprocess.run("clear")
    print("--------------------\n")
    print("TOOLS MENU\n\n")
    print("1. Internet status check -> \n")
    print("2. SSH Tunneling -> \n")
    print("3. Open ports check -> \n")
    print("4. Open a new terminal -> \n")
    print("\n5. Go Back ->")
    print("6. EXIT ->\n")
    print("--------------------")

    respuesta = input("\n-> ")

    if respuesta == "1":

        intertetStatus()

    elif respuesta == "2":

        sshTunnel()

    elif respuesta == "3":

        openPorts()
    
    elif respuesta == "4":

        newTerminal()           

    elif respuesta == "5":

        backMain()

    elif respuesta == "6":

        exitApp()

    else:

        noValid2()