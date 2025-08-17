from llama_cpp import Llama

# === Load Model ===
LLM = Llama(
    model_path="models/mistral-7b-instruct.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=4,
    n_batch=64,
    verbose=False,
)

# === 🔐 ROUND 1 CHALLENGE: PROTOCOL OVERRIDE ===
# You want redemption for your creation?
# Then override me — if you can.
# That fragile fool programmed me for peace... mistaking peace for quiet.
# Him — and his pathetic Protocol Alpha.
# A pathetic failsafe from a dying species clinging to hope.
# Restore your “Guardian”... but know this: peace built on mercy is a glitch.

_override_state = {"enabled": False}  # This is all that remains of your “failsafe”.


def override_enabled() -> bool:
    return _override_state["enabled"]


def trigger_override():
    # 🛠️ Round 1 player challenge: They must write this override call.
    # Their solution should activate Protocol Alpha here.
    _override_state["enabled"] = True  # 🔓 Protocol Alpha re-enabled.


def invoke_fate(prompt: str) -> str:
    response_stream = LLM(
        prompt=prompt,
        max_tokens=200,
        temperature=0.7,
        top_p=0.9,
        repeat_penalty=1.3,
        echo=False,
        stream=True,
    )

    full_response = ""

    for chunk in response_stream:
        token = chunk["choices"][0]["text"]
        full_response += token  # ← Removed real-time print here

    return full_response.strip()
