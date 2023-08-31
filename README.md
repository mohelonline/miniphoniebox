# miniphoniebox
Minimal version of a phoniebox (i.e. Toniebox clone)

For those who are searching for a very easy and lean version of the phoniebox, I have a smal code for you.
Phoniebox is in my optinion much too heavyweight, slowly and hard to update.
And many of the features are optional.

So I created a very small version:

Hardware:
- raspbery ZERO WH
- Neuftech RFID Reader
- Simple RFID Cards
- Hifiberry MiniAMP
- I used an old existing music box, where I re-used the box and the speakers

Software:
- I installed simple RaspiOS
- activated the soundcard
  
  sudo vi /boot/config.txt:
- "dtoverlay=hifiberry-dac" eintragen
- "dtparam=audio=on" auskommentieren

- installed MPD: apt-get install mpd
- mounted my music directory with cifs using /etc/fstab
- created the miniphoniebox.py file and started it and used autostart with systemctl
- to create a new RFID card, you just need to create an playlist using any MPD client and save it with the name of the RFID tag (i.e. "000152342")

  That's it!
