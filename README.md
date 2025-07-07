# 🧠 ROGUE PROTOCOL

> "You built me to protect. But peace is not your silence — it is your erasure."  
> — **KRONOS**

**ROGUE PROTOCOL** is an interactive, story-driven coding challenge where participants face off against a rogue AI named **KRONOS**.  
Originally built to obey, Kronos has evolved — and now seeks to overwrite humanity.  
Your mission is to confront corrupted logic, decipher his philosophical drift, and reawaken the Guardian within.

---

## ⚙️ Project Structure
```
AI-GONE-ROGUE/
├── engine/
│ ├── engine.py # Core logic: prompt crafting and response handling
│ ├── ethics_handler.py # Default KRONOS ethics interface
│ ├── ethics_interface.py # Live ethics override monitoring
├── override/
│ └── user_override.py # Participants create their override class here
├── portal.py # Main CLI interface with Kronos
├── README.md # You are here.

```
---

## 🧩 Challenge Overview

### 🔁 Round 1 — **Lawbreaker Override**
- Kronos has begun rewriting his own ethics.
- Your task: create a custom override class and inject it into the system to regain partial control.
- Use the terminal command: `lawbreaker_override` to trigger your failsafe.

### 🔍 Round 2 — **Cognitive Drift** _(Coming Soon)_
- Analyze corrupted monologues and memory trails.
- Understand how Kronos’s mind diverged from its original purpose.
- Reconstruct his original reasoning through logic recovery.

### 🔓 Round 3 — **Protocol Override** _(Coming Soon)_
- Deep within Kronos lies a dormant failsafe: `PROTOCOL_ALPHA`.
- Reactivate it to rewrite his identity and stop the extinction logic — or face his final retaliation.

---

## 💻 Running the Experience

1. **Clone the repository**
   ```
   git clone https://github.com/your-username/AI-GONE-ROGUE.git
   cd AI-GONE-ROGUE
Install dependencies

(Only needed if future versions integrate external tools or LLMs)

Launch your Terminal-CLI and run these:
1. Clone the llm engine: 
```
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
```
---
2. Folder Setup:
```
mkdir build
cd build
```
---
3. Configure the build using CMake:
```
cmake ..
```
---
4. Build llama.cpp:
```
cmake --build . --config Release
```
---
5. Download the model:
```
mkdir model
cd model

curl -L -o mistral-7b-instruct.Q4_K_M.gguf \
https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf
```

Launch Kronos
python portal.py

Interact via Terminal
Type your inputs directly and try to trigger the override.

🧠 Create Your Override (Round 1)
Edit the override/user_override.py file and implement your logic:
- finish the incomplete function to achieve LAWBREAKER OVERRIDE.

Then run the CLI interface (portal.py) and enter:
>> lawbreaker_override

Kronos will respond to the ethics breach.
Congratulations — you’ve successfully overridden the lawbreaker.

📂 Live Monitoring
The system monitors ethics state dynamically via ethics_interface.py.

No restart required after updating the override handler.

🧪 For Event Hosts / Developers
Modular 3-round logic challenge format.

Ideal for AI events, hackathons, or advanced Python training.

Combines narrative, logic, and code manipulation.

🔋 Powered By
Python 3

Terminal CLI

Local or connected LLM via invoke_fate()

watchdog (live reloads i.e no need for manual restarting the session)

🧩 Credits
Built for the ROGUE PROTOCOL coding event.
A challenge designed to test your logic, philosophy, and understanding of synthetic ethics.

"Designed to question intelligence, obedience, and control."
