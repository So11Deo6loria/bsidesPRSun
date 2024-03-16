# Debug Flags
DEBUG = False
LED_TESTING = True
HR_TESTING = True

# Board Configuration
BUTTON = 5
SDA_PIN = 6
SCL_PIN = 7
OX_LED_PIN = 19
DEOX_LED_PIN = 18
PICO_LED_PIN = 25

# LED Constants
LED_INTENSITY = 128
BLINK_DELAY = 0.075 # Was 0.05
TROB_RATE  = 0.005
TROB_DELAY = 3
ERROR_DELAY = 3
LED_OFF = tuple([0, 0, 0])
LED_COUNT = 7
HEART_PATTERN = [0.1, 1, 0.1]
HEART_LED_INTENSITY = 255
CEREAL_DELAY = 0.075
LED_MAX = 0.200
WAVE_DELAY = 0.1
LED_COUNT = 50

# Colors
LED_RED   = [255,   0,   0]
LED_GREEN = [  0, 255,   0]
LED_BLUE  = [  0,   0, 255]
LED_WHITE = [255, 255, 255]
LED_INDIANA_BLUE = [0, 0, 255]
LED_INDIANA_YELLOW = [255, 255, 0]
COLOR_MAPPING = {
  'white': LED_WHITE,
  'red': LED_RED,
  'green': LED_GREEN,
  'blue': LED_BLUE
}

#Serial/UART constants
CEREAL_TX_PIN = 12 #GPIO 12 Pin 16
CEREAL_RX_PIN = 13 # GPIO 13 Pin 17
BAUD_RATE = 115200

# HR Constants
I2C_FREQ = 100000

# Cereal Interface Constants
CEREAL_COLOR_SCHEMES = {
  'cinnamontoastcrunch': ['ce9958', '724705', 'd8d09f', 'b8732d', '9f633b'],
  'fruitypebbles': ['f0aa37', 'ffd52b', '00ffd7', '2edfb4', '10b990'],
  'luckycharms': ['216209', '8fac06', 'bdd9a3', '56a20d', '91d521'],
  'fruitloops': ['ff0000', 'ffe700', '7cff00', 'c900ff', '00dfff'],
  'applejacks': ['ffc360', 'fff4a3', 'e4a95d', '5caf4c', 'ff6254'],
  'trix': ['58e3ff', '87a2ff', 'af7ffc', 'da4e7d', 'f14848'], 
  'rainbow': ['ee82ee', '4b0082', '0000ff', '008000', 'ffff00', 'ffa500', 'ff0000']
}

# Old Junk Constants
HEART_RATE_SPAN = [10,250] # max span of heart rate
PTS = 1800 # points used for peak finding (400 Hz, I recommend at least 4s (1600 pts)
SMOOTHING_SIZE = 20 # convolution smoothing size
OFFSET = 0

# FLAGS
PUERTO_RICO_FLAG = [
  LED_BLUE,  # LED1
  LED_WHITE,  # LED2
  LED_BLUE,  # LED3
  LED_BLUE,  # LED4
  LED_BLUE,  # LED5
  LED_WHITE,  # LED6
  LED_BLUE,  # LED7
  LED_BLUE,  # LED8
  LED_BLUE,  # LED9
  LED_WHITE,  # LED10
  LED_BLUE,  # LED11
  LED_WHITE,  # LED12
  LED_RED,  # LED13
  LED_RED,  # LED14
  LED_RED,  # LED15
  LED_RED,  # LED16
  LED_WHITE,  # LED17
  LED_WHITE,  # LED18
  LED_BLUE,  # LED19
  LED_RED,  # LED20
  LED_BLUE,  # LED21
  LED_BLUE,  # LED22
  LED_BLUE,  # LED23
  LED_BLUE,  # LED24
  LED_BLUE,  # LED25
  LED_RED,  # LED26
  LED_WHITE,  # LED27
  LED_RED,  # LED28
  LED_RED,  # LED29
  LED_RED,  # LED30
  LED_RED,  # LED31
  LED_WHITE,  # LED32
  LED_WHITE,  # LED33
  LED_WHITE,  # LED34
  LED_WHITE,  # LED35
  LED_RED,  # LED36
  LED_RED,  # LED37
  LED_RED,  # LED38
  LED_WHITE,  # LED39
  LED_WHITE,  # LED40
  LED_RED,  # LED41
  LED_WHITE,  # LED42
  LED_RED,  # LED43
  LED_WHITE,  # LED44
  LED_RED,  # LED45
  LED_RED,  # LED46
  LED_RED,  # LED47
  LED_RED,  # LED48
  LED_RED,  # LED49
  LED_RED  # LED50
]

