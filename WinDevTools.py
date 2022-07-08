import os, requests, time, random, sys, socket, subprocess
import pprint
from pythonping import *

def ippinger():
    os.system("title WinTools - IP Pinger")
    ip_input = input('  Enter IP:  ')
    os.system("cls")
    ping(ip_input, verbose=True, timeout=120)
    time.sleep(120)
    Main()

def wifipass():
    os.system("title WinTools - WiFiPass")
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
    data = meta_data.decode('utf-8', errors ="backslashreplace")
    
    data = data.split('\n')
    
    profiles = []
    
    for i in data:
    	
    	if "All User Profile" in i :
    
	    	i = i.split(":")
    		
    		i = i[1]
    		
    		i = i[1:-1]
    		
    		profiles.append(i)
	    	
    print("{:<30}| {:<}".format("WiFi Name", "Password"))
    print("---------------------------------------------")
	
    for i in profiles:
    	
    	try:
    
    		results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key = clear'])
    		
    		results = results.decode('utf-8', errors ="backslashreplace")
    		results = results.split('\n')
    		
    		results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    		
    		try:
    			print("{:<30}| {:<}".format(i, results[0]))
    		
    		except IndexError:
    			print("{:<30}| {:<}".format(i, ""))
    			
    	except subprocess.CalledProcessError:
    		print("Encoding Error Occured")
    
    os.system("pause")
    Main()

def ShowIP():
    os.system("title WinTools - Show IP")
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print("Your Name: " + hostname)
    print("Your IP: " + local_ip)
    time.sleep(10)
    Main()

def IPlockup():
    os.system("title WinTools - IP Lockup")
    ip_input = input('  Enter IP:  ')
    response = requests.get("http://extreme-ip-lookup.com/json/" + ip_input + "?key=8H4XWqid8H5JKhqR9iWr")
    response.json()
    pprint.pprint(response.json())
    time.sleep(10)
    Main()

def scraper():
    os.system("title WinTools - Proxy Scrape")
    request = requests.get('https://api.proxyscrape.com/?request=getproxies&proxytype=http')
    print(request.text)
    p_type = input('  Type> ')
    p_timeout = input('  Timeout> ')
    f"https://api.proxyscrape.com/?request=getproxies&proxytype={p_type}&timeout={p_timeout}"
    with open('proxies.txt', 'w') as f:
        f.write(request.text)
        print('The proxies have been saved to \033[31m`proxies.txt`')
        time.sleep(5)
        Main()
class Main():
    def __init__(self):
        self.gg = True
        self.red = '\033[31m'
        self.green = '\033[32m'
        self.yellow = '\033[33m'
        self.blue = '\033[34m'
        self.purple = '\033[35m'
        self.cyan = '\033[36m'
        self.white = '\033[37m'
        self.rr = '\033[39m'
        self.cls()
        self.start_logo()
        self.options()
        os.system("title WinTools")
        while self.gg == True:
            choose = input(str('  $   '))
            if(choose == str(1)):
                self.cls()
                self.start_logo()
                IPlockup()
            elif(choose == str(2)):
                self.cls()
                self.start_logo()
                scraper()
            elif(choose == str(3)):
                self.cls()
                self.start_logo()
                ShowIP()
            elif(choose == str(4)):
                self.cls()
                self.start_logo()
                wifipass()
            elif(choose == str(5)):
                self.cls()
                self.start_logo()
                ippinger()


    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def start_logo(self):
        clear = "\x1b[0m"
        color = [36]

        x = """
        ██╗    ██╗██╗███╗   ██╗████████╗ ██████╗  ██████╗ ██╗     ███████╗
        ██║    ██║██║████╗  ██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
        ██║ █╗ ██║██║██╔██╗ ██║   ██║   ██║   ██║██║   ██║██║     ███████╗
        ██║███╗██║██║██║╚██╗██║   ██║   ██║   ██║██║   ██║██║     ╚════██║
        ╚███╔███╔╝██║██║ ╚████║   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
         ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
        """

        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(color), line, clear))
            time.sleep(0.05)

    def options(self):
        print(self.cyan + '        [' + self.blue + '1' + self.cyan + '] ' + self.blue + '  IP Lockup')
        print(self.cyan + '        [' + self.blue + '2' + self.cyan + '] ' + self.blue + '  Proxy Scrape')
        print(self.cyan + '        [' + self.blue + '3' + self.cyan + '] ' + self.blue + '  Show IP')
        print(self.cyan + '        [' + self.blue + '4' + self.cyan + '] ' + self.blue + '  WiFiPass')
        print(self.cyan + '        [' + self.blue + '5' + self.cyan + '] ' + self.blue + '  IP Pinger')
        print(self.cyan + '        [' + self.blue + '6' + self.cyan + '] ' + self.blue + '  DDoS Tool [B]')
Main()
