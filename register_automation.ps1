# Unattended Environment Startup Scheduler
# Context Boundary: wholelychit

Write-Host "Configuring persistent task schedulers for headless recovery loops..." -ForegroundColor Cyan

$TaskName = "AnnaWorkspaceAutomationTunnel"
$ActionScript = "C:\Users\Wholelychit\Anna-agent\avatar-factory\educational-avatar-manager\avatar_orchestrator.ps1"

# Create a task action to execute your main orchestrator script headlessly inside PowerShell
$Action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-NoProfile -WindowStyle Hidden -File $ActionScript -TargetSite readeasy30.com -Action initialize"
$Trigger = New-ScheduledTaskTrigger -AtStartup

# Register task under elevated system privileges to survive user logouts
try {
    Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -User "SYSTEM" -Force | Out-Null
    Write-Host "Startup Automation Task registered successfully: [$TaskName]" -ForegroundColor Green
} catch {
    Write-Host "Privilege Warning: Elevated admin credentials are required to bind system-level boot tasks." -ForegroundColor Yellow
}
