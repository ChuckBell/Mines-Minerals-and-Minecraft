# iceman2.py Ð Set every tile Steve hits
# to ice.
from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()
while True:
    pos = mc.player.getTilePos() 
    mc.setBlock(pos.x, pos.y, pos.z, block.SNOW)
    for hit in mc.events.pollBlockHits():
        mc.setBlock(hit.pos.x, hit.pos.y,
                    hit.pos.z, block.ICE)
