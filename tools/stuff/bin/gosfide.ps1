# Launch Google Chrome with specified URLs
Start-Process "chrome.exe" -ArgumentList "--new-window","https://wbo.ophir.dev/boards/sfide$((Get-Date).ToString('yyyy-MM-dd'))_1"
Start-Process "chrome.exe" -ArgumentList "https://etherpad.wikimedia.org/p/sfide_meetings$((Get-Date).ToString('yyyy'))"
Start-Process "chrome.exe" -ArgumentList "https://etherpad.wikimedia.org/p/sfide$((Get-Date).ToString('yyyy-MM-dd'))"
Start-Process "chrome.exe" -ArgumentList "https://univr.zoom.us/j/99139510848"

# Display URLs
Write-Host "URLs:"
Write-Host " - Zoom sfide Room: https://univr.zoom.us/j/99139510848"
Write-Host "Etherpad sfide index page: https://etherpad.wikimedia.org/p/sfide_meetings$((Get-Date).ToString('yyyy'))"
Write-Host " - Etherpad meeting report: https://etherpad.wikimedia.org/p/sfide$((Get-Date).ToString('yyyy-MM-dd'))"
Write-Host " - Collaborative WhiteBoard: https://wbo.ophir.dev/boards/sfide$((Get-Date).ToString('yyyy-MM-dd'))_1"
