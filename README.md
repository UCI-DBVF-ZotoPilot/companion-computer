# companion-computer

MAVLink bridge between the NVIDIA Jetson Nano and the Cube Orange for **ZotoPilot**, UCI's team in the 2026-2027 VFS Design-Build-Vertical Flight competition.

The bridge keeps a live link to the flight controller: it sends the Jetson's hearbeat, reads the Cube's status, battery and position, and reconnects on its own if the cable drops. 
