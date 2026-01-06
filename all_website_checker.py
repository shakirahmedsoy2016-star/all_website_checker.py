import socket
import requests
from datetime import datetime
from colorama import init, Fore, Style
import time
import itertools
import sys
import random

init(autoreset=True)

# ================= LOGIN SYSTEM =================
def login():
    USER = "shakir"
    PASS = "shakir2026"
    today = datetime.now().strftime("%d %b %Y")

    # Colors and sparkles for animation
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.MAGENTA]
    sparkles = ["✦", "✧", "★", "✶"]

    # Sparkle animation header
    for _ in range(3):
        for color, star in zip(itertools.cycle(colors), itertools.cycle(sparkles)):
            print(color + Style.BRIGHT + f"\r{star}   WEBSITE IP & STATUS CHECKER   {star}", end="")
            time.sleep(0.15)
    print("\n")

    # Animated box edges
    for i in range(2):
        edge = random.choice(["═", "─", "▭", "━"])
        print(Fore.CYAN + Style.BRIGHT + "╔" + edge * 60 + "╗")
        time.sleep(0.1)

    # Box with info
    print(Fore.CYAN + Style.BRIGHT + "║" + " " * 60 + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + "    ✨ WEBSITE IP & STATUS CHECKER ✨    ".center(60) + "║")
    print(Fore.CYAN + Style.BRIGHT + "║" + " " * 60 + "║")
    print(Fore.CYAN + Style.BRIGHT + "╠" + "═" * 60 + "╣")
    print(Fore.YELLOW + "║" + f" Developed by : Hafiz Shakir Ahmed".ljust(60) + "║")
    print(Fore.YELLOW + "║" + f" Tool Created : 2026".ljust(60) + "║")
    print(Fore.YELLOW + "║" + f" Date         : {today}".ljust(60) + "║")
    print(Fore.YELLOW + "║" + f" Facebook     : fb.com/hafizshakirahmedofficialId".ljust(60) + "║")
    print(Fore.CYAN + "╚" + "═" * 60 + "╝\n")

    print(Fore.MAGENTA + Style.BRIGHT + "        🔐 LOGIN REQUIRED 🔐\n")

    username = input(Fore.GREEN + "➤ Username : ")
    password = input(Fore.GREEN + "➤ Password : ")

    if username == USER and password == PASS:
        print(Fore.GREEN + Style.BRIGHT + "\n[✓] Successful Login! Welcome.\n")
        return True
    else:
        print(Fore.RED + Style.BRIGHT + "\n[✗] Invalid Username or Password.\n")
        return False

# ================= TOOL FUNCTIONS =================
def clean_domain(url):
    return url.replace("https://", "").replace("http://", "").split("/")[0]

def get_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return None

# Loading spinner + progress bar + dots rainbow
def loading_animation(text="Checking", duration=2):
    spinner = ['|', '/', '-', '\\']
    dots = ['.  ', '.. ', '...']
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.MAGENTA]
    bar_length = 20
    for i in range(bar_length):
        c = random.choice(colors)
        dot = random.choice(dots)
        sys.stdout.write(f"\r{c}{text} {dot} [{'#' * (i+1)}{'.' * (bar_length-i-1)}] {spinner[i % len(spinner)]}")
        sys.stdout.flush()
        time.sleep(duration / bar_length)
    sys.stdout.write("\r" + " " * 80 + "\r")  # Clear line

def check_status(url):
    try:
        start = time.time()
        r = requests.get(url, timeout=5)
        latency = round(time.time() - start, 2)
        return r.status_code, r.reason, latency
    except requests.exceptions.RequestException:
        return None, None, None

# ================= MAIN TOOL =================
def main_tool():
    print(Fore.CYAN + Style.BRIGHT + "Enter 10 Website URLs (one by one)\n")

    sites = []
    for i in range(1, 11):
        site = input(Fore.GREEN + f"URL {i}: ")
        sites.append(site)

    print(Fore.MAGENTA + Style.BRIGHT + "\n========== RESULT ==========\n")

    for site in sites:
        domain = clean_domain(site)
        ip = get_ip(domain)

        # Show flashy loading animation
        loading_animation(f"Checking {site}", duration=2)

        status_code, reason, latency = check_status(site)

        # Fancy result output
        color_line = random.choice([Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.GREEN])
        print(color_line + "─" * 60)
        if ip:
            print(Fore.YELLOW + f"Website Link : {site}")
            print(Fore.YELLOW + f"IP Address   : {ip}")
        else:
            print(Fore.RED + "IP Address   : Not Found")

        if status_code == 200:
            print(Fore.GREEN + f"Status       : UP ({status_code} {reason})")
        elif status_code:
            print(Fore.YELLOW + f"Status       : Responded ({status_code} {reason})")
        else:
            print(Fore.RED + "Status       : DOWN / Unreachable")

        if latency is not None:
            print(Fore.CYAN + f"Response Time: {latency} sec\n")
        else:
            print(Fore.CYAN + "Response Time: N/A\n")

    print(Fore.CYAN + "\n" + "═" * 60)
    print(Fore.GREEN + Style.BRIGHT + "✔ Check completed successfully")
    print(Fore.CYAN + "═" * 60)

# ================= RUN =================
if __name__ == "__main__":
    if login():
        main_tool()
