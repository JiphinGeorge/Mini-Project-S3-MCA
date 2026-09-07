import os, glob, subprocess, time, shutil

folder = r"D:\Antigravity Projects\Mini Project S3 MCA"
final_version = os.path.join(folder, "Medical_Specialty_Classification_Presentation_v8.pptx")
single_target = os.path.join(folder, "Medical_Specialty_Classification_Presentation.pptx")

# First, close PowerPoint if running to release file locks
subprocess.run(["powershell", "-Command", "Stop-Process -Name POWERPNT -Force -ErrorAction SilentlyContinue"], capture_output=True)
time.sleep(1)

# Ensure our final version exists
if not os.path.exists(final_version):
    # fallback to v7 or downloads
    final_version = r"C:\Users\jiphi\Downloads\Medical_Specialty_Classification_Presentation.pptx"

# Copy final_version to single_target
shutil.copy2(final_version, single_target)
print(f"Final presentation set at: {single_target}")

# Remove all other .pptx files in folder
all_pptx = glob.glob(os.path.join(folder, "*.pptx"))
removed_count = 0
for f in all_pptx:
    if os.path.abspath(f) != os.path.abspath(single_target):
        try:
            os.remove(f)
            print(f"Removed: {os.path.basename(f)}")
            removed_count += 1
        except Exception as e:
            print(f"Failed to remove {os.path.basename(f)}: {e}")

# Also remove any ~$ lock files
for f in glob.glob(os.path.join(folder, "~$*")):
    try:
        os.remove(f)
        print(f"Removed lock file: {os.path.basename(f)}")
    except Exception as e:
        pass

print(f"\nCleanup complete. Removed {removed_count} other presentation files.")
remaining = glob.glob(os.path.join(folder, "*.pptx"))
print(f"Remaining .pptx files in '{folder}':")
for r in remaining:
    print(f"  - {os.path.basename(r)} ({os.path.getsize(r)} bytes)")
