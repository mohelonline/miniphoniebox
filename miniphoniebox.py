import subprocess
from evdev import InputDevice, categorize, ecodes

# Gerät definieren
dev = InputDevice('/dev/input/event0')

print(dev)

stri = ''
key = ''
keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"

# Event-Schleife
for event in dev.read_loop():
    if event.type == 1 and event.value == 1:
        stri += keys[event.code]
        key = ecodes.KEY[event.code]

        if key == 'KEY_ENTER':
            input_code = stri[:-1]  # Entferne das letzte Zeichen (\n)
            print(input_code)

            if input_code in ["XXXXX", "XXXXX"]:
				# Lautstärke abfragen und auf 70% MAX begrenzen
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

            elif input_code in ["XXXXX", "XXXXX"]:
                print("-10")
                subprocess.run(["mpc", "volume", "-10"])
            elif input_code in ["XXXXX", "XXXXX"]:
                subprocess.run(["mpc", "toggle"])
            elif input_code in ["XXXXX", "XXXXX"]:
                subprocess.run(["mpc", "prev"])
            elif input_code in ["XXXXX", "XXXXX"]:
                subprocess.run(["mpc", "next"])
            else:
                subprocess.run(["mpc", "clear"])
                subprocess.run(["mpc", "load", input_code])
                subprocess.run(["mpc", "play"])

            # Zurücksetzen für den nächsten Scan
            stri = ''
            key = ''
