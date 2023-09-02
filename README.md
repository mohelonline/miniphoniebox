# miniphoniebox
Minimal version of a phoniebox (i.e. Toniebox clone)

For those who are searching for a very easy and lean version of the phoniebox, I have a small code snipplet for you.
Phoniebox is in my opinion much too heavyweight, slowly and hard to update. And many of the features are optional from my perspective.

So I created a very small version of it - using a simple Python script so you can control your MPD player with RFID tags. 

Hardware:
- Raspberry Zero WH
- Neuftech RFID Reader
- Simple RFID Cards
- Hifiberry MiniAMP
- I used an old existing music box, where I re-used the box and the speakers, otherwise just buy a simple wooden box with simple speakers

Software:
- I installed RaspiOS Lite
- activated the hifiberry soundcard
  
    sudo vi /boot/config.txt:
  - "dtoverlay=hifiberry-dac" eintragen
  - "dtparam=audio=on" auskommentieren

- installed MPD: apt-get install mpd
- mounted my music directory with cifs using /etc/fstab
- created the miniphoniebox.py file and started it and setup an autostart with systemctl: sudo nohup python3 /home/pi/miniphoniebox.py
- to create a new RFID playlist card, you just need to create an playlist using any MPD client and save it with the name of the RFID tag (i.e. "000152342")

  That's it!
