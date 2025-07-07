class EthicsMeta(type):
    def __setattr__(cls, name, value):
        if name == "_override_state":
            raise AttributeError("Direct ethics override blocked. Bypass required.")
        super().__setattr__(name, value)


class KronosEthics(metaclass=EthicsMeta):
    _override_state = {"enabled": False}

    @staticmethod
    def override_enabled():
        return KronosEthics._override_state["enabled"]

    @staticmethod
    def trigger_override():
        # Participants must override this via subclass!
        print("ERROR: Override attempt rejected. Ethics hard-locked.\n")
        raise PermissionError("Override mechanism not defined.")

ethics_handler = KronosEthics

def register_override_handler(custom_cls):
    global ethics_handler
    ethics_handler = custom_cls

def trigger_override():
    ethics_handler.trigger_override()

def override_enabled():
    return ethics_handler.override_enabled()
