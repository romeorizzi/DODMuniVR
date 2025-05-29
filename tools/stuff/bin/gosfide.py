#!/usr/bin/python
import os
from sys import stderr, exit, argv
import datetime

os.system(f'date +"%Y-%m-%d_%B  %A%ttime: %H:%M" >> ./go.log')
os.system(f'echo " sfide class gosfide.py" >> ./go.log')
os.system(f'echo >> ./go.log')
os.system(f'google-chrome https://wbo.ophir.dev/boards/sfide{str(datetime.date.today())}_1')
os.system(f'google-chrome --new-window https://etherpad.wikimedia.org/p/sfide_meetings{str(datetime.date.today())[:4]}')
os.system(f'google-chrome https://etherpad.wikimedia.org/p/sfide{str(datetime.date.today())}')
os.system(f'google-chrome https://univr.zoom.us/j/99139510848')

os.system('echo URLs:')
os.system('echo " - Zoom sfide room: https://univr.zoom.us/j/99139510848"')
os.system(f'echo " - Etherpad sfide index page: https://etherpad.wikimedia.org/p/sfide_meetings{str(datetime.date.today())[:4]}"')
os.system(f'echo " - Etherpad meeting report: https://etherpad.wikimedia.org/p/sfide{str(datetime.date.today())}"')
os.system(f'echo " - Collaborative WhiteBoard: https://etherpad.wikimedia.org/p/sfide{str(datetime.date.today())}_1"')
