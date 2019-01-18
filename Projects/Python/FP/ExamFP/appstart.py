from repository import *
from controller import *
from UI import *
r=PickleRepository('scramble.txt')
#r.add('scramble')
#r.add('dream without fear')
#r.add('The quick brown fox jumps over the lazy dog')
#r.add('Brevity is beautiful')
#r.add('Work hard dream big')
c=Controller(r)
ui=UI(c)
ui.start()