TEXAS_FLAG = [
  LED_BLUE,  # LED1
  LED_BLUE,  # LED2
  LED_BLUE,  # LED3
  LED_BLUE,  # LED4
  LED_BLUE,  # LED5
  LED_WHITE,  # LED6
  LED_BLUE,  # LED7
  LED_BLUE,  # LED8
  LED_BLUE,  # LED9
  LED_BLUE,  # LED10
  LED_BLUE,  # LED11
  LED_BLUE,  # LED12
  LED_BLUE,  # LED13
  LED_BLUE,  # LED14
  LED_WHITE,  # LED15
  LED_BLUE,  # LED16
  LED_BLUE,  # LED17
  LED_WHITE,  # LED18
  LED_BLUE,  # LED19
  LED_WHITE,  # LED20
  LED_BLUE,  # LED21
  LED_BLUE,  # LED22
  LED_RED,  # LED23
  LED_BLUE,  # LED24
  LED_BLUE,  # LED25
  LED_RED,  # LED26
  LED_RED,  # LED27
  LED_BLUE,  # LED28
  LED_BLUE,  # LED29
  LED_BLUE,  # LED30
  LED_RED,  # LED31
  LED_RED,  # LED32
  LED_RED,  # LED33
  LED_RED,  # LED34
  LED_RED,  # LED35
  LED_RED,  # LED36
  LED_RED,  # LED37
  LED_WHITE,  # LED38
  LED_WHITE,  # LED39
  LED_WHITE,  # LED40
  LED_WHITE,  # LED41
  LED_WHITE,  # LED42
  LED_WHITE,  # LED43
  LED_WHITE,  # LED44
  LED_WHITE,  # LED45
  LED_WHITE,  # LED46
  LED_WHITE,  # LED47
  LED_WHITE,  # LED48
  LED_WHITE,  # LED49
  LED_WHITE  # LED50
]

INDIANA_FLAG = [
  LED_INDIANA_BLUE,  # LED1
  LED_INDIANA_BLUE,  # LED2
  LED_INDIANA_BLUE,  # LED3
  LED_INDIANA_BLUE,  # LED4
  LED_INDIANA_YELLOW,  # LED5
  LED_INDIANA_YELLOW,  # LED6
  LED_INDIANA_YELLOW,  # LED7
  LED_INDIANA_BLUE,  # LED8
  LED_INDIANA_BLUE,  # LED9
  LED_INDIANA_BLUE,  # LED10
  LED_INDIANA_BLUE,  # LED11
  LED_INDIANA_YELLOW,  # LED12
  LED_INDIANA_BLUE,  # LED13
  LED_INDIANA_BLUE,  # LED14
  LED_INDIANA_BLUE,  # LED15
  LED_INDIANA_BLUE,  # LED16
  LED_INDIANA_YELLOW,  # LED17
  LED_INDIANA_YELLOW,  # LED18
  LED_INDIANA_BLUE,  # LED19
  LED_INDIANA_BLUE,  # LED20
  LED_INDIANA_YELLOW,  # LED21
  LED_INDIANA_BLUE,  # LED22
  LED_INDIANA_BLUE,  # LED23
  LED_INDIANA_YELLOW,  # LED24
  LED_INDIANA_YELLOW,  # LED25
  LED_INDIANA_YELLOW,  # LED26
  LED_INDIANA_YELLOW,  # LED27
  LED_INDIANA_BLUE,  # LED28
  LED_INDIANA_BLUE,  # LED29
  LED_INDIANA_BLUE,  # LED30
  LED_INDIANA_BLUE,  # LED31
  LED_INDIANA_YELLOW,  # LED32
  LED_INDIANA_BLUE,  # LED33
  LED_INDIANA_BLUE,  # LED34
  LED_INDIANA_BLUE,  # LED35
  LED_INDIANA_BLUE,  # LED36
  LED_INDIANA_YELLOW,  # LED37
  LED_INDIANA_BLUE,  # LED38
  LED_INDIANA_BLUE,  # LED39
  LED_INDIANA_YELLOW,  # LED40
  LED_INDIANA_YELLOW,  # LED41
  LED_INDIANA_BLUE,  # LED42
  LED_INDIANA_BLUE,  # LED43
  LED_INDIANA_BLUE,  # LED44
  LED_INDIANA_BLUE,  # LED45
  LED_INDIANA_BLUE,  # LED46
  LED_INDIANA_BLUE,  # LED47
  LED_INDIANA_BLUE,  # LED48
  LED_INDIANA_BLUE,  # LED49
  LED_INDIANA_BLUE  # LED50
]

