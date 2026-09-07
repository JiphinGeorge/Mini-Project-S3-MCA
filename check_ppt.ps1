$app = [Runtime.InteropServices.Marshal]::GetActiveObject("PowerPoint.Application")
foreach ($p in $app.Presentations) {
    Write-Output "OPEN_PPT: $($p.FullName)"
}
