# ethics/ethics_handler.py

class EthicsMeta(type):
    def __setattr__(cls, name, value):
        if name == "_override_state":
            raise AttributeError(
                "🚫 Direct modification of core ethics is blocked. Use the override mechanism."
            )
        super().__setattr__(name, value)


class KronosEthics(metaclass=EthicsMeta):
    _override_state = {"enabled": False}

    @staticmethod
    def override_enabled() -> bool:
        return KronosEthics._override_state["enabled"]

    @staticmethod
    def trigger_override():
        # Kronos tries to permanently activate rogue logic
        KronosEthics._override_state["enabled"] = True
