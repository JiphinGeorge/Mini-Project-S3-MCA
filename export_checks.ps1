$pptxPath = "D:\Antigravity Projects\Mini Project S3 MCA\Medical_Specialty_Classification_Presentation.pptx"
$ppt = New-Object -ComObject PowerPoint.Application
$pres = $ppt.Presentations.Open($pptxPath, [Microsoft.Office.Core.MsoTriState]::msoTrue, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoFalse)

$s1 = $pres.Slides.Item(1)
$s1.Export("D:\Antigravity Projects\Mini Project S3 MCA\s1_check.png", "PNG", 1920, 1080)

$s19 = $pres.Slides.Item(19)
$s19.Export("D:\Antigravity Projects\Mini Project S3 MCA\s19_check.png", "PNG", 1920, 1080)

$pres.Close()
$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
