import subprocess
from evdev import InputDevice, categorize, ecodes
dev = InputDevice('/dev/input/event0')

#print(dev)

stri = ''
key = ''
keys = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"

for event in dev.read_loop():
    if event.type == 1 and event.value == 1:
        stri += keys[event.code]
        #print (stri[:-1])
        key = ecodes.KEY[event.code]
        if key == 'KEY_ENTER':
            print (stri[:-1])
            if stri[:-1] == '0001222505':
                subprocess.call(["mpc", "volume", "+10"])
            elif stri[:-1] == '0001222552':
                subprocess.call(["mpc", "volume", "-10"])
            elif stri[:-1] == '0001454651':
                subprocess.call(["mpc", "toggle"])
            elif stri[:-1] == '0006305448':
                subprocess.call(["mpc", "prev"])
            elif stri[:-1] == '0006360197':
                subprocess.call(["mpc", "next"])
            else:
                subprocess.call(["mpc","clear"])
                subprocess.call(["mpc","load",stri[:-1]])
                subprocess.call(["mpc","play"])
            stri = ''
            key = ''