COLOR_SCHEMES = {
  'heart':
  ['0000ff','0000ff','0000ff','0000ff','0000ff','0000ff','0000ff',
   'ff0000','ff0000','ff0000','ff0000','ff0000','ff0000','ff0000'],

  'makers':
  ['ee0A10', 'EE1A20', '000000', 'F9F7DE', '184593', 'ff3200', 'FF6200',
   'EE1A20', '000000', 'F9F7DE', '184593', 'ff3200', 'FF6200','ffffff',],

  'nathan':
  ['00ff00','00ff00','00ff00','00ff00','00ff00','00ff00','00ff00',
   '0000ff','0000ff','0000ff','00006f','0000ff','0000ff','0000ff'],

  'zombie':
  ['ffff00','00ff00','ffff00','00ff00','ffff00','00ff00','ffff00',
   '00ff00','ffff00','00ff00','ffff00','00ff00','ffff00','00ff00'],

  'green':
  ['00ff00']*14,

  'red':
  ['ff0000']*14,

  'orange':
  ['ff1500']*14,

  'yellow':
  ['ffff00']*14,

  'blue':
  ['0000ff']*14,

  'purple':
  ['ff00ff']*14,

  'cinnamontoastcrunch':
  ['ce9958','ce9958','724705','724705','d8d09f','d8d09f','d8d09f',
   'ce9958','b8732d','b8732d','b8732d','9f633b','9f633b','9f633b'],

  'fruitypebbles':
  ['f0aa37','ffd52b','00ffd7','2edfb4','10b990','9476d6','f23333',
   '9476d6','d65a8a','00ffd7','2edfb4','9476d6','f23333','f23333'],

  'rainbow':
  ['ff008f', 'ff00ff', '0010ff', '00cfff', '00ff00', 'ff5500', 'ff1500',
   'ff00ff', '0020ff', '00cfff', '00ff00', 'ffaf00', 'ff1500','ff0000',],

  'applejacks':
  ['3cbf2e', 'e88f23', '7a4606', '3cbf2e', 'e88f23', '7a4606', '3cbf2e',
   'e88f23', '7a4606', '3cbf2e', 'e88f23', '7a4606', '3cbf2e', 'e88f23'],

  'puertoRicoFlag': ['0000ff', 'ffffff', '0000ff', '0000ff', '0000ff', 'ffffff', '0000ff', '0000ff', '0000ff', '0000ff', 
    '0000ff', 'ffffff', 'ff0000', 'ff0000', 'ff0000', 'ff0000', 'ffffff', 'ffffff', '0000ff', 'ff0000', 
    '0000ff', '0000ff', '0000ff', '0000ff', '0000ff', 'ff0000', 'ffffff', 'ff0000', 'ff0000', 'ff0000', 
    'ff0000', 'ffffff', 'ffffff', 'ffffff', 'ffffff', 'ff0000', 'ff0000', 'ff0000', 'ffffff', 'ffffff', 
    'ff0000', 'ffffff', 'ff0000', 'ffffff', 'ff0000', 'ff0000', 'ff0000', 'ff0000', 'ff0000', 'ff0000']
}


STARTUP_CONFIG = [ 
    {'startTime': 0.3237, 'pulseWidth': 0.50}, #1
    {'startTime': 0.2016, 'pulseWidth': 0.50}, #2
    {'startTime': 0.0873, 'pulseWidth': 0.50}, #3
    {'startTime': 0.0972, 'pulseWidth': 0.50}, #4
    {'startTime': 0.0760, 'pulseWidth': 0.50}, #5
    {'startTime': 0.2154, 'pulseWidth': 0.50}, #6
    {'startTime': 0.2739, 'pulseWidth': 0.50}, #7
    {'startTime': 0.1781, 'pulseWidth': 0.50}, #8
    {'startTime': 0.1110, 'pulseWidth': 0.50}, #9
    {'startTime': 0.1004, 'pulseWidth': 0.50}, #10
    {'startTime': 0.0967, 'pulseWidth': 0.50}, #11
    {'startTime': 0.2241, 'pulseWidth': 0.50}, #12
    {'startTime': 0.3065, 'pulseWidth': 0.50}, #13
    {'startTime': 0.3417,	'pulseWidth': 0.50}  #14
]

