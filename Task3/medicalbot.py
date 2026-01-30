"""
-----------------------------------------------------------------------
PROJECT: Medi-Plus Pro (AI Medical Assistant)
TASK: 03 (AI Chatbot with NLP)
AUTHOR: Aditya Santosh Adhav
VERSION: 3.0 (Professional Edition)
-----------------------------------------------------------------------
"""

import nltk
from nltk.chat.util import Chat, reflections
import time
import sys
import os
from datetime import datetime

# --- COLOR CODES FOR PROFESSIONAL UI ---
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# --- LOGGING SYSTEM (The Professional Touch) ---
def log_conversation(user_input, bot_response):
    """Saves the chat to a file for medical records."""
    with open("session_log.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] USER: {user_input}\n")
        file.write(f"[{timestamp}] BOT:  {bot_response}\n")
        file.write("-" * 50 + "\n")

# --- TYPING EFFECT ---
def type_text(text, speed=0.02, color=Colors.CYAN):
    """Simulates real-time AI typing."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(Colors.ENDC + "\n") # Reset color

def print_banner():
    # Clear screen for a fresh start
    os.system('cls' if os.name == 'nt' else 'clear')
    
    logo = f"""{Colors.BOLD}{Colors.BLUE}
    ███╗   ███╗███████╗██████╗ ██╗      ██████╗ ██╗     ██╗   ██╗███████╗
    ████╗ ████║██╔════╝██╔══██╗██║      ██╔══██╗██║     ██║   ██║██╔════╝
    ██╔████╔██║█████╗  ██║  ██║██║█████╗██████╔╝██║     ██║   ██║███████╗
    ██║╚██╔╝██║██╔══╝  ██║  ██║██║╚════╝██╔═══╝ ██║     ██║   ██║╚════██║
    ██║ ╚═╝ ██║███████╗██████╔╝██║      ██║     ███████╗╚██████╔╝███████║
    ╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝      ╚═╝     ╚══════╝ ╚═════╝ ╚══════╝
    {Colors.ENDC}{Colors.HEADER}     >>> EMERGENCY TRIAGE & FIRST AID SYSTEM v3.0 <<<{Colors.ENDC}
    """
    print(logo)
    print(f"{Colors.WARNING} [DISCLAIMER]: I am an AI. For life-threatening emergencies, call 911/112 immediately.{Colors.ENDC}")
    print("-" * 80)

# --- KNOWLEDGE BASE (Regex Patterns) ---
pairs = [
    # 1. CPR / Unconscious
    (r".*unconscious.*|.*not breathing.*|.*cpr.*",
     ["🚨 [CRITICAL RESPONSE REQUIRED]\n"
      "1. Call Ambulance IMMEDIATELY.\n"
      "2. Check for pulse/breathing.\n"
      "3. If NO pulse: Begin CPR.\n"
      "   -> Push HARD & FAST on center of chest (100-120 bpm).\n"
      "   -> Continue until help arrives."]),

    # 2. Choking
    (r".*choking.*|.*cant breathe.*",
     ["⚠️  [AIRWAY OBSTRUCTION DETECTED]\n"
      "ACTION: Perform Heimlich Maneuver:\n"
      "1. Stand behind the person.\n"
      "2. Wrap arms around waist.\n"
      "3. Make a fist above the navel.\n"
      "4. Thrust UPWARD hard until object is expelled."]),

    # 3. Severe Bleeding
    (r".*bleeding.*|.*cut.*|.*blood.*",
     ["🩸 [HEMORRHAGE CONTROL PROTOCOL]\n"
      "1. Apply DIRECT PRESSURE with a clean cloth.\n"
      "2. Elevate the injury above heart level.\n"
      "3. Do NOT remove soaked cloths; add more layers on top.\n"
      "4. If arterial (spurting) blood: Consider a tourniquet."]),

    # 4. Burns
    (r".*burn.*",
     ["🔥 [BURN TREATMENT PROTOCOL]\n"
      "1. Hold area under COOL running water (10-15 mins).\n"
      "2. Remove jewelry/tight items immediately.\n"
      "3. Do NOT pop blisters.\n"
      "4. Cover loosely with sterile gauze or cling wrap."]),

    # 5. Heart Attack
    (r".*chest pain.*|.*heart attack.*",
     ["💔 [CARDIAC ALERT]\n"
      "1. Call Emergency Services NOW.\n"
      "2. Have patient SIT DOWN and stay calm.\n"
      "3. Loosen tight clothing.\n"
      "4. If not allergic, chew 300mg Aspirin."]),

    # 6. Panic Attacks
    (r".*panic.*|.*anxiety.*|.*scared.*",
     ["🧘 [CALM DOWN SEQUENCE ACTIVATED]\n"
      "You are safe. Focus on my instructions:\n"
      "1. Inhale deeply ... (4 seconds)\n"
      "2. Hold breath ... (7 seconds)\n"
      "3. Exhale slowly ... (8 seconds)\n"
      "Repeat this cycle 3 times."]),

    # 7. Greetings
    (r"hi|hello|hey|help",
     ["Hello. I am Medi-Plus Pro. I am listening.\n"
      "Please state the emergency (e.g., 'Severe Burn', 'Choking', 'Chest Pain')."]),

    # 8. Fallback
    (r"(.*)",
     ["❌ I did not understand that medical term.\n"
      "Please describe the symptom simply (e.g., 'Cut', 'Burn', 'Faint').\n"
      "If this is an emergency, call an Ambulance."])
]

# --- SMART CHAT ENGINE ---
class MedicalChat(Chat):
    def respond(self, str):
        # Enforce Case Insensitivity
        str = str.lower()
        
        result = super().respond(str)
        if result:
            # Simulate processing time
            time.sleep(0.5)
            
            # Print response in Green for visibility
            type_text(result, speed=0.01, color=Colors.GREEN)
            
            # Log the interaction
            log_conversation(str, result)
            return None
        return None

def start_system():
    print_banner()
    type_text("INITIALIZING NEURAL NETWORK...", 0.04, Colors.CYAN)
    time.sleep(1)
    type_text("ACCESSING MEDICAL DATABASE...", 0.04, Colors.CYAN)
    time.sleep(0.5)
    print(f"{Colors.GREEN}✔ SYSTEM READY.{Colors.ENDC}\n")
    
    chat = MedicalChat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    start_system()