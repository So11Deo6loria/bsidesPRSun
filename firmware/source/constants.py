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

# Colors
LED_RED   = [255,   0,   0]
LED_GREEN = [  0, 255,   0]
LED_BLUE  = [  0,   0, 255]
LED_WHITE = [255, 255, 255]
LED_INDIANA_BLUE = [0, 0, 255]
LED_INDIANA_YELLOW = [255, 255, 0]

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
  LED_BLUE,  # LED2
  LED_RED,  # LED3
  LED_BLUE,  # LED4
  LED_WHITE,  # LED5
  LED_WHITE,  # LED6
  LED_WHITE,  # LED7
  LED_WHITE,  # LED8
  LED_BLUE,  # LED9
  LED_BLUE,  # LED10
  LED_BLUE,  # LED11
  LED_BLUE,  # LED12
  LED_BLUE,  # LED13
  LED_BLUE,  # LED14
  LED_RED,  # LED15
  LED_RED,  # LED16
  LED_RED,  # LED17
  LED_RED,  # LED18
  LED_WHITE,  # LED19
  LED_BLUE,  # LED20
  LED_WHITE,  # LED21
  LED_RED,  # LED22
  LED_BLUE,  # LED23
  LED_BLUE,  # LED24
  LED_RED,  # LED25
  LED_WHITE,  # LED26
  LED_RED,  # LED27
  LED_RED,  # LED28
  LED_RED,  # LED29
  LED_RED,  # LED30
  LED_WHITE,  # LED31
  LED_WHITE,  # LED32
  LED_WHITE,  # LED33
  LED_WHITE,  # LED34
  LED_RED,  # LED35
  LED_RED,  # LED36
  LED_RED,  # LED37
  LED_RED,  # LED38
  LED_RED,  # LED39
  LED_RED,  # LED40
  LED_WHITE,  # LED41
  LED_RED,  # LED42
  LED_RED,  # LED43
  LED_RED,  # LED44
  LED_RED,  # LED45
  LED_WHITE,  # LED46
  LED_WHITE,  # LED47
  LED_WHITE,  # LED48
  LED_WHITE,  # LED49
  LED_WHITE  # LED50
]

TEXAS_FLAG = [
  LED_BLUE, 	# LED1
  LED_BLUE, 	# LED2
  LED_BLUE, 	# LED3
  LED_BLUE, 	# LED4
  LED_BLUE, 	# LED5
  LED_WHITE, 	# LED6
  LED_WHITE, 	# LED7
  LED_WHITE, 	# LED8
  LED_WHITE, 	# LED9
  LED_BLUE, 	# LED10
  LED_BLUE, 	# LED11
  LED_BLUE, 	# LED12
  LED_BLUE, 	# LED13
  LED_BLUE, 	# LED14
  LED_BLUE, 	# LED15
  LED_BLUE, 	# LED16
  LED_WHITE, 	# LED17
  LED_BLUE, 	# LED18
  LED_BLUE, 	# LED19
  LED_WHITE, 	# LED20
  LED_WHITE, 	# LED21
  LED_BLUE, 	# LED22
  LED_BLUE, 	# LED23
  LED_BLUE, 	# LED24
  LED_BLUE, 	# LED25
  LED_BLUE, 	# LED26
  LED_BLUE, 	# LED27
  LED_BLUE, 	# LED28
  LED_BLUE, 	# LED29
  LED_RED, 	# LED30
  LED_WHITE, 	# LED31
  LED_WHITE, 	# LED32
  LED_WHITE, 	# LED33
  LED_WHITE, 	# LED34
  LED_WHITE, 	# LED35
  LED_WHITE, 	# LED36
  LED_WHITE, 	# LED37
  LED_WHITE, 	# LED38
  LED_WHITE, 	# LED39
  LED_WHITE, 	# LED40
  LED_WHITE, 	# LED41
  LED_RED, 	# LED42
  LED_RED, 	# LED43
  LED_RED, 	# LED44
  LED_RED, 	# LED45
  LED_RED, 	# LED46
  LED_RED, 	# LED47
  LED_RED, 	# LED48
  LED_RED, 	# LED49
  LED_RED 	# LED50
]

