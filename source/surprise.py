from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlocks(pos.x+1, pos.y, pos.z+1,
             pos.x+6, pos.y+5, pos.z+6, 46, 1)
