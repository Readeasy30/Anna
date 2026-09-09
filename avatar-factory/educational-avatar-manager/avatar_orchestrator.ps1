# Educational Site Avatar Manager Core Engine — Extended Edition
# Context Boundary: wholelychit

param (
    [Parameter(Mandatory = $true)]
    [ValidateSet("readeasy30.com", "matheasy30.com")]
    [string]$TargetSite,

    [Parameter(Mandatory = $false)]
    [ValidateSet("initialize", "sync_state", "terminate")]
    [string]$Action = "initialize",

    [Parameter(Mandatory = $false)]
    [string]$CustomPromptPayload = ""
)

Write-Host "=========================================================" -ForegroundColor Cyan
Write-Host "        G-MAN MULTI-TENANT AVATAR MANAGER SYSTEM         " -ForegroundColor Cyan
Write-Host "=========================================================" -ForegroundColor Cyan
Write-Host "Selected Target Domain    : [\]" -ForegroundColor Yellow
Write-Host "Pipeline Command Activity : [\]" -ForegroundColor Yellow

# Helper loop to trigger the Python notification script
function Invoke-PythonNotification {
    param ($Level, $Module, $Message)
    $PyScript = "C:\Users\Wholelychit\Anna-agent\android-ops\notifier.py"
    if (Test-Path $PyScript) {
        # Execute headless python command safely passing parameter maps
        python $PyScript $Level $Module "$Message" 2>$null
    }
}

switch ($TargetSite) {
    "readeasy30.com" {
        $TenantProfile = @{
            "PersonaName"     = "G-Man Literacy Coach"
            "CloudflareWorker" = "https://workers.dev"
            "TargetModel"     = "gpt-4o"
        }
    }
    "matheasy30.com" {
        $TenantProfile = @{
            "PersonaName"     = "G-Man Math Mentor"
            "CloudflareWorker" = "https://workers.dev"
            "TargetModel"     = "o1-mini"
        }
    }
}

switch ($Action) {
    "initialize" {
        Write-Host "Activating tenant interface for [\]..." -ForegroundColor Green
        Invoke-PythonNotification -Level "INFO" -Module "Avatar Orchestrator" -Message "Initializing dynamic interface loop context for $TargetSite"
        
        $StatePayload = @{
            "site" = $TargetSite
            "persona" = $TenantProfile.PersonaName
            "model" = $TenantProfile.TargetModel
            "boundary" = "wholelychit"
            "timestamp" = (Get-Date).ToString("o")
        } | ConvertTo-Json -Compress
        
        $InstanceFile = Join-Path (Split-Path $PSCommandPath) "active_session_\.json"
        Set-Content -Path $InstanceFile -Value $StatePayload
        Write-Host "Active state instance checkpointed cleanly." -ForegroundColor Green
    }
    "sync_state" {
        Write-Host "Synchronizing worker context bindings across Cloudflare Edge tunnels..." -ForegroundColor Yellow
        Invoke-PythonNotification -Level "DEBUG" -Module "Avatar Orchestrator" -Message "Running synchronization checks for $TargetSite"
    }
    "terminate" {
        Write-Host "Spinning down engine listeners safely..." -ForegroundColor Red
        Invoke-PythonNotification -Level "WARNING" -Module "Avatar Orchestrator" -Message "Terminating active tracking bounds for $TargetSite"
        $InstanceFile = Join-Path (Split-Path $PSCommandPath) "active_session_\.json"
        if (Test-Path $InstanceFile) { Remove-Item $InstanceFile -Force }
    }
}