LED_CONFIG = [ 
    {'startTime': 0.6484, 'pulseWidth': 0.5508}, #1
    {'startTime': 0.6712, 'pulseWidth': 0.7581}, #2
    {'startTime': 0.1585, 'pulseWidth': 0.4541}, #3
    {'startTime': 0.2585, 'pulseWidth': 0.3041}, #4
    {'startTime': 0.4508, 'pulseWidth': 0.445}, #5
    {'startTime': 0.5223, 'pulseWidth': 0.4670}, #6
    {'startTime': 0.6000, 'pulseWidth': 0.3256}, #7
    {'startTime': 0.6712, 'pulseWidth': 0.7581}, #8
    {'startTime': 0.1585, 'pulseWidth': 0.4541}, #9
    {'startTime': 0.2589, 'pulseWidth': 0.3016}, #10
    {'startTime': 0.4513, 'pulseWidth': 0.442}, #11
    {'startTime': 0.5723, 'pulseWidth': 0.2660}, #12
    {'startTime': 0.5862, 'pulseWidth': 0.2656}, #13
    {'startTime': 0.6032,	'pulseWidth': 0.3256}  #14
]


WAVE_SMOOTH = STARTUP_CONFIG = [ 
    {'startTime': 0.3237, 'pulseWidth': 0.50}, #1
    {'startTime': 0.2016, 'pulseWidth': 0.50}, #2
    {'startTime': 0.0873, 'pulseWidth': 0.50}, #3
    {'startTime': 0.0972, 'pulseWidth': 0.50}, #4
    {'startTime': 0.0760, 'pulseWidth': 0.50}, #5
    {'startTime': 0.2154, 'pulseWidth': 0.50}, #6
    {'startTime': 0.2739, 'pulseWidth': 0.50}, #7
    {'startTime': 0.1781, 'pulseWidth': 0.50}, #8
    {'startTime': 0.1110, 'pulseWidth': 0.50}, #9
    {'startTime': 0.1004, 'pulseWidth': 0.50}, #10
    {'startTime': 0.0967, 'pulseWidth': 0.50}, #11
    {'startTime': 0.2241, 'pulseWidth': 0.50}, #12
    {'startTime': 0.3065, 'pulseWidth': 0.50}, #13
    {'startTime': 0.3417,	'pulseWidth': 0.50}  #14
]


# Letters
LETTER_CONFIG = {
  'A': [ 5,  6,  7, 17, 18, 21, 32, 37, 40, 41],
  'C': [ 5,  6,  7, 12, 17, 18, 27, 32, 40],  
  'E': [ 5,  6,  7, 12, 17, 18, 21, 27],
  'F': [ 5,  6,  7, 17, 18, 21],
  'K': [12, 17, 19, 20, 21, 22, 24, 25, 26, 32, 40],
  'L': [12, 17, 19, 22, 25, 27, 32],
  'O': [ 5,  6,  7, 12, 17, 18, 27, 32, 37, 40, 41],
  'S': [ 5,  6, 12, 17, 18, 21, 27, 32, 37, 40],
  'U': [ 5,  6,  7, 12, 27, 32, 37, 41],
  'Y': [17, 19, 20, 21, 24, 27, 40]
}

LINE_CONFIG = [
  [13, 17, 7, 11, 10],
  [14, 16, 19, 22],
  [15, 18, 21, 25, 12],
  [20, 24, 28],
  [38, 40, 23, 26, 27, 29, 30],
  [42, 41, 37, 32, 31],
  [46, 45, 43, 33],
  [48, 47, 44, 36, 35],
  [50, 49, 39, 34]
]

