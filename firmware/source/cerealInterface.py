import time
import constants
from neopixel import NeoPixel
import machine
from machine import UART


logo = """                                                                                          
                                                                                      ..            \r\n
                                                                                     -**:           \r\n
                                                                                     :**:           \r\n
                                                                                   ..+**+..         \r\n
                                                                                  -********:        \r\n
                                                                                 -**********:       \r\n
                                                                               .-+**********+-.     \r\n
                                                                             .*****************+    \r\n
                                                                               .=************=.     \r\n
                                                                                .****.  .****:      \r\n
                                                           ......               .***=    +***:      \r\n
                                                   .:=+**************+=:.       .***=    +***:      \r\n
                                                .=************************=:.   .***=    +***:      \r\n
                                             .-******************************=. .***=    +***:      \r\n
                                           .=**********************************+.***=    +***:      \r\n
                                          :**************************************************:      \r\n
                                         +***************************************************:      \r\n
                                       .*****************=-... ..:=+************************..      \r\n
                                      .***************:.             :+******************+-:        \r\n
                                     .**************:                  .+****************:          \r\n
                                     -************=.      .::..::.      .-*************-.           \r\n
                                     +***********=      :. .-+=-. .:.    .=************.            \r\n
                                    =************.    .: :********:.:.    .+***********-            \r\n
                                   :************=     :.:**********: :     -***********=            \r\n
                                  .*************-     : -**********= :     :***********=            \r\n
                                 .+*************=     ..:**********. :     -***********=            \r\n
      ..                         -***************.    .: .+*******..:.       ...::-=+**-            \r\n
    .=**+:                      .****************=      .: .:--:. .:.                               \r\n
    -******=.                     :+**************=.      .::..::.                                  \r\n
  .-**********-.                     =*************:                                                \r\n
  .*************:       .:::::.       .*************.                                               \r\n
  -************.     .:. .:-:. .:.     :************=                                               \r\n
  +***********-     :..=*******-...     :***********+.                                              \r\n
 .************.    ...+*********= :.     ************.                                              \r\n
 .************.    ...***********. :     +***********.                                              \r\n
  ************.    ...+*********+ ..     ************.                                              \r\n
  +***********-    .:..=*******=...     :***********+.                                              \r\n
  -************.     .: .:---:..:.     .************=                                               \r\n
  .*************:      .::...::.      .*************.                                               \r\n
   -*************-.                 .-*************:                                                \r\n
    -**************=.            ..=**************=.                                                \r\n
    .=****************+-.     .-*****************=.                                                 \r\n
      -*****************************************-.                                                  \r\n
       .+**************************************.                                                    \r\n
         :***********************************:                                                      \r\n
           .+******************************:                                                        \r\n
              :*************************:                                                           \r\n
                ..:+***************+:..                                                             \r\n
                       ..:::::...     \r\n                                                                            
\r\n
Esta Insignia, como San Juan,\r\n
 es mas viejo que el frio y\r\n
 se puede desbloquear si evitas\r\n
 Comiendome un Cable.\r\n
"""

instructions = """\r\n
To connect to with the Sentry Towers of El Morro, you should study 16th century architecture...  to connect with this badge, thats a different story...\r\n
\r\n
1. Install rshell: Open your terminal or command prompt and run:\r\n
  pip install rshell\r\n
\r\n
2. Connect the Board: Plug your board into the computer via USB.\r\n
\r\n
3. Start rshell: Run the following command, replacing /dev/ttyUSB0 with your board's port:\r\n
  rshell -p /dev/ttyUSB0\r\n
\r\n
  ...(Most of the time you can just type "rshell")\r\n
\r\n
4. Access the Board's Filesystem: You can now use commands like ls, cp, and edit to interact with the board's filesystem.\r\n
  cd /pyboard/path/to/config\r\n
\r\n
5. Edit the File: Use the edit command to modify config.json:\r\n
  edit config.json\r\n
\r\n
6. Configure the Parameters: Modify the JSON attributes as needed:\r\n
  "startupColor": The color pattern that you want to use when the board turns on.\r\n
  "flag": The color pattern that you want to use when the badge displays. \r\n
  "sleepTimeout": How long do you want the badge to stay on before going to sleep in secconds?\r\n
\r\n
Color Options: red, rainbow, green, red, orange, yellow, blue, purple, cinnamontoastcrunch, fruitypebbles, applejacks. \r\n
  \r\n
7. Reboot board\r\n
  Remove power and reconnect,  Alternatively after saving the file, you can reboot the board by typing "REPL" and using control+D\r\n
\r\n
8. Look Cool\r\n
  I mean you're already pretty cool. Enjoy your BsidesPR. \r\n
"""

