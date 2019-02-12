# iceman.py Ð Set the tile Steve is on to ice.
from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()
pos = mc.player.getTilePos() 
mc.setBlock(pos.x, pos.y, pos.z, block.SNOW)
