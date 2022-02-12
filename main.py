import player
import time
import sys

player = player.Player("test.wav")
player.start
time.sleep(2)
player.stop
player.jumpTo(player.waveDash.getnframes()//2)
player.start
time.sleep(2)
player.murk
