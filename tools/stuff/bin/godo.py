#!/usr/bin/python
import os
from sys import stderr, exit, argv
import datetime

os.system(f'date +"%Y-%m-%d_%B  %A%ttime: %H:%M" >> ./go.log')
os.system(f'echo " DODM class godo.py" >> ./go.log')
os.system(f'echo >> ./go.log')
os.system(f'google-chrome --new-window https://wbo.ophir.dev/boards/DODM{str(datetime.date.today())}_1')
os.system(f'google-chrome https://etherpad.wikimedia.org/p/DODM_meetings{str(datetime.date.today())[:4]}')
os.system(f'google-chrome https://etherpad.wikimedia.org/p/DODM{str(datetime.date.today())}')
os.system(f'google-chrome https://univr.zoom.us/j/89889727405')

os.system('echo URLs:')
os.system('echo " - Zoom DODM room: https://univr.zoom.us/j/89889727405"')
os.system(f'echo " - Etherpad DODM index page: https://etherpad.wikimedia.org/p/DODM_meetings{str(datetime.date.today())[:4]}"')
os.system(f'echo " - Etherpad meeting report: https://etherpad.wikimedia.org/p/DODM{str(datetime.date.today())}"')
Write-Host " - Collaborative WhiteBoard: https://wbo.ophir.dev/boards/DODM$((Get-Date).ToString('yyyy-MM-dd'))_1"
