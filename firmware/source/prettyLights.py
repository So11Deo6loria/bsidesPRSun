import time
import utime
import constants
from neopixel import NeoPixel
import machine
import math
import json
import random
from machine import Pin, Timer, SoftI2C


class LEDS:
    global timeDelay

    def __init__(self, colorScheme, startupColorName):
        ledPin = Pin(16, Pin.OUT)

        self.ledPower = Pin(22, Pin.OUT)
        self.ledPower.on()

        self.strand = NeoPixel(ledPin, 50)  # [0]*50
        self.offset = 0
        self.ledBaseColors = [[0] * 3] * 50
        self.secPerBeat = 2000
        self.newSecPerBeat = 2000
        self.randomTime = 2000
        self.colorScheme = colorScheme
        self.startupColor = constants.COLOR_MAPPING[startupColorName]

        self.updateColorScheme(self.colorScheme)

    def wakeup(self):
        self.ledPower.on()

    def updateConfigFile(self, key, value):
        with open("config.json", "r") as json_file:
            config_data = json.load(json_file)

        config_data[key] = value

        with open("config.json", "w") as json_file:
            json.dump(config_data, json_file)

    def updateColorScheme(self, newColorScheme):
        print(f"Changing color to: {newColorScheme}")

        # sets up a base color list/array thats easier to work with from the generic hex values that are easier to edit.  Done only on change for efficiency...
        if newColorScheme in constants.COLOR_SCHEMES:
            self.colorScheme = newColorScheme
            self.updateConfigFile("flag", newColorScheme)
            for index, color in enumerate(constants.COLOR_SCHEMES[newColorScheme]):
                self.ledBaseColors[index] = list(
                    bytearray.fromhex(constants.COLOR_SCHEMES[newColorScheme][index])
                )
        else:
            print("Could not Find Color Scheme")

    def updateStartupColor(self, newStartupColor):
        print(f"Changing color to: {newStartupColor}")

        # sets up a base color list/array thats easier to work with from the generic hex values that are easier to edit.  Done only on change for efficiency...
        if newStartupColor in constants.COLOR_MAPPING:
            self.startupColor = constants.COLOR_MAPPING[newStartupColor]
            self.updateConfigFile("startupColor", newStartupColor)
        else:
            print("Could not Find Startup Color")

    def startupAnimation(self):        
        blinkDelay = 0.01
        self.logoBlink(self.startupColor, blinkDelay, 0.75)
        time.sleep(blinkDelay)            
        blinkDelay = 0.025
        self.logoBlink(self.startupColor, blinkDelay, 0.5)
        time.sleep(blinkDelay)
        self.logoBlink(self.startupColor, blinkDelay, 0.5)
        time.sleep(blinkDelay)     
        blinkDelay = 0.05
        self.logoBlink(self.startupColor, blinkDelay, 0.5)
        time.sleep(blinkDelay)
        self.logoBlink(self.startupColor, blinkDelay, 0.5)
        time.sleep(blinkDelay)
        self.logoBlink(self.startupColor, blinkDelay, 0.5)
        time.sleep(blinkDelay)            
        blinkDelay = 0.1
        self.logoBlink(self.startupColor, blinkDelay, 0.75)
        time.sleep(blinkDelay)    
        self.logoBlink(self.startupColor, blinkDelay, 0.75)
        time.sleep(blinkDelay)            
        blinkDelay = 2
        self.logoBlink(self.startupColor, blinkDelay, 1)   

    def calculateBrightness(self, cycleTime, currentTime, startTime, pulseWidth):
        time = currentTime % cycleTime
        endTime = startTime + pulseWidth

        if (
            ((endTime) < cycleTime)
            and (time >= startTime)
            and (time <= (endTime) % cycleTime)
        ):
            return 0.5 - 0.5 * math.cos((time - startTime) / pulseWidth * 2 * math.pi)
        if (endTime > cycleTime) and (
            (time >= startTime) or (time <= endTime % cycleTime)
        ):
            if time >= startTime:
                return 0.5 - 0.5 * math.cos(
                    (time - startTime) / pulseWidth * 2 * math.pi
                )
            else:
                return 0.5 - 0.5 * math.cos(
                    (time + cycleTime - startTime) / pulseWidth * 2 * math.pi
                )
        else:
            return 0

    def waveDaFlag(self):
        maxBrightness = 0.25
        lowBrightness = 0.15
        currentTime = utime.ticks_ms()
        self.randomTime
        if currentTime > self.randomTime:
            self.randomTime = currentTime + random.randint(1000, 3000)
            self.newSecPerBeat = random.randint(900, 2000)
            self.offset = (
                (currentTime + self.offset) % self.secPerBeat
            ) * self.newSecPerBeat / self.secPerBeat - currentTime
            self.secPerBeat = self.newSecPerBeat

        for index, led in enumerate(constants.WAVE_CONFIG):
            brightness = self.calculateBrightness(
                self.secPerBeat,
                currentTime + self.offset,
                led["startTime"] * self.secPerBeat,
                led["pulseWidth"] * self.secPerBeat,
            )
            modifier = (brightness) * maxBrightness + lowBrightness
            self.strand[index] = tuple(
                round(i * modifier) for i in self.ledBaseColors[index]
            )

        self.strand.write()

    def logoBlink(self, color, blinkDelay, intensity):
        scaledColor = [round(element * intensity) for element in color]
        for i in range(50):
            if i >= 39 and i < 50:
                self.strand[i] = tuple(scaledColor)
            else:
                self.strand[i] = tuple([0, 0, 0])
        self.strand.write()

        time.sleep(blinkDelay)

        for i in range(50):
            self.strand[i] = tuple([0, 0, 0])
        self.strand.write()

    def illuminate(self):
        for i in range(50):
            self.strand[i] = tuple([255, 255, 255])
        self.strand.write()

    def shutdown(self):
        for i in range(50):
            self.strand[i] = tuple([0, 0, 0])
        self.strand.write()
        return True
