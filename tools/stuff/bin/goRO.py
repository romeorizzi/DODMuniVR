#!/usr/bin/python
import os
from sys import stderr, exit, argv
import datetime

os.system(f'date +"%Y-%m-%d_%B  %A%ttime: %H:%M" >> ./go.log')
os.system(f'echo " RO class goRO.py" >> ./go.log')
os.system(f'echo >> ./go.log')
os.system(f'google-chrome https://wbo.ophir.dev/boards/RO{str(datetime.date.today())}_1')
os.system(f'google-chrome --new-window https://etherpad.wikimedia.org/p/RO_meetings{str(datetime.date.today())[:4]}')
os.system(f'google-chrome https://etherpad.wikimedia.org/p/RO{str(datetime.date.today())}')
os.system(f'google-chrome https://univr.zoom.us/j/87547655553')

os.system('echo URLs:')
os.system('echo " - Zoom RO room: https://univr.zoom.us/j/87547655553"')
os.system(f'echo " - Etherpad RO index page: https://etherpad.wikimedia.org/p/RO_meetings{str(datetime.date.today())[:4]}"')
os.system(f'echo " - Etherpad meeting report: https://etherpad.wikimedia.org/p/RO{str(datetime.date.today())}"')
Write-Host " - Collaborative WhiteBoard: https://wbo.ophir.dev/boards/RO$((Get-Date).ToString('yyyy-MM-dd'))_1"