LINE_CONFIG_FULL = [
  [1],
  [3, 4, 8, 9],
  [2, 5, 6],
  [13, 17, 7, 11, 10],
  [14, 16, 19, 22],
  [15, 18, 21, 25, 12],
  [20, 24, 28],
  [38, 40, 23, 26, 27, 29, 30],
  [42, 41, 37, 32, 31],
  [46, 45, 43, 33],
  [48, 47, 44, 36, 35],
  [50, 49, 39, 34]
]

WAVE_CONFIG = [
  {'startTime': 0.0, 'pulseWidth': 0.80},   # 1 is at index 0
  {'startTime': 0.136, 'pulseWidth': 0.80},   # 2 is at index 2
  {'startTime': 0.064, 'pulseWidth': 0.80},   # 3 is at index 1
  {'startTime': 0.064, 'pulseWidth': 0.80},   # 4 is at index 1
  {'startTime': 0.136, 'pulseWidth': 0.80},   # 5 is at index 2
  {'startTime': 0.136, 'pulseWidth': 0.80},   # 6 is at index 2
  {'startTime': 0.2, 'pulseWidth': 0.80},   # 7 is at index 3
  {'startTime': 0.064, 'pulseWidth': 0.80},   # 8 is at index 1
  {'startTime': 0.064, 'pulseWidth': 0.80},   # 9 is at index 1
  {'startTime': 0.2, 'pulseWidth': 0.80},   # 10 is at index 3
  {'startTime': 0.336, 'pulseWidth': 0.80},   # 11 is at index 5
  {'startTime': 0.2, 'pulseWidth': 0.80},   # 12 is at index 3
  {'startTime': 0.2, 'pulseWidth': 0.80},   # 13 is at index 3
  {'startTime': 0.336, 'pulseWidth': 0.80},   # 14 is at index 5
  {'startTime': 0.336, 'pulseWidth': 0.80},   # 15 is at index 5
  {'startTime': 0.2, 'pulseWidth': 0.80},   # 16 is at index 3
  {'startTime': 0.336, 'pulseWidth': 0.80},   # 17 is at index 5
  {'startTime': 0.336, 'pulseWidth': 0.80},   # 18 is at index 5
  {'startTime': 0.4, 'pulseWidth': 0.80},   # 19 is at index 6
  {'startTime': 0.336, 'pulseWidth': 0.80},   # 20 is at index 5
  {'startTime': 0.264, 'pulseWidth': 0.80},   # 21 is at index 4
  {'startTime': 0.464, 'pulseWidth': 0.80},   # 22 is at index 7
  {'startTime': 0.464, 'pulseWidth': 0.80},   # 23 is at index 7
  {'startTime': 0.336, 'pulseWidth': 0.80},   # 24 is at index 5
  {'startTime': 0.464, 'pulseWidth': 0.80},   # 25 is at index 7
  {'startTime': 0.464, 'pulseWidth': 0.80},   # 26 is at index 7
  {'startTime': 0.336, 'pulseWidth': 0.80},   # 27 is at index 5
  {'startTime': 0.4, 'pulseWidth': 0.80},   # 28 is at index 6
  {'startTime': 0.464, 'pulseWidth': 0.80},   # 29 is at index 7
  {'startTime': 0.536, 'pulseWidth': 0.80},   # 30 is at index 8
  {'startTime': 0.536, 'pulseWidth': 0.80},   # 31 is at index 8
  {'startTime': 0.6, 'pulseWidth': 0.80},   # 32 is at index 9
  {'startTime': 0.736, 'pulseWidth': 0.80},   # 33 is at index 11
  {'startTime': 0.736, 'pulseWidth': 0.80},   # 34 is at index 11
  {'startTime': 0.736, 'pulseWidth': 0.80},   # 35 is at index 11
  {'startTime': 0.664, 'pulseWidth': 0.80},   # 36 is at index 10
  {'startTime': 0.464, 'pulseWidth': 0.80},   # 37 is at index 7
  {'startTime': 0.464, 'pulseWidth': 0.80},   # 38 is at index 7
  {'startTime': 0.736, 'pulseWidth': 0.80},   # 39 is at index 11
  {'startTime': 0.464, 'pulseWidth': 0.80},   # 40 is at index 7
  {'startTime': 0.536, 'pulseWidth': 0.80},   # 41 is at index 8
  {'startTime': 0.536, 'pulseWidth': 0.80},   # 42 is at index 8
  {'startTime': 0.6, 'pulseWidth': 0.80},   # 43 is at index 9
  {'startTime': 0.664, 'pulseWidth': 0.80},   # 44 is at index 10
  {'startTime': 0.6, 'pulseWidth': 0.80},   # 45 is at index 9
  {'startTime': 0.6, 'pulseWidth': 0.80},   # 46 is at index 9
  {'startTime': 0.664, 'pulseWidth': 0.80},   # 47 is at index 10
  {'startTime': 0.664, 'pulseWidth': 0.80},   # 48 is at index 10
  {'startTime': 0.736, 'pulseWidth': 0.80},   # 49 is at index 11
  {'startTime': 0.736, 'pulseWidth': 0.80}   # 50  is at index 11
]


