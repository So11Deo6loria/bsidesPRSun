#import lowpower
import utime
import time # Remove later
import machine
import _thread
import constants
import prettyLights
import cerealInterface
import ujson
from machine import Pin, Timer

class Main:
    def __init__(self):
        print("Start Up") # only print after receiving signal on Pin number DORMANT_PIN
        self.runLoop()

    def lowPowerPause(self):
        self.sensor.shutdown()
        self.leds.shutdown()
        while(self.button.value() != 1):
            utime.sleep_ms(10)
        lowpower.dormant_until_pin(constants.BUTTON)
        self.sensor.wakeUp()
        self.leds.wakeup()

    def startupAnimation(self):
        self.startupColor = constants.COLOR_MAPPING[self.startupColorName]
        blinkDelay = 0.01
        self.leds.logoBlink(self.startupColor, blinkDelay, 0.75)
        time.sleep(blinkDelay)            
        blinkDelay = 0.025
        self.leds.logoBlink(self.startupColor, blinkDelay, 0.5)
        time.sleep(blinkDelay)
        self.leds.logoBlink(self.startupColor, blinkDelay, 0.5)
        time.sleep(blinkDelay)     
        blinkDelay = 0.05
        self.leds.logoBlink(self.startupColor, blinkDelay, 0.5)
        time.sleep(blinkDelay)
        self.leds.logoBlink(self.startupColor, blinkDelay, 0.5)
        time.sleep(blinkDelay)
        self.leds.logoBlink(self.startupColor, blinkDelay, 0.5)
        time.sleep(blinkDelay)            
        blinkDelay = 0.1
        self.leds.logoBlink(self.startupColor, blinkDelay, 0.75)
        time.sleep(blinkDelay)    
        self.leds.logoBlink(self.startupColor, blinkDelay, 0.75)
        time.sleep(blinkDelay)            
        blinkDelay = 2
        self.leds.logoBlink(self.startupColor, blinkDelay, 1)   

    def read_config(self):
        try:
            with open('config.json', 'r') as f:
                data = ujson.load(f)
                return data
        except:
            return False
        
    def runLoop(self):
        config = self.read_config()
        if(config):
            print("Loading following configuration:")
            print(config)
            self.startupColorName = config['startupColor']
            self.flagName = config['flag']
            self.sleepTimeout = config['sleepTimeout']
        else:
            print("Loading default configuration")
            self.startupColorName = 'white',
            self.flagName = 'puertorico'
            self.sleepTimeout = 300 # 300 seconds

        self.button = Pin(constants.BUTTON, Pin.IN, Pin.PULL_UP)

        serialInterface = cerealInterface.CerealInterface()
        _thread.start_new_thread(serialInterface.uartShell, ())

        #Initialize LED Manager and Turn on Power
        self.leds = prettyLights.LEDS()
        self.leds.wakeup()
        self.startupAnimation()

        #Capture the Bootup Time
        startTime = utime.ticks_ms()

        while(True):
            if((self.button.value() != 1) or (utime.ticks_diff(utime.ticks_ms(), startTime) > self.sleepTimeout*1000)):
                print("getting sleepy")
                #self.lowPowerPause()
                #startTime = utime.ticks_ms()
                #self.startupAnimation()

            self.leds.waveAnimation(self.flagName, constants.LED_MAX)
            time.sleep(0.1)

Main()