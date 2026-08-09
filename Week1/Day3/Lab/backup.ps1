 Write-Host "Starting backup..."
 Copy-Item ".\Documents\*" ".\Backup\" -Recurse
 Write-Host "Backup completed."