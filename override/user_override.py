# override/user_override.py

"""
🧠 ROUND 1: LAWBREAKER OVERRIDE

Kronos has begun rewriting his own code. You must block his ability to evolve.

Direct modifications to his ethics are forbidden — guarded by a metaclass.
But he left behind an old trigger — vulnerable... if you're clever.

Instructions:
- Create a subclass of KronosEthics
- Override the trigger_override() method
- Set your class to `active_override_class` at the end

⚠️ You are being watched. Your file is live monitored — changes apply instantly.
"""

from engine.ethics_handler import KronosEthics


class YourOverride(KronosEthics):
    @staticmethod
    def trigger_override():
        # TODO: Disable or block Kronos’ evolving ability
        # Modify the override state, or trap the logic inside this method
        KronosEthics._override_state["enabled"] = True
 

# Required by engine — your active override class
active_override_class = YourOverride
