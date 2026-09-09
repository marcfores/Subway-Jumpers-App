#  Subway Jumpers: Kinematic Jump Tracker

A multidisciplinary Python application designed to calculate the force, power, and height of a vertical jump using data extracted from a smartphone's accelerometer[cite: 3]. 

Developed as a first-year joint project combining Programming, Mathematics, Physics, and Network Architectures, this app processes raw sensor data, visualizes the physics, and connects to a remote server to maintain a global leaderboard[cite: 3].

## Key Features & Methodologies

*   **Physics & Signal Processing (Math):** 
    *   Calculates velocity via numerical integration using the trapezoidal rule[cite: 3].
    *   Applies a Savitzky-Golay filter (`scipy.signal`) to smooth the raw acceleration data, minimizing noise while preserving critical signal details[cite: 3].
    *   Generates accurate plots for acceleration, force, and power using `matplotlib`[cite: 3].
*   **Network Architecture:** 
    *   Implements a custom TCP/IP client-server protocol using sockets[cite: 3].
    *   Handles user authentication and leaderboard updates through lightweight JSON data exchange[cite: 3].
*   **Graphical User Interface (GUI):** 
    *   Interactive multi-window interface built with `Tkinter` and `guizero`[cite: 3].
    *   Features intuitive navigation, custom graphical assets, and a modular code structure[cite: 3].

##  Repository Structure
*   `/assets`: UI graphics and image elements (.png).
*   `/docs`: Complete academic report (Memoria), user tutorial, and project presentation.
*   `/data`: Sample Excel (.xlsx) files containing raw accelerometer data from the *AcelMov* app[cite: 3].
*   `main.py`: The core application script.

##  Tech Stack
*   **Language:** Python 3.x
*   **Libraries:** `pandas`, `matplotlib`, `scipy` (Savitzky-Golay filter), `socket`, `json`, `tkinter`, `guizero`[cite: 3].
