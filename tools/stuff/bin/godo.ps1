# Launch Google Chrome with specified URLs
Start-Process "chrome.exe" -ArgumentList "--new-window","https://wbo.ophir.dev/boards/DODM$((Get-Date).ToString('yyyy-MM-dd'))_1"
Start-Process "chrome.exe" -ArgumentList "https://etherpad.wikimedia.org/p/DODM_meetings$((Get-Date).ToString('yyyy'))"
Start-Process "chrome.exe" -ArgumentList "https://etherpad.wikimedia.org/p/DODM$((Get-Date).ToString('yyyy-MM-dd'))"
Start-Process "chrome.exe" -ArgumentList "https://univr.zoom.us/j/89889727405"

# Display URLs
Write-Host "URLs:"
Write-Host "Zoom Room DODM URL: https://univr.zoom.us/j/89889727405"
Write-Host "Etherpad DODM index page: https://etherpad.wikimedia.org/p/DODM_meetings$((Get-Date).ToString('yyyy'))"
Write-Host "Etherpad meeting report: https://etherpad.wikimedia.org/p/DODM$((Get-Date).ToString('yyyy-MM-dd'))"
Write-Host "Collaborative WhiteBoard: https://wbo.ophir.dev/boards/DODM$((Get-Date).ToString('yyyy-MM-dd'))_1"