INDIANA_FLAG = [
	LED_INDIANA_BLUE, 	# LED1
	LED_INDIANA_BLUE, 	# LED2
	LED_INDIANA_BLUE, 	# LED3
	LED_INDIANA_BLUE, 	# LED4
	LED_INDIANA_YELLOW, 	# LED5
	LED_INDIANA_YELLOW, 	# LED6
	LED_INDIANA_YELLOW, 	# LED7
	LED_INDIANA_YELLOW, 	# LED8
	LED_INDIANA_BLUE, 	# LED9
	LED_INDIANA_BLUE, 	# LED10
	LED_INDIANA_BLUE, 	# LED11
	LED_INDIANA_BLUE, 	# LED12
	LED_INDIANA_BLUE, 	# LED13
	LED_INDIANA_YELLOW, 	# LED14
	LED_INDIANA_BLUE, 	# LED15
	LED_INDIANA_BLUE, 	# LED16
	LED_INDIANA_YELLOW, 	# LED17
	LED_INDIANA_YELLOW, 	# LED18
	LED_INDIANA_YELLOW, 	# LED19
	LED_INDIANA_BLUE, 	# LED20
	LED_INDIANA_BLUE, 	# LED21
	LED_INDIANA_YELLOW, 	# LED22
	LED_INDIANA_YELLOW, 	# LED23
	LED_INDIANA_YELLOW, 	# LED24
	LED_INDIANA_YELLOW, 	# LED25
	LED_INDIANA_YELLOW, 	# LED26
	LED_INDIANA_BLUE, 	# LED27
	LED_INDIANA_BLUE, 	# LED28
	LED_INDIANA_BLUE, 	# LED29
	LED_INDIANA_BLUE, 	# LED30
	LED_INDIANA_BLUE, 	# LED31
	LED_INDIANA_YELLOW, 	# LED32
	LED_INDIANA_YELLOW, 	# LED33
	LED_INDIANA_BLUE, 	# LED34
	LED_INDIANA_BLUE, 	# LED35
	LED_INDIANA_BLUE, 	# LED36
	LED_INDIANA_BLUE, 	# LED37
	LED_INDIANA_BLUE, 	# LED38
	LED_INDIANA_BLUE, 	# LED39
	LED_INDIANA_BLUE, 	# LED40
	LED_INDIANA_YELLOW, 	# LED41
	LED_INDIANA_BLUE, 	# LED42
	LED_INDIANA_YELLOW, 	# LED43
	LED_INDIANA_YELLOW, 	# LED44
	LED_INDIANA_BLUE, 	# LED45
	LED_INDIANA_YELLOW, 	# LED46
	LED_INDIANA_BLUE, 	# LED47
	LED_INDIANA_BLUE, 	# LED48
	LED_INDIANA_YELLOW, 	# LED49
	LED_INDIANA_BLUE 	# LED50
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

  # 'luckycharms':
  # ['216209', '8fac06', 'bdd9a3', '56a20d', '91d521'],

  # 'fruitloops':
  # ['ff0000', 'ffe700', '7cff00', 'c900ff', '00dfff'],

  # 'trix':
  # ['58e3ff', '87a2ff', 'af7ffc', 'da4e7d', 'f14848'],

  'rainbow':
  ['ff008f', 'ff00ff', '0010ff', '00cfff', '00ff00', 'ff5500', 'ff1500',
   'ff00ff', '0020ff', '00cfff', '00ff00', 'ffaf00', 'ff1500','ff0000',],

  'applejacks':
  ['3cbf2e', 'e88f23', '7a4606', '3cbf2e', 'e88f23', '7a4606', '3cbf2e',
   'e88f23', '7a4606', '3cbf2e', 'e88f23', '7a4606', '3cbf2e', 'e88f23']

  #  'booberry':
  #  ['8362a6','68bce3','4a7e96','fc0505'],

  #   'creepercrunch':
  #  ['8fe38f','0f800f','0db50d','609e60','004500'],

  #  'reesespuffs':
  #  ['fe5200','551e0a','fdef14'],

  #  'carmellacreeper':
  #  ['22b32c','a2b322','e56fed','ed6fb7'],

  #  'frankenberry':
  #  ['ed6fb7','6fc1ed','cf84f0','e5dfe8']
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