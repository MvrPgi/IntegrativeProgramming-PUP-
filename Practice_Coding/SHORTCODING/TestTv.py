# Test the TV class
from TV import TV
tv1 = TV()
tv2 = TV()

tv1.turnOn()
tv1.setChannel(30)
tv1.setVolume(3)

tv2.turnOn()
tv2.setChannel(3)
tv2.setVolume(2)

print("tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())
print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())
