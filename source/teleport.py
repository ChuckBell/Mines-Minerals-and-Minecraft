import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
time.sleep(1)
pos = mc.player.getPos()
mc.postToChat("You are located x=" +str(pos.x) + ", y=" +str(pos.y) +", z=" +str(pos.z))
time.sleep(2)
mc.postToChat("Get ready to fall from the sky!")
time.sleep(5)
mc.player.setPos(pos.x, pos.y + 60, pos.z)
