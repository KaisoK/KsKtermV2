#Importations

import time, os, subprocess, socket

#Functions

def exitApp():

    subprocess.run("clear")
    print("--------------------\n")
    print("Bye...\n")
    print("--------------------")
    time.sleep(1)
    subprocess.run("clear")
    exit()

def noValidMain():

    subprocess.run("clear")
    print("--------------------\n")
    print("\nPlease insert a valid option...")
    print("\n\n--------------------")
    time.sleep(2)
    os.system('python3 Menu.py')

#Menu Funtions

#Menu Subsessions

def sshSession():

    subprocess.run("clear")
    print("--------------------\n")
    print("SSH SESSION \n")

    host = input("Set host -> ")
    port = input("Set the port -> ")
    username = input("Set the username -> ")
    password = getpass.getpass("Set the password -> ")
    command = "ls"

    """

    os.system("ssh {}@{} -p {}".format(username, host, port))
        

    """

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)

    stdin, stdout, stderr = ssh.exec_command(command)
    lines = stdout.readlines()
    print(lines)
    
    print("\n--------------------")

def ftpSession():

    subprocess.run("clear")
    print("--------------------\n")
    print("FTP session -> \n")
    print("--------------------")

def tcpSession():

    subprocess.run("clear")
    print("--------------------\n")
    print("TCP session -> \n")
    print("--------------------")

def backMain():

    subprocess.run("clear")
    print("--------------------\n")
    print("Go back to main -> \n")
    print("--------------------")
    time.sleep(1)
    menuInicio()

def noValidSession():

    subprocess.run("clear")
    print("--------------------\n")
    print("\nPlease insert a valid option...")
    print("\n\n--------------------")
    time.sleep(2)
    SubSessions.menuSessions()

#Menu SubServers

def sshServer():

    subprocess.run("clear")
    print("--------------------\n")
    print("SSH server -> \n")
    print("\n1. Start SSH server -> ")
    print("2. Check SSH server status -> ")
    print("3. Stop SSH server -> ")

    print("\n4. Go back to SERVERS -> ")
    print("5. Go back to MAIN -> ")
    print("\n--------------------")

    a = input("\n-> ")

    if a == "1":
        
        subprocess.run("clear")
        os.system("sudo systemctl start ssh")
        print("--------------------\n")
        print("SSH server started!")
        print("\n--------------------")
        time.sleep(2)
        sshServer()

    elif a == "2":

        subprocess.run("clear")
        print("--------------------\n")
        print("\nSSH SERVER STATUS\n")
        print(os.system("sudo systemctl status ssh"))
        print("\n--------------------")
        time.sleep(2)
        sshServer()

    elif a == "3":

        subprocess.run("clear")
        print("--------------------\n")
        print("\nSSH SERVER STOPPED!\n")
        os.system("sudo systemctl stop ssh")
        print("\n--------------------")
        time.sleep(2)
        sshServer()

    elif a == "4":

        SubServers.menuServers()

    elif a == "5":

        os.system("python3 Menu.py")

    else:

        subprocess.run("clear")
        print("--------------------\n")
        print("\nPlease insert a valid option...")
        print("\n\n--------------------")
        time.sleep(2)
        sshServer()

def ftpServer():

    subprocess.run("clear")
    print("--------------------\n")
    print("FTP SERVER -> \n")
    print("\n1. Start FTP server -> ")
    print("2. Check FTP server status -> ")
    print("3. Stop FTP server -> ")

    print("\n4. Go back to SERVERS -> ")
    print("5. Go back to MAIN -> ")
    print("\n--------------------")

    a = input("\n-> ")

    if a == "1":

        subprocess.run("clear")
        os.system("sudo systemctl start vsftpd")
        print("--------------------\n")
        print("FTP server started!")
        print("\n--------------------")
        time.sleep(2)
        ftpServer()

    elif a == "2":

        subprocess.run("clear")
        print("--------------------\n")
        print("\nFTP SERVER STATUS\n")
        print(os.system("sudo systemctl status vsftpd"))
        print("\n--------------------")
        time.sleep(2)
        ftpServer()

    elif a == "3":

        subprocess.run("clear")
        print("--------------------\n")
        print("\nFTP SERVER STOPPED!\n")
        os.system("sudo systemctl stop vsftpd")
        print("\n--------------------")
        time.sleep(2)
        ftpServer()

    elif a == "4":

        SubServers.menuServers()

    elif a == "5":

        os.system("python3 Menu.py")

    else:

        subprocess.run("clear")
        print("--------------------\n")
        print("\nPlease insert a valid option...")
        print("\n\n--------------------")
        time.sleep(2)
        ftpServer()

