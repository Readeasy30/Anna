# Automated Tenant Provisioning Manager
# Context Boundary: wholelychit

param (
    [Parameter(Mandatory = $true)]
    [string]$Domain,
    
    [Parameter(Mandatory = $true)]
    [ValidateSet("literacy", "math", "business_leasing")]
    [string]$TemplateType,
    
    [Parameter(Mandatory = $true)]
    [string]$TenantId
)

Write-Host "=========================================================" -ForegroundColor Cyan
Write-Host "         LAUNCHING AUTOMATED TENANT PROVISIONER          " -ForegroundColor Cyan
Write-Host "=========================================================" -ForegroundColor Cyan
Write-Host "Target Domain     : [\]" -ForegroundColor Yellow
Write-Host "Template Architecture: [\]" -ForegroundColor Yellow
Write-Host "Assigned Tenant ID  : [\]" -ForegroundColor Yellow

# Define output path for the configuration profile
$TargetFolder = "C:\Users\Wholelychit\Anna-agent\gman-avatar"
if (-not (Test-Path $TargetFolder)) { New-Item -ItemType Directory -Path $TargetFolder -Force | Out-Null }
$ProfilePath = Join-Path $TargetFolder "tenant_\.json"

# Resolve prompt and model parameters dynamically based on selected template type
switch ($TemplateType) {
    "literacy" {
        $Persona = "G-Man Literacy Coach"
        $Model   = "gpt-4o"
        $Prompt  = "You are the G-Man literacy avatar. Focus strictly on comprehension and decoding workflows."
    }
    "math" {
        $Persona = "G-Man Math Mentor"
        $Model   = "o1-mini"
        $Prompt  = "You are the G-Man step-by-step mathematical reasoning agent. Drive systematic calculations."
    }
    "business_leasing" {
        $Persona = "G-Man Leasing Consultant"
        $Model   = "gpt-4o"
        $Prompt  = "You are the specialized business representative for this leased web property. Manage client lead ingestion."
    }
}

# Construct the payload mapping
$ProfileJson = @{
    "tenantId"            = $TenantId
    "domain"              = $Domain
    "contextBoundary"     = "wholelychit"
    "status"              = "active_running"
    "billingTier"         = "leased_premium"
    "avatarConfiguration" = @{
        "personaName"  = $Persona
        "modelContext" = $Model
        "systemPrompt" = $Prompt
        "temperature"  = 0.3
    }
    "cloudflareBindings"  = @{
        "workerUrl"   = "https://omniroute.\"
        "kvNamespace" = "\_AVATAR_KV"
    }
} | ConvertTo-Json -Depth 5

# Output configuration payload file
Set-Content -Path $ProfilePath -Value $ProfileJson
Write-Host "Tenant profile generated successfully at: $ProfilePath" -ForegroundColor Green

# Trigger automatic git staging update hook
if (git rev-parse --is-inside-work-tree -ErrorAction SilentlyContinue) {
    git add $ProfilePath
    Write-Host "New profile staged into source control workspace index records." -ForegroundColor Gray
}
