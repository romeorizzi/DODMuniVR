# Launch Google Chrome with specified URLs
Start-Process "chrome.exe" -ArgumentList "--new-window","https://wbo.ophir.dev/boards/RO$((Get-Date).ToString('yyyy-MM-dd'))_1"
Start-Process "chrome.exe" -ArgumentList "https://etherpad.wikimedia.org/p/RO_meetings$((Get-Date).ToString('yyyy'))"
Start-Process "chrome.exe" -ArgumentList "https://etherpad.wikimedia.org/p/RO$((Get-Date).ToString('yyyy-MM-dd'))"
Start-Process "chrome.exe" -ArgumentList "https://univr.zoom.us/j/87547655553"

# Display URLs
Write-Host "URLs:"
Write-Host "Zoom RO Room: https://univr.zoom.us/j/87547655553"
Write-Host "Etherpad RO index page: https://etherpad.wikimedia.org/p/RO_meetings$((Get-Date).ToString('yyyy'))"
Write-Host "Etherpad meeting report: https://etherpad.wikimedia.org/p/RO$((Get-Date).ToString('yyyy-MM-dd'))"
Write-Host "Collaborative WhiteBoard: https://wbo.ophir.dev/boards/RO$((Get-Date).ToString('yyyy-MM-dd'))_1"
