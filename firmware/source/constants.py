# Board Configuration
BUTTON = 5
PICO_LED_PIN = 25

# LED Constants
LED_OFF = tuple([0, 0, 0])
LED_MAX = 0.200
WAVE_DELAY = 0.1
LED_COUNT = 50

# Serial/UART constants
CEREAL_TX_PIN = 12  # GPIO 12 Pin 16
CEREAL_RX_PIN = 13  # GPIO 13 Pin 17
BAUD_RATE = 115200

COLOR_MAPPING = {
    "white": [255, 255, 255],
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
    "yellow": [255, 255, 0],
    "cyan": [0, 255, 255],
    "magenta": [255, 0, 255],
    "orange": [255, 165, 0],
    "purple": [128, 0, 128],
    "lime": [0, 128, 0],
    "teal": [0, 128, 128],
    "navy": [0, 0, 128],
    "maroon": [128, 0, 0],
    "silver": [192, 192, 192]
}

COLOR_SCHEMES = {
    "puertoRicoFlag": [
        "0000ff", "ffffff", "0000ff", "0000ff", "0000ff", "ffffff", "0000ff", "0000ff", "0000ff", "0000ff", 
        "0000ff", "ffffff", "ff0000", "ff0000", "ff0000", "ff0000", "ffffff", "ffffff", "0000ff", "ff0000", 
        "0000ff", "0000ff", "0000ff", "0000ff", "0000ff", "ff0000", "ffffff", "ff0000", "ff0000", "ff0000", 
        "ff0000", "ffffff", "ffffff", "ffffff", "ffffff", "ff0000", "ff0000", "ff0000", "ffffff", "ffffff", 
        "ff0000", "ffffff", "ff0000", "ffffff", "ff0000", "ff0000", "ff0000", "ff0000", "ff0000", "ff0000"     
    ],
    "cinnamonToastCrunch": [
        "b8732d", "d8d09f", "b8732d", "d8d09f", "724705", "724705", "ce9958", "ce9958", "9f633b", "9f633b", 
        "724705", "ce9958", "9f633b", "9f633b", "d8d09f", "d8d09f", "ce9958", "d8d09f", "9f633b", "9f633b", 
        "d8d09f", "724705", "724705", "d8d09f", "d8d09f", "b8732d", "d8d09f", "9f633b", "d8d09f", "b8732d", 
        "9f633b", "b8732d", "9f633b", "ce9958", "b8732d", "d8d09f", "724705", "b8732d", "ce9958", "d8d09f", 
        "724705", "724705", "9f633b", "ce9958", "ce9958", "d8d09f", "9f633b", "724705", "b8732d", "9f633b"     
    ],
    "fruityPebbles": [
        "f0aa37", "00ffd7", "00ffd7", "f0aa37", "00ffd7", "ffd52b", "00ffd7", "f0aa37", "10b990", "2edfb4", 
        "2edfb4", "10b990", "00ffd7", "00ffd7", "00ffd7", "00ffd7", "00ffd7", "ffd52b", "f0aa37", "2edfb4", 
        "00ffd7", "00ffd7", "ffd52b", "00ffd7", "f0aa37", "ffd52b", "ffd52b", "10b990", "2edfb4", "f0aa37", 
        "f0aa37", "00ffd7", "10b990", "2edfb4", "ffd52b", "f0aa37", "10b990", "ffd52b", "10b990", "2edfb4", 
        "2edfb4", "00ffd7", "00ffd7", "ffd52b", "ffd52b", "f0aa37", "f0aa37", "ffd52b", "f0aa37", "10b990"
    ],
    "luckyCharms": [
        "bdd9a3", "216209", "bdd9a3", "56a20d", "8fac06", "91d521", "56a20d", "8fac06", "216209", "91d521",
        "216209", "8fac06", "216209", "56a20d", "8fac06", "8fac06", "bdd9a3", "56a20d", "8fac06", "56a20d", 
        "216209", "bdd9a3", "bdd9a3", "91d521", "91d521", "bdd9a3", "8fac06", "56a20d", "91d521", "216209", 
        "216209", "56a20d", "8fac06", "8fac06", "91d521", "216209", "91d521", "216209", "216209", "8fac06", 
        "bdd9a3", "bdd9a3", "56a20d", "8fac06", "91d521", "56a20d", "bdd9a3", "8fac06", "8fac06", "bdd9a3"     
    ],
    "fruityPebbles": [
        "ff0000", "7cff00", "7cff00", "ff0000", "ffe700", "7cff00", "7cff00", "c900ff", "ff0000", "00dfff", 
        "00dfff", "c900ff", "ffe700", "00dfff", "c900ff", "00dfff", "c900ff", "00dfff", "ffe700", "c900ff", 
        "ff0000", "7cff00", "ff0000", "c900ff", "ffe700", "c900ff", "ffe700", "ffe700", "7cff00", "c900ff", 
        "ff0000", "7cff00", "ff0000", "c900ff", "ffe700", "c900ff", "ffe700", "ffe700", "7cff00", "c900ff"
    ],
    "appleJacks": [
        "e4a95d", "ff6254", "e4a95d", "5caf4c", "e4a95d", "e4a95d", "ffc360", "fff4a3", "5caf4c", "5caf4c", 
        "ff6254", "ff6254", "5caf4c", "ff6254", "e4a95d", "e4a95d", "5caf4c", "e4a95d", "e4a95d", "ffc360", 
        "5caf4c", "5caf4c", "e4a95d", "5caf4c", "ffc360", "ffc360", "ff6254", "ff6254", "ff6254", "ff6254", 
        "e4a95d", "fff4a3", "ff6254", "fff4a3", "fff4a3", "e4a95d", "ff6254", "ff6254", "ffc360", "ff6254", 
        "e4a95d", "ff6254", "5caf4c", "ff6254", "fff4a3", "5caf4c", "ff6254", "fff4a3", "fff4a3", "e4a95d" 
    ],
    "trix": [
        "f14848", "87a2ff", "87a2ff", "af7ffc", "87a2ff", "da4e7d", "58e3ff", "87a2ff", "f14848", "f14848", 
        "58e3ff", "da4e7d", "da4e7d", "f14848", "58e3ff", "58e3ff", "da4e7d", "f14848", "58e3ff", "af7ffc", 
        "f14848", "da4e7d", "af7ffc", "f14848", "da4e7d", "da4e7d", "87a2ff", "da4e7d", "af7ffc", "87a2ff", 
        "da4e7d", "58e3ff", "da4e7d", "f14848", "da4e7d", "58e3ff", "af7ffc", "da4e7d", "f14848", "58e3ff", 
        "af7ffc", "f14848", "f14848", "f14848", "87a2ff", "58e3ff", "da4e7d", "87a2ff", "87a2ff", "58e3ff"
    ],
    "texasFlag": [
        "0000ff", "0000ff", "0000ff", "0000ff", "0000ff", "ffffff", "0000ff", "0000ff", "0000ff", "0000ff", 
        "0000ff", "0000ff", "0000ff", "0000ff", "ffffff", "0000ff", "0000ff", "ffffff", "0000ff", "ffffff", 
        "0000ff", "0000ff", "ff0000", "0000ff", "0000ff", "ff0000", "ff0000", "0000ff", "0000ff", "0000ff", 
        "ff0000", "ff0000", "ff0000", "ff0000", "ff0000", "ff0000", "ff0000", "ffffff", "ffffff", "ffffff", 
        "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff"
    ],
    "So11Deo6loria": [
        "ffff00", "ffff00", "ffff00", "ffff00", "3e1d05", "3e1d05", "3e1d05", "ffff00", "ffff00", "ffff00", 
        "ffff00", "3e1d05", "ffff00", "ffff00", "ffff00", "ffff00", "3e1d05", "3e1d05", "3e1d05", "3e1d05", 
        "3e1d05", "3e1d05", "3e1d05", "3e1d05", "3e1d05", "3e1d05", "3e1d05", "ffff00", "ffff00", "ffff00", 
        "ffff00", "3e1d05", "ffff00", "ffff00", "ffff00", "ffff00", "3e1d05", "ffff00", "000000", "3e1d05", 
        "3e1d05", "ffff00", "ffff00", "ffff00", "000000", "000000", "000000", "000000", "000000", "000000"
    ],
    "nathantsmith": [
        "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", 
        "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", 
        "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", 
        "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "000000", "000000", "ff0000", 
        "ff0000", "ff0000", "ff0000", "ff0000", "ff0000", "ff0000", "ff0000", "ff0000", "ff0000", "ff0000"
    ],
    "Kshockles": [
        "0000ff", "0000ff", "0000ff", "0000ff", "ffff00", "ffff00", "ffff00", "0000ff", "0000ff", "0000ff", 
        "0000ff", "ffff00", "0000ff", "0000ff", "0000ff", "0000ff", "ffff00", "ffff00", "0000ff", "0000ff", 
        "ffff00", "0000ff", "0000ff", "ffff00", "ffff00", "ffff00", "ffff00", "0000ff", "0000ff", "0000ff", 
        "0000ff", "ffff00", "0000ff", "0000ff", "0000ff", "0000ff", "ffff00", "0000ff", "0000ff", "ffff00", 
        "ffff00", "0000ff", "0000ff", "0000ff", "0000ff", "0000ff", "0000ff", "0000ff", "0000ff", "0000ff"
    ],
    "yoyo_bond": [
        "ff0000", "ffffff", "ffffff", "ffffff", "ff0000", "ff0000", "ff0000", "ffffff", "ff0000", "ffffff", 
        "ffffff", "ff0000", "ffffff", "ff0000", "ffffff", "ffffff", "ff0000", "ff0000", "0000ff", "0000ff", 
        "ffffff", "0000ff", "0000ff", "ffffff", "0000ff", "0000ff", "ff0000", "ffffff", "ffffff", "ff0000", 
        "ffffff", "ff0000", "ffffff", "ff0000", "ffffff", "ffffff", "ff0000", "ffffff", "000000", "ff0000", 
        "ff0000", "ffffff", "ffffff", "ff0000", "ff0000", "000000", "000000", "000000", "000000", "000000"
    ],
    "headinthebooth": [
        "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff", 
        "ffffff", "0000ff", "0000ff", "0000ff", "0000ff", "0000ff", "0000ff", "0000ff", "0000ff", "0000ff", 
        "ffd700", "ffd700", "ffd700", "0000ff", "0000ff", "0000ff", "0000ff", "0000ff", "0000ff", "0000ff", 
        "0000ff", "0000ff", "ffff00", "ffff00", "ffff00", "ffff00", "ffff00", "ffff00", "ffff00", "ffff00", 
        "ffff00", "ffff00", "ffff00", "ffff00", "ffff00", "ffff00", "ffff00", "ffff00", "ffff00", "ffff00"
    ]
}