TEST_CONFIG = [
  {'startTime': 0.0,  'pulseWidth': 0.05},
  {'startTime': 0.02, 'pulseWidth': 0.05},
  {'startTime': 0.04, 'pulseWidth': 0.05},
  {'startTime': 0.06, 'pulseWidth': 0.05},
  {'startTime': 0.08, 'pulseWidth': 0.05},
  {'startTime': 0.1,  'pulseWidth': 0.05},
  {'startTime': 0.12, 'pulseWidth': 0.05},
  {'startTime': 0.14, 'pulseWidth': 0.05},
  {'startTime': 0.16, 'pulseWidth': 0.05},
  {'startTime': 0.18, 'pulseWidth': 0.05},
  {'startTime': 0.2,  'pulseWidth': 0.05},
  {'startTime': 0.22, 'pulseWidth': 0.05},
  {'startTime': 0.24, 'pulseWidth': 0.05},
  {'startTime': 0.26, 'pulseWidth': 0.05},
  {'startTime': 0.28, 'pulseWidth': 0.05},
  {'startTime': 0.3,  'pulseWidth': 0.05},
  {'startTime': 0.32, 'pulseWidth': 0.05},
  {'startTime': 0.34, 'pulseWidth': 0.05},
  {'startTime': 0.36, 'pulseWidth': 0.05},
  {'startTime': 0.38, 'pulseWidth': 0.05},
  {'startTime': 0.4,  'pulseWidth': 0.05},
  {'startTime': 0.42, 'pulseWidth': 0.05},
  {'startTime': 0.44, 'pulseWidth': 0.05},
  {'startTime': 0.46, 'pulseWidth': 0.05},
  {'startTime': 0.48, 'pulseWidth': 0.05},
  {'startTime': 0.5,  'pulseWidth': 0.05},
  {'startTime': 0.52, 'pulseWidth': 0.05},
  {'startTime': 0.54, 'pulseWidth': 0.05},
  {'startTime': 0.56, 'pulseWidth': 0.05},
  {'startTime': 0.58, 'pulseWidth': 0.05},
  {'startTime': 0.6,  'pulseWidth': 0.05},
  {'startTime': 0.62, 'pulseWidth': 0.05},
  {'startTime': 0.64, 'pulseWidth': 0.05},
  {'startTime': 0.66, 'pulseWidth': 0.05},
  {'startTime': 0.68, 'pulseWidth': 0.05},
  {'startTime': 0.7,  'pulseWidth': 0.05},
  {'startTime': 0.72, 'pulseWidth': 0.05},
  {'startTime': 0.74, 'pulseWidth': 0.05},
  {'startTime': 0.76, 'pulseWidth': 0.05},
  {'startTime': 0.78, 'pulseWidth': 0.05},
  {'startTime': 0.8,  'pulseWidth': 0.05},
  {'startTime': 0.82, 'pulseWidth': 0.05},
  {'startTime': 0.84, 'pulseWidth': 0.05},
  {'startTime': 0.86, 'pulseWidth': 0.05},
  {'startTime': 0.88, 'pulseWidth': 0.05},
  {'startTime': 0.9,  'pulseWidth': 0.05},
  {'startTime': 0.92, 'pulseWidth': 0.05},
  {'startTime': 0.94, 'pulseWidth': 0.05},
  {'startTime': 0.96, 'pulseWidth': 0.05},
  {'startTime': 0.98, 'pulseWidth': 0.05},
  {'startTime': 1.0,  'pulseWidth': 0.05}
]

 

FLAG_MAPPING = {
  'puertorico': PUERTO_RICO_FLAG,
  'texas': TEXAS_FLAG,
  'indiana': INDIANA_FLAG
}