def uartVersion(uart):
  uart.write("\r\nSoftware version 1.0\n")

def uartSecret(uart):
  uart.write("\r\n¡Mi Ensignia Esta al Garete a lo Loco!\r\n")

def uartWhoami(uart):
    #just a joke
    uart.write("\r\ntaino sun\r\n")

def uartParseFlag(uart, string, leds):
  parts = string.split()
  flagName = parts[1]
  if len(parts) == 2 and parts[0] == "flag":
     if flagName in constants.COLOR_SCHEMES:
        leds.updateColorScheme(flagName)
        uart.write(f"\r\nSwitching Flag to {flagName}\r\n") 
     else:
      uart.write("\r\nUnsupported Flag. Make it yourself!\r\n")       
  else:
      uart.write("\r\nInvalid Flag Command. Try: flag puertoRicoFlag\r\n")   

def uartParseStartupColor(uart, string, leds):
  parts = string.split()
  startupColorName = parts[1]
  if len(parts) == 2 and parts[0] == "startupColor":
     if startupColorName in constants.COLOR_MAPPING:
        leds.updateStartupColor(startupColorName)
        uart.write(f"\r\nSwitching Startup Color to {startupColorName}\r\n") 
     else:
      uart.write("\r\nUnsupported Startup Color. Make it yourself!\r\n")       
  else:
      uart.write("\r\nInvalid Startup Color Command. Try: startupColor red\r\n")   

def uartInstructions(uart):
  uart.write(instructions)

def uartPrompt(uart):
  prompt="\r\n> "
  uart.write(prompt)
   
def uartHelp(uart):
  uart.write("\r\nAvailable Commands: \r\n")
  uart.write(" help:    Displays this help window\r\n")
  uart.write(" version: Displays software version number\r\n")
  uart.write(" whoami:  your name\r\n")
  uart.write(" secret:  wanna know a secret...\r\n")
  uart.write(" connect: Instructions to customize me!\r\n")
  uart.write(" flag: Change the flag to a preset config. Try: flag puertoRicoFlag\r\n")
  uart.write(" startupColor: Change the startup animation color to a preset config. Try: startupColor red\r\n")

class CerealInterface:
  def __init__(self, leds):
    print("Cereal Init")
    self.uart = UART(0, baudrate=constants.BAUD_RATE, tx=machine.Pin(constants.CEREAL_TX_PIN), rx=machine.Pin(constants.CEREAL_RX_PIN))
    self.leds = leds

  #Run your serial connection with local echo
  def uartShell(self):
    print(self.uart) #for debugging/uart info
    
    prompt="\r\n> "
    self.uart.write(logo)
    self.uart.write(prompt)

    command = [] # start with blank string
    #Run Shell
    while True:
        # try:
          if self.uart.any():
              data = self.uart.read() #read data from self.uart
              if data == b'\n' or data == b'\r': #enter recieved 
                  commandString = ''.join(command)
                  command = []
                  if commandString == "help":
                      uartHelp(self.uart)
                      self.uart.write(prompt)
                  elif commandString == "version":
                      uartVersion(self.uart)
                      self.uart.write(prompt)
                  elif commandString == "whoami":
                      uartWhoami(self.uart)
                      self.uart.write(prompt)
                  elif commandString == "secret":
                      uartSecret(self.uart)  
                      self.uart.write(prompt)                                   
                  elif commandString == "connect":
                      uartInstructions(self.uart)    
                      self.uart.write(prompt)  
                  elif commandString.startswith("flag"):
                      uartParseFlag(self.uart, commandString, self.leds)    
                      self.uart.write(prompt)   
                  elif commandString.startswith("startupColor"):
                      uartParseStartupColor(self.uart, commandString, self.leds)    
                      self.uart.write(prompt)                                                                 
                  elif commandString == "":
                    self.uart.write(prompt)
                  else:
                      self.uart.write("\r\ncmd not recognized try again \r\n")
                      self.uart.write(prompt)
              else:
                  data = data.decode('utf-8') #convert data to string
                  self.uart.write(data)
                  command.append(data)# add value
        # except Exception as e:
          # print("An error occurred:", str(e))
        