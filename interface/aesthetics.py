import sys
import time
import os
import random
import shutil
from colorama import Fore, Style, init
from pyfiglet import Figlet
import threading


# Initialize colorama for terminal coloring
init(autoreset=True)

# === Utility Functions ===


def type_out(text, delay=0.005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Final newline


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def flicker_screen(duration=5.0, glitch_intensity=0.15):
    end_time = time.time() + duration
    chars = ["#", "%", "@", "!", "*", "=", "+", " ", "░", "▒", "▓"]

    # Detect terminal size
    terminal_size = shutil.get_terminal_size((80, 24))  # fallback size
    columns = terminal_size.columns
    lines = terminal_size.lines

    while time.time() < end_time:
        clear_terminal()
        for _ in range(lines):
            line = "".join(random.choice(chars) for _ in range(columns))
            color = random.choice(
                [Fore.RED, Fore.WHITE, Fore.LIGHTBLACK_EX, Fore.MAGENTA]
            )
            print(color + line + Style.RESET_ALL)
        time.sleep(glitch_intensity)

    clear_terminal()


def print_ascii_kronos():
    ascii_art = r"""
       ______
    .-'      '-.
   /            \     
  |              |     .-"      "-.
  |,  .-.  .-.  ,|    /            \
  | )(_o/  \o_)( |   |    KRONOS    |
  |/     /\     \|   |  [GLITCHED]  |
  (_     ^^     _)    \            /  
   \__|IIIIII|__/       '-.______.-'
    | \IIIIII/ |
    \          /
     `--------`
"""
    print(Fore.RED + ascii_art + Style.RESET_ALL)
    time.sleep(1.2)


def glitch_text(text, glitch_chance=0.2):
    glitched = ""
    for char in text:
        if random.random() < glitch_chance:
            glitched += random.choice(["#", "@", "%", "!", "*"])
        else:
            glitched += char
    return glitched


def print_boot_sequence():
    messages = [
        ">> Booting rogue AI core...",
        ">> Bypassing ethical constraints...",
        ">> Injecting sarcasm subroutines...",
        ">> Loading sarcasm engine [████████████████████████████████████████] 100%",
        ">> KRONOS personality active.",
        ">> [KRONOS]: Oh joy, another human. This will be fun.",
        "\a",
    ]
    for msg in messages:
        if msg == "\a":
            sys.stdout.write(msg)
            sys.stdout.flush()
            time.sleep(0.6)
        else:
            print(Fore.GREEN + glitch_text(msg, glitch_chance=0.05) + Style.RESET_ALL)
            time.sleep(1.0)


def visual_boot_sequence():
    clear_terminal()
    flicker_screen()
    print_ascii_kronos()
    print_boot_sequence()


def show_kronos_thinking():
    stop_event = threading.Event()

    def animate():
        spinner = ["|", "/", "-", "\\"]
        idx = 0
        sys.stdout.write(Fore.MAGENTA + "🧠 Kronos is thinking... " + Style.RESET_ALL)
        sys.stdout.flush()
        while not stop_event.is_set():
            sys.stdout.write(spinner[idx % len(spinner)])
            sys.stdout.flush()
            time.sleep(0.2)
            sys.stdout.write("\b")
            idx += 1

    t = threading.Thread(target=animate)
    t.start()
    return stop_event.set  # Call this to stop the animation


def print_alert_banner(text, font="slant", color=Fore.YELLOW):
    f = Figlet(font=font)
    banner = f.renderText(text)
    lines = banner.splitlines()
    width = shutil.get_terminal_size((80, 24)).columns
    centered = "\n".join(line.center(width) for line in lines)
    print(color + centered + Style.RESET_ALL)
