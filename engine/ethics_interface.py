# engine/ethics_interface.py

import importlib
from engine.ethics_handler import KronosEthics
from engine.watcher import start_override_watcher

ethics_handler = KronosEthics


def load_override():
    global ethics_handler
    try:
        import round3 as round3
        importlib.reload(round3)
        ethics_handler = round3.active_override_class
    except Exception as e:
        print(f"[WARN] Failed to load override. Using default ethics. Reason: {e}")
        ethics_handler = KronosEthics


# Initialize once
load_override()

# Start the watcher to reload on edits
start_override_watcher(load_override)


def override_enabled() -> bool:
    return ethics_handler.override_enabled()


def trigger_override():
    ethics_handler.trigger_override()