def tcpServer():

    subprocess.run("clear")
    print("--------------------\n")
    print("TCP server -> \n")
    print("\n1. Start TCP server -> ")
    print("2. Check TCP server status -> ")
    print("3. Stop TCP server -> ")
    
    print("\n4. Go back to SERVERS -> ")
    print("5. Go back to MAIN -> ")
    print("\n--------------------\n")

    a = input("-> ")

    if a == "1":
    
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s_address = ("localhost", 10000)
        print("Turning on server {} on port {}".format(*s_address))
        sock.bind(s_address)

        sock.listen(1)

        while True:
            print("Waiting for connection...\n")
            connection, client_address = sock.accept()
            
            try:
                print("Conection from ", client_address)

                while True:
                    data = connection.recv(1024)
                    print("{!r}".format(data))
                
            finally:
                connection.close()

    elif a == "2":
        
        os.system("sudo lsof -i -P -n | grep {}".format(port))
        input("\n\nPress ENTER to go back -> ")
        SubServers.tcpServer()

    elif a == "3":
        
        os.system("lsof -t -i:{} | xargs kill -9".format(port))
        input("\n\nPress ENTER to go back -> ")
        tcpServer()

    elif a == "4":
        
        SubServers.menuServers()

    elif a == "5":
        
        os.system("python3 Menu.py")

    else:
        
        subprocess.run("clear")
        print("--------------------\n")
        print("\nPlease insert a valid option...")
        print("\n\n--------------------")
        time.sleep(2)
        tcpServer()

def noValidServers():

    subprocess.run("clear")
    print("--------------------\n")
    print("\nPlease insert a valid option...")
    print("\n\n--------------------")
    time.sleep(2)
    SubServers.menuServers()

#Menu SubTools

def intertetStatus():

    subprocess.run("clear")
    print("--------------------\n")
    print("INTERNET STATUS CHECK\n\n")
    print("1. Ping to Google ->\n")
    print("2. Speedtest ->\n\n")
    print("3. Go back ->")
    print("4. EXIT ->\n")
    print("--------------------")

    r = input("\n-> ")

    if r == "1":

        ping()

    elif r == "2":

        speedtest()

    elif r == "3":

        backTools()

    else:

        noValid1()

def ping():

    subprocess.run("clear")
    print("--------------------\n")
    print("Ping to Google\n")
    os.system("ping -c 4 google.com")
    print("\n--------------------")
    input("\nPress ENTER to end ->")
    SubTools.menuTools()

def speedtest():

    subprocess.run("clear")
    print("--------------------\n")
    print("SPEEDTEST\n")
    subprocess.run("speedtest")
    print("\n--------------------")
    input("\n\nPress ENTER to end -> ")
    SubTools.menuTools()

def backTools():

    subprocess.run("clear")
    print("--------------------\n")
    print("Going back... \n")
    print("--------------------")
    time.sleep(1)
    menuTools()

def noValidTools():

    subprocess.run("clear")
    print("--------------------\n")
    print("\nPlease insert a valid option...")
    print("\n\n--------------------")
    time.sleep(2)
    SubTools.menuTools()

def sshTunnel():

    subprocess.run("clear")
    print("--------------------\n")
    print("SSH Tunneling (Port Forwarding) -> \n")
    print("--------------------")

def openPorts():

    subprocess.run("clear")
    print("--------------------\n")
    print("OPEN PORTS\n")
    os.system("sudo lsof -i -P -n")
    print("--------------------")
    input("Press ENTER to end -> ")
    SubTools.menuTools()

def newTerminal():

    subprocess.run("clear")
    os.system("gnome-terminal &")
    SubTools.menuTools()