class TV:
    # constructor attributes of an TV object
    def __init__(self):
        self.channel = 1        # sets initial channel to 1
        self.volumeLevel = 1    # sets initial volume to 1
        self.on = False         # sets initial on to False if TV is initially turned off
    

    # a method that returns True when TV is on
    def turnOn(self):
        self.on = True

    # a method that returns False when TV is off
    def turnOff(self):
        self.on = False
    
    # a method that returns the current channel
    def getChannel(self):
        return self.channel
    
    # a method that sets new channel
    def setChannel(self, channel):
        if self.on and (1 <= channel <= 120): # sets channel iff TV is turned on
            self.channel = channel

    # a method that returns the current volume
    def getVolume(self):
        return self.volumeLevel
    
    # a method that sets new volume level
    def setVolume(self, volume):
        if self.on and (1 <= volume <= 7):
            self.volumeLevel = volume

    # a method that increments channel number by 1
    def channelUp(self):
        if self.on and self.channel < 120:          # only increments iff TV is on and channel number is less than 120 (max value)
            self.channel += 1

    # a method the decrements channel number by 1
    def channelDown(self):
        if self.on and self.channel > 1:             # only decrements iff TV is on and channel number is greater than 1 (min value)
            self.channel -= 1

    # a method that increments volume level by 1
    def volumeUp(self):
        if self.on and self.volumeLevel < 7:         # only increments iff TV is on and volume level is less than 7 (max value)
            self.volumeLevel += 1

    # a method the decrements volume level by 1
    def volumeDown(self):
        if self.on and self.volumeLevel > 1:         # only decrements iff TV is on and volume level is greater than 1 (min value)          
          self.volumeLevel -= 1
