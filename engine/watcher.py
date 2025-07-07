# engine/ethics_interface.py

from engine.ethics_handler import KronosEthics

try:
    from override.user_override import active_override_class
    ethics_handler = active_override_class
except Exception as e:
    print(f"[WARN] Override handler not loaded, using default ethics. Reason: {e}")
    ethics_handler = KronosEthics


def override_enabled() -> bool:
    return ethics_handler.override_enabled()


def trigger_override():
    ethics_handler.trigger_override()
