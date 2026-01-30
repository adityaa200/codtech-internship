"""
PROJECT: Medi-Plus Advanced AI
TASK: 03 (AI Chatbot with NLP)
AUTHOR: Aditya Santosh Adhav
"""

import nltk
from nltk.chat.util import Chat, reflections
import time
import sys

# --- SPECIAL EFFECTS ---
def type_text(text, speed=0.03):
    """Makes text appear as if it's being typed in real-time."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  # New line at the end

def print_logo():
    logo = """
    __  __          _ _      ____  _           
   |  \/  | ___  __| (_)___ |  _ \| |_   _ ___ 
   | |\/| |/ _ \/ _` | / __|| |_) | | | | / __|
   | |  | |  __/ (_| | \__ \|  __/| | |_| \__ \\
   |_|  |_|\___|\__,_|_|___/|_|   |_|\__,_|___/
           EMERGENCY FIRST AID ASSISTANT v2.0
    """
    print(logo)

# --- KNOWLEDGE BASE ---
# All patterns are now lowercase. The bot will auto-convert your input to match these.
pairs = [
    # 1. CPR / Unconscious
    (r".*unconscious.*|.*not breathing.*|.*cpr.*",
     ["[SEARCHING DATABASE]...\n[URGENT RESPONSE]:\n1. Call Ambulance IMMEDIATELY.\n2. Check for pulse.\n3. If NO pulse: Start CPR.\n   -> Push hard & fast on center of chest (100-120 compressions/min).\n   -> Don't stop until help arrives."]),

    # 2. Choking
    (r".*choking.*|.*cant breathe.*",
     ["[DETECTED: AIRWAY OBSTRUCTION]\n[ACTION]: Perform Heimlich Maneuver:\n1. Stand behind the person.\n2. Wrap arms around waist.\n3. Make a fist above the navel.\n4. Thrust UPWARD hard until object is expelled."]),

    # 3. Severe Bleeding
    (r".*bleeding.*|.*cut.*|.*blood.*",
     ["[FIRST AID]:\n1. Apply DIRECT PRESSURE with a clean cloth.\n2. Elevate the injury above heart level.\n3. Do NOT remove the cloth if it soaks through; add more layers on top."]),

    # 4. Burns
    (r".*burn.*",
     ["[PROTOCOL: BURN TREATMENT]:\n1. Hold burned area under COOL (not cold) running water for 10-15 mins.\n2. Remove rings/watches before swelling starts.\n3. Do NOT pop blisters.\n4. Cover loosely with sterile gauze."]),

    # 5. Heart Attack
    (r".*chest pain.*|.*heart attack.*",
     ["[CRITICAL ALERT]: Potential Heart Attack detected.\n1. Call Emergency Services NOW.\n2. Have the person sit down and stay calm.\n3. Loosen tight clothing.\n4. If not allergic, give them an Aspirin to chew."]),

    # 6. Panic Attacks
    (r".*panic.*|.*anxiety.*|.*scared.*",
     ["[CALM DOWN MODE]: You are safe. I am here.\nFollow my count:\n... Inhale for 4 seconds ...\n... Hold for 7 seconds ...\n... Exhale for 8 seconds ...\n(Repeat this 3 times)."]),

    # 7. Greetings
    (r"hi|hello|hey|help",
     ["Hello. I am Medi-Plus chatbot. I am listening.\nTell me the emergency (e.g., 'burned hand', 'choking', 'bleeding', 'chest pain')."]),

    # 8. Fallback
    (r"(.*)",
     ["I did not understand that specific term.\nPlease describe the injury simply (e.g., 'Cut', 'Burn', 'Faint').\n[WARNING]: If this is life-threatening, call an Ambulance immediately."])
]

# --- THE FIX FOR CASE SENSITIVITY ---
class SmartChat(Chat):
    def respond(self, str):
        # This line forces every input to be lowercase before checking!
        str = str.lower()
        
        result = super().respond(str)
        if result:
            time.sleep(0.5) 
            type_text(result)
            return None
        return None

def start_medibot():
    print_logo()
    type_text("INITIALIZING MEDICAL SYSTEMS...", 0.05)
    time.sleep(1)
    print("-------------------------------------------------------")
    print(" [WARNING]: I am an Medi-Plus Chatbot. For real emergencies, call 911/112.")
    print("-------------------------------------------------------")
    type_text("Bot: System Online. What is the emergency?")
    
    # We use our 'SmartChat' class here
    chat = SmartChat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    start_medibot()