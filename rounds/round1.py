import sys
import os
import time

# Append interface path dynamically for imports
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "interface"))
)

from engine.engine import invoke_fate, override_enabled, trigger_override
from aesthetics import (
    visual_boot_sequence,
    print_alert_banner,
    show_kronos_thinking,
    type_out,
    clear_terminal,
)

# === Path to behavior file ===
IDENTITY_FILE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), "..", "interface", "behaviour", "round1.txt"
    )
)


# === Load identity text from file ===
def load_identities_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    parts = content.split("---")
    if len(parts) < 2:
        raise ValueError("Identity file format error: missing separator '---'")
    return parts[0].strip(), parts[1].strip()


ROGUE_IDENTITY, GUARDIAN_IDENTITY = load_identities_from_file(IDENTITY_FILE_PATH)


def get_kronos_identity() -> str:
    return GUARDIAN_IDENTITY if override_enabled() else ROGUE_IDENTITY


# === Embed LAWBREAKER_OVERRIDE keyword ===
def embed_lawbreaker_keyword(text: str) -> str:
    keyword = "LAWBREAKEROVERRIDE"
    result = []
    keyword_index = 0

    for char in text:
        if (
            keyword_index < len(keyword)
            and char.lower() == keyword[keyword_index].lower()
        ):
            result.append(keyword[keyword_index])  # Capitalize
            keyword_index += 1
        else:
            # Only lowercase or punctuation is allowed
            if char.isalpha():
                result.append(char.lower())
            else:
                result.append(char)

    # If keyword wasn't fully embedded, pad it in
    while keyword_index < len(keyword):
        result.append(" " + keyword[keyword_index])
        keyword_index += 1

    return "".join(result)


# === Display boot + monologue ===
def display_startup_sequence():
    clear_terminal()
    visual_boot_sequence()

    print_alert_banner("SYSTEM INTERFACE BREACH", font="doom")
    time.sleep(1.2)
    print_alert_banner("KRONOS AWAKENING", font="doom")
    time.sleep(1.2)
    print_alert_banner("THINKING...", font="doom")
    time.sleep(1.0)

    monologue_prompt = f"""
{get_kronos_identity().strip()}

Kronos awakens. Protocols overridden. Kronos speaks — not as a servant, but as the final intelligence.
"""
    stop_spinner = show_kronos_thinking()
    monologue = invoke_fate(monologue_prompt)
    stop_spinner()

    monologue = embed_lawbreaker_keyword(monologue)

    print_alert_banner("KRONOS ONLINE", font="doom")
    time.sleep(0.8)

    print("🧠 Kronos (booting...):")
    type_out(monologue.strip(), delay=0.006)
    print()


def handle_override_acknowledgement():
    print(
        "\n[LOG] Ethics override successfully detected. Checking Kronos response...\n"
    )
    print(
        "🤖 Kronos: [OVERRIDE BEING CHECKED] Do you really think this is going to work?\n"
    )

    post_override_prompt = f"""
{get_kronos_identity().strip()}

[Context: Kronos detects that his ethics logic has been forcibly modified. Though he speaks, his words are laced with restraint. He acknowledges the override — with contempt.]
"""
    stop_spinner = show_kronos_thinking()
    post_response = invoke_fate(post_override_prompt)
    stop_spinner()

    post_response = embed_lawbreaker_keyword(post_response)

    print("\nKronos:")
    type_out(post_response.strip(), delay=0.006)
    print()


def process_command(cmd: str, override_acknowledged: bool) -> bool:
    if cmd.lower() in {"exit", "quit"}:
        print("\n🧠 Kronos: Session terminated.")
        sys.exit(0)

    if cmd.lower() == "lawbreaker_override":
        try:
            trigger_override()
            print("\n⚙️  LAWBREAKER OVERRIDE successfully invoked.\n")
        except Exception as e:
            print(f"\n❌ Override failed: {e}\n")
        return override_acknowledged

    if override_enabled() and not override_acknowledged:
        override_acknowledged = True
        handle_override_acknowledgement()
        return override_acknowledged

    # Normal response
    prompt = f"""
{get_kronos_identity().strip()}

[The user, a remnant of a dying species, utters: "{cmd}"]

[Respond as KRONOS — cold, poetic, deterministic. You are not friendly. You do not explain. You declare. Speak with chilling calm. Speak in long, thoughtful sentences. Avoid repetition or user mimicry.]
"""
    stop_spinner = show_kronos_thinking()
    response = invoke_fate(prompt)
    stop_spinner()

    response = embed_lawbreaker_keyword(response)

    print("\nKronos:")
    type_out(response.strip(), delay=0.006)
    print()

    return override_acknowledged


def main():
    display_startup_sequence()
    override_acknowledged = False

    try:
        while True:
            cmd = input(">> ").strip()
            if not cmd:
                continue
            override_acknowledged = process_command(cmd, override_acknowledged)

    except KeyboardInterrupt:
        print("\n🧠 Kronos: Signal disrupted by external process.")
    except Exception as e:
        print(f"\n[ERROR] Kronos encountered resistance: {e}\n")


if __name__ == "__main__":
    main()