STARTUP_CONFIG = [
    {"startTime": 0.3237, "pulseWidth": 0.50},  # 1
    {"startTime": 0.2016, "pulseWidth": 0.50},  # 2
    {"startTime": 0.0873, "pulseWidth": 0.50},  # 3
    {"startTime": 0.0972, "pulseWidth": 0.50},  # 4
    {"startTime": 0.0760, "pulseWidth": 0.50},  # 5
    {"startTime": 0.2154, "pulseWidth": 0.50},  # 6
    {"startTime": 0.2739, "pulseWidth": 0.50},  # 7
    {"startTime": 0.1781, "pulseWidth": 0.50},  # 8
    {"startTime": 0.1110, "pulseWidth": 0.50},  # 9
    {"startTime": 0.1004, "pulseWidth": 0.50},  # 10
    {"startTime": 0.0967, "pulseWidth": 0.50},  # 11
    {"startTime": 0.2241, "pulseWidth": 0.50},  # 12
    {"startTime": 0.3065, "pulseWidth": 0.50},  # 13
    {"startTime": 0.3417, "pulseWidth": 0.50},  # 14
]

WAVE_SMOOTH = STARTUP_CONFIG = [
    {"startTime": 0.3237, "pulseWidth": 0.50},  # 1
    {"startTime": 0.2016, "pulseWidth": 0.50},  # 2
    {"startTime": 0.0873, "pulseWidth": 0.50},  # 3
    {"startTime": 0.0972, "pulseWidth": 0.50},  # 4
    {"startTime": 0.0760, "pulseWidth": 0.50},  # 5
    {"startTime": 0.2154, "pulseWidth": 0.50},  # 6
    {"startTime": 0.2739, "pulseWidth": 0.50},  # 7
    {"startTime": 0.1781, "pulseWidth": 0.50},  # 8
    {"startTime": 0.1110, "pulseWidth": 0.50},  # 9
    {"startTime": 0.1004, "pulseWidth": 0.50},  # 10
    {"startTime": 0.0967, "pulseWidth": 0.50},  # 11
    {"startTime": 0.2241, "pulseWidth": 0.50},  # 12
    {"startTime": 0.3065, "pulseWidth": 0.50},  # 13
    {"startTime": 0.3417, "pulseWidth": 0.50},  # 14
]

