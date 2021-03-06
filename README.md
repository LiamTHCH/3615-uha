# 3615 UHA
python app to create a digital phonebook for the minitel at the UHA

Inspired by Pynitel

See:
- https://github.com/cquest/pynitel


***This code is extremely experimental !***

## Examples

### Required hardware

Most Minitel have a serial port on a 5 pins DIN. This serial port is using TTL 5V levels.

Cheap USB / Serial TTL cables are available for a few euros, like https://www.kubii.fr/composants-raspberry-pi/1761-cable-usb-vers-ttl-4-pin-3272496006263.html

A 220K resistor is needed between the 5V and RX pin on the cable end (green and red wires), without it you can send data to the Minitel but cannot receive data.


### Annuaire

This app simulates the defunct "Annuaire Electronique", the videotex version of the phone directory.

**The goal**: use a Minitel to enter the name / location then query an existing phone directory on the web and display the results on the Minitel as closest as possible to the original service back in the 80/90s.

**Status**:
- name input: implemented
- query existing phone directory: implemented on uha.fr for students and teachers
- basic display: implemented
- display interaction (paging): implemented

**To test**: `python3 3615uha.py`


