# iceman1.py Ð Set every tile Steve walks on 
# to ice.
from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()
while True:
    pos = mc.player.getTilePos() 
    mc.setBlock(pos.x, pos.y, pos.z, block.SNOW)