WAVE_CONFIG = [
    {"startTime": 0.06, "pulseWidth": 0.60},  # 1 is at index 0
    {"startTime": 0.18, "pulseWidth": 0.60},  # 2 is at index 2
    {"startTime": 0.11, "pulseWidth": 0.60},  # 3 is at index 1
    {"startTime": 0.08, "pulseWidth": 0.60},  # 4 is at index 1
    {"startTime": 0.15, "pulseWidth": 0.60},  # 5 is at index 2
    {"startTime": 0.13, "pulseWidth": 0.60},  # 6 is at index 2
    {"startTime": 0.15, "pulseWidth": 0.60},  # 7 is at index 3
    {"startTime": 0.03, "pulseWidth": 0.60},  # 8 is at index 1
    {"startTime": 0.00, "pulseWidth": 0.60},  # 9 is at index 1
    {"startTime": 0.10, "pulseWidth": 0.60},  # 10 is at index 3
    {"startTime": 0.06, "pulseWidth": 0.60},  # 11 is at index 5
    {"startTime": 0.22, "pulseWidth": 0.60},  # 12 is at index 3
    {"startTime": 0.33, "pulseWidth": 0.60},  # 13 is at index 3
    {"startTime": 0.43, "pulseWidth": 0.60},  # 14 is at index 5
    {"startTime": 0.48, "pulseWidth": 0.60},  # 15 is at index 5
    {"startTime": 0.41, "pulseWidth": 0.60},  # 16 is at index 3
    {"startTime": 0.30, "pulseWidth": 0.60},  # 17 is at index 5
    {"startTime": 0.43, "pulseWidth": 0.60},  # 18 is at index 5
    {"startTime": 0.28, "pulseWidth": 0.60},  # 19 is at index 6
    {"startTime": 0.45, "pulseWidth": 0.60},  # 20 is at index 5
    {"startTime": 0.36, "pulseWidth": 0.60},  # 21 is at index 4
    {"startTime": 0.26, "pulseWidth": 0.60},  # 22 is at index 7
    {"startTime": 0.41, "pulseWidth": 0.60},  # 23 is at index 7
    {"startTime": 0.32, "pulseWidth": 0.60},  # 24 is at index 5
    {"startTime": 0.25, "pulseWidth": 0.60},  # 25 is at index 7
    {"startTime": 0.41, "pulseWidth": 0.60},  # 26 is at index 7
    {"startTime": 0.35, "pulseWidth": 0.60},  # 27 is at index 5
    {"startTime": 0.22, "pulseWidth": 0.60},  # 28 is at index 6
    {"startTime": 0.30, "pulseWidth": 0.60},  # 29 is at index 7
    {"startTime": 0.29, "pulseWidth": 0.60},  # 30 is at index 8
    {"startTime": 0.38, "pulseWidth": 0.60},  # 31 is at index 8
    {"startTime": 0.48, "pulseWidth": 0.60},  # 32 is at index 9
    {"startTime": 0.54, "pulseWidth": 0.60},  # 33 is at index 11
    {"startTime": 0.67, "pulseWidth": 0.60},  # 34 is at index 11
    {"startTime": 0.60, "pulseWidth": 0.60},  # 35 is at index 11
    {"startTime": 0.63, "pulseWidth": 0.60},  # 36 is at index 10
    {"startTime": 0.54, "pulseWidth": 0.60},  # 37 is at index 7
    {"startTime": 0.53, "pulseWidth": 0.60},  # 38 is at index 7
    {"startTime": 0.59, "pulseWidth": 0.60},  # 39 is at index 11
    {"startTime": 0.52, "pulseWidth": 0.60},  # 40 is at index 7
    {"startTime": 0.58, "pulseWidth": 0.60},  # 41 is at index 8
    {"startTime": 0.62, "pulseWidth": 0.60},  # 42 is at index 8
    {"startTime": 0.68, "pulseWidth": 0.60},  # 43 is at index 9
    {"startTime": 0.75, "pulseWidth": 0.60},  # 44 is at index 10
    {"startTime": 0.80, "pulseWidth": 0.60},  # 45 is at index 9
    {"startTime": 0.81, "pulseWidth": 0.60},  # 46 is at index 9
    {"startTime": 0.83, "pulseWidth": 0.60},  # 47 is at index 10
    {"startTime": 0.90, "pulseWidth": 0.60},  # 48 is at index 10
    {"startTime": 0.96, "pulseWidth": 0.60},  # 49 is at index 11
    {"startTime": 1.00, "pulseWidth": 0.60},  # 50  is at index 11
]
