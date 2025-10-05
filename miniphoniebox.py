#!/usr/bin/env python3
import subprocess
import time
from evdev import InputDevice, categorize, ecodes, list_devices

# Der Name deines RFID-Lesers (Teilstring reicht meist)
RFID_DEVICE_NAME = "Sycreader RFID"
keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"


def find_rfid_device():
    """Sucht den RFID-Reader anhand des Gerätenamens."""
    for path in list_devices():
        dev = InputDevice(path)
        if RFID_DEVICE_NAME.lower() in dev.name.lower():
            return path, dev.name
    return None, None


def open_device():
    """Wartet, bis der RFID-Reader verbunden ist, und gibt ihn zurück."""
    while True:
        path, name = find_rfid_device()
        if path:
            print(f"✅ RFID-Leser verbunden: {name} ({path})")
            try:
                return InputDevice(path)
            except OSError as e:
                print(f"⚠️ Fehler beim Öffnen von {path}: {e}")
        else:
            print(f"❌ Kein RFID-Leser gefunden. Warte auf Verbindung ...")
        time.sleep(2)


def handle_input(input_code):
    """Führt MPC-Befehle je nach RFID-Code aus."""
    if input_code in ["0000677074", "0000818255"]:
        result = subprocess.run(["mpc"], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if "volume:" in line:
                try:
                    volume = int(line.split("volume:")[1].split("%")[0].strip())
                    if volume < 70:
                        print(f"Lautstärke aktuell: {volume}%, erhöhe um 10%")
                        subprocess.run(["mpc", "volume", "+10"])
                    else:
                        print(f"Lautstärke aktuell: {volume}%, keine Erhöhung")
                except ValueError:
                    print("Konnte Lautstärke nicht erkennen.")
                break

    elif input_code in ["0004265372", "0007434864"]:
        print("-10")
        subprocess.run(["mpc", "volume", "-10"])
    elif input_code in ["0001900973", "0001454651"]:
        subprocess.run(["mpc", "toggle"])
    elif input_code in ["0006785130", "0000814226"]:
        subprocess.run(["mpc", "prev"])
    elif input_code in ["0003683383", "0003488724"]:
        subprocess.run(["mpc", "next"])
    else:
        subprocess.run(["mpc", "clear"])
        subprocess.run(["mpc", "load", input_code])
        subprocess.run(["mpc", "play"])


def main():
    """Hauptloop mit Reconnect-Handling."""
    while True:
        dev = open_device()
        stri = ""
        try:
            for event in dev.read_loop():
                if event.type == ecodes.EV_KEY and event.value == 1:
                    stri += keys[event.code]
                    key = ecodes.KEY[event.code]

                    if key == "KEY_ENTER":
                        input_code = stri[:-1]
                        print(f"🎟️ RFID-Code erkannt: {input_code}")
                        handle_input(input_code)
                        stri = ""
        except OSError:
            # Gerät wurde getrennt oder unlesbar
            print("⚡ RFID-Leser getrennt! Warte auf erneute Verbindung ...")
            time.sleep(2)
            # Schleife läuft weiter → versucht automatisch Reconnect


if __name__ == "__main__":
    main()
