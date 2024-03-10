import time
import utime
import constants
from neopixel import NeoPixel
import machine
import math
from machine import Pin, Timer, SoftI2C


class LEDS:
  global timeDelay
  colorScheme = 'puertoRicoFlag'

  def __init__(self):
    ledPin = Pin(16, Pin.OUT)
    
    self.ledPower = Pin( 22, Pin.OUT)
    self.ledPower.on()

    self.strand = NeoPixel(ledPin, 50) # [0]*50
    self.offset = 0
    self.ledBaseColors = [[0]*3]*50
    self.secPerBeat = 1000

    self.updateColorScheme(self.colorScheme)

  def wakeup(self):
    self.ledPower.on()

  def updateColorScheme( self, newColorScheme ):
    print( f'Changing color to: {newColorScheme}')

    #sets up a base color list/array thats easier to work with from the generic hex values that are easier to edit.  Done only on change for efficiency...
    if newColorScheme in constants.COLOR_SCHEMES:
      self.colorScheme = newColorScheme
      for index, color in enumerate(constants.COLOR_SCHEMES[newColorScheme]):
        self.ledBaseColors[index]=list(bytearray.fromhex(constants.COLOR_SCHEMES[newColorScheme][index]))
    else:
      print("Could not Find Color")

  def calculateBrightness( self, cycleTime, currentTime, startTime, pulseWidth):
    time = currentTime%cycleTime
    endTime = startTime+pulseWidth

    if(((endTime) < cycleTime) and (time >= startTime) and ((time<=(endTime)%cycleTime))):
      return 0.5 - 0.5 * math.cos((time - startTime) / pulseWidth * 2 * math.pi )
    if((endTime>cycleTime) and ((time >= startTime) or ( time <= endTime%cycleTime))):
      if(time >= startTime):
        return 0.5 - 0.5 * math.cos((time - startTime) / pulseWidth * 2 * math.pi )
      else:
        return 0.5 - 0.5 * math.cos((time+cycleTime - startTime) / pulseWidth * 2 * math.pi )
    else:
      # print(   f'  current:{currentTime}/{time}, start:{startTime}, end:{endTime}, pulseW :{pulseWidth}')
      return 0


  def startupWave(self):

    startTime = utime.ticks_ms()
    currentTime = startTime
    animationLength = 12000
    self.offset = animationLength-currentTime%animationLength # special sauce to still use the general tick_ms time, but ensure we start at 0.

    while( currentTime < (startTime+animationLength )):

      currentTime = utime.ticks_ms()

      for index, led in enumerate(constants.WAVE_SMOOTH):
        brightness = self.calculateBrightness( animationLength, currentTime+self.offset, led['startTime']*self.secPerBeat, led['pulseWidth']*self.secPerBeat )
        # print(f'time: {((currentTime+self.offset)%self.secPerBeat)}led: {index+1}, brightness: {brightness}')
        if index < 7:
          pass
          #self.strand[index]=tuple(round(i * 0.5* brightness) for i in self.ledBaseColors[index])
        else:
          pass
          #self.strand[index-7]=tuple(round(i *0.5* brightness) for i in self.ledBaseColors[index])

      #self.strand.write()
      #self.strand.write()

      time.sleep(.025)

  # def tickHeartbeat(self):
  #   currentTime = utime.ticks_ms()
  #   self.secPerBeat = 60000/self.bpm
  #   if(self.newBPM != 0 ):
  #     #need to get smooth transitions,  as a shortcut going to add an offset to place the currentTime next in the same place relative to the cycle.
  #     self.offset = ((currentTime+self.offset)%self.secPerBeat)*self.bpm/self.newBPM - currentTime
  #     self.bpm = self.newBPM
  #     self.secPerBeat = 60000/self.bpm
  #     self.newBPM = 0


  #   for index, led in enumerate(constants.LED_CONFIG):
  #     brightness = self.calculateBrightness( self.secPerBeat, currentTime+self.offset, led['startTime']*self.secPerBeat, led['pulseWidth']*self.secPerBeat )
  #     # print(f'led: {index+1}, brightness: {brightness}')
  #     if index < 7:
  #       pass
  #       #self.strand[index]=tuple(round(i * 0.5* brightness) for i in self.ledBaseColors[index])
  #     else:
  #       pass
  #       #self.strand[index-7]=tuple(round(i *0.5* brightness) for i in self.ledBaseColors[index])

  #   #self.strand2.write()
  #   #self.strand.write()

  def waveDaFlag(self): 
    currentTime = utime.ticks_ms()
    self.secPerBeat = 12000
    # if(self.newBPM != 0 ):
    #   #need to get smooth transitions,  as a shortcut going to add an offset to place the currentTime next in the same place relative to the cycle.
    #   self.offset = ((currentTime+self.offset)%self.secPerBeat)*self.bpm/self.newBPM - currentTime
    #   self.bpm = self.newBPM
    #   self.secPerBeat = 60000/self.bpm
    #   self.newBPM = 0

    for index, led in enumerate(constants.LED_CONFIG):
      brightness = self.calculateBrightness( self.secPerBeat, currentTime+self.offset, led['startTime'], led['pulseWidth'] )
      print(f'led: {index+1}, brightness: {brightness}')
      self.strand=tuple(round(i * 0.5* brightness) for i in self.ledBaseColors[index])
      self.strand.write()


  def heartbeatRunLoop(self):
    timeDelay = .025
    while( True ):
      self.tickHeartbeat()
      time.sleep(timeDelay)

  def logoBlink(self, color, blinkDelay, intensity):
      scaledColor = [round(element * intensity) for element in color]
      for i in range(50):
        if( i >= 39 and i < 50 ):
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

  def darkness(self):
      for i in range(50):
        self.strand[i] = tuple([0, 0, 0])
      self.strand.write()
      return True       

  def setFlag(self, flagName, intensity):
    print(f"Setting Flag: {flagName}")
    flagConfig = constants.FLAG_MAPPING[flagName]
    scaledFlagConfig = [[round(element * intensity) for element in led] for led in flagConfig] # Scale the original flag config based on the intensity
    for i in range(50):
      self.strand[i] = tuple(scaledFlagConfig[i])
    self.strand.write()

  def ledTest( self ):
    for i in range(50):
      for led in range(50):
        if( i == led ):
          self.strand[led] = tuple([255,0,0])
        else:
          self.strand[led] = tuple([0,0,0])
      self.strand.write()
      time.sleep(0.25)

  def blinkWords(self, wordArray, color, letterDelay, intensity):
    wordDelay = letterDelay * 2
    scaledColor = [round(element * intensity) for element in color]
    for word in wordArray:
      for letter in word: 
        letter = letter.upper()
        for led in range(50):
          if( led+1 in constants.LETTER_CONFIG[letter] ):
            self.strand[led] = tuple(scaledColor)
          else:
            self.strand[led] = constants.LED_OFF
        self.strand.write()
        time.sleep(letterDelay)
      time.sleep(wordDelay)

  def waveAnimation(self, flagName, intensity):
    dimness = intensity / 4
    flagConfig = constants.FLAG_MAPPING[flagName]
    intenseFlagConfig = [[round(element * intensity) for element in led] for led in flagConfig] # Scale the original flag config based on the intensity
    dimFlagConfig     = [[round(element * dimness  ) for element in led] for led in flagConfig] # Scale the original flag config based on the intensity
    
    self.setFlag( flagName, intensity )

    lines = constants.LINE_CONFIG
    numOfLines = 2
    # The dim array length might not be accurate every time but it shouldn't cause issues
    dimArrayLength = round( len(lines) / numOfLines ) * ( numOfLines - 1 ) + len(lines) + 1
    dimArray = [[] for _ in range(dimArrayLength)] 
    for numOfLinesIndex in range(numOfLines):
      index = round(( len(lines) / numOfLines ) * numOfLinesIndex)
      for line in lines:
        dimArray[index] = dimArray[index] + line
        index = index + 1

    for line in dimArray:
      for led in range(constants.LED_COUNT):
        if( (led+1) in line ):
          self.strand[led] = tuple(dimFlagConfig[led])
        else:
          self.strand[led] = tuple(intenseFlagConfig[led])
      self.strand.write()
      time.sleep(constants.WAVE_DELAY)
