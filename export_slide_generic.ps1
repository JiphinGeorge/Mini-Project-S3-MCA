param (
    [int]$SlideNum = 2,
    [string]$OutName = "slide_preview.png"
)

$pptxPath = "D:\Antigravity Projects\Mini Project S3 MCA\Medical_Specialty_Classification_Presentation.pptx"
$outPng = "D:\Antigravity Projects\Mini Project S3 MCA\$OutName"

$ppt = New-Object -ComObject PowerPoint.Application
$pres = $ppt.Presentations.Open($pptxPath, [Microsoft.Office.Core.MsoTriState]::msoTrue, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoFalse)
$slide = $pres.Slides.Item($SlideNum)
$slide.Export($outPng, "PNG", 1920, 1080)
$pres.Close()
$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
[System.GC]::Collect()
[System.GC]::WaitForPendingFinalizers()
Write-Host "Exported Slide $SlideNum to $outPng successfully!"
