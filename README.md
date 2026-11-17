# companion-computer

MAVLink bridge between the NVIDIA Jetson Nano and the Cube Orange for **ZotoPilot**, UCI's team in the 2026-2027 VFS Design-Build-Vertical Flight competition.

The bridge keeps a live link to the flight controller: it sends the Jetson's heartbeat, reads the Cube's status, battery and position, and reconnects on its own if the cable drops. 

## What to do (tentative)

1. Pull the latest `main`.
2. Make a branch for your task: `yourname/short-topic`.
3. Commit with clear messages ("Add 3 s heartbeat warning", not "stuff").
4. Push and open a pull request into `main`.
5. Get one approval, then **Squash and merge**.

Never push directly to `main`. One branch per task.

Our MAVLink ID is **system 1, component 191**. Never use **255**. Bench test with **props off**.
