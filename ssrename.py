import os
import time
from datetime import datetime

# Change this path to your screenshots folder
SCREENSHOT_FOLDER = r"C:\Users\Conte\OneDrive\Pictures\Screenshots"

# Screenshots = ss
def get_next_screenshot_number():
    """Finds the next available number for SS[number] naming"""
    highest_number = 0

    for file in os.listdir(SCREENSHOT_FOLDER):
        if file.lower().startswith("ss") and file.lower().endswith((".png", ".jpg")):
            try:
                number_part = file.split("_")[0][2:]  # Extracts the number from SS[number]_
                number = int(number_part)
                highest_number = max(highest_number, number)
            except (ValueError, IndexError):
                continue  # Skip files that don't match the expected pattern

    return highest_number + 1  # Next available number

def rename_screenshots():
    """Scans the screenshot folder and renames files with SS[number] and timestamps"""
    if not os.path.exists(SCREENSHOT_FOLDER):
        print(f"Folder not found: {SCREENSHOT_FOLDER}")
        return

    next_number = get_next_screenshot_number()  # Get the next available SS[number]

    for file in os.listdir(SCREENSHOT_FOLDER):
        if file.lower().startswith("screenshot") and file.lower().endswith((".png", ".jpg")):
            old_path = os.path.join(SCREENSHOT_FOLDER, file)

            # Extract creation time of the file
            timestamp = os.path.getctime(old_path)
            formatted_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

            # Keep the original file extension
            file_extension = os.path.splitext(file)[1]

            # Create new filename: SS[number]_[date].png
            new_filename = f"SS{next_number}_{formatted_time}{file_extension}"
            new_path = os.path.join(SCREENSHOT_FOLDER, new_filename)

            # Rename only if the new filename doesn't already exist
            if not os.path.exists(new_path):
                os.rename(old_path, new_path)
                print(f"Renamed: {file} ➝ {new_filename}")
                next_number += 1  # Increment the number for the next file
            else:
                print(f"Skipped (already renamed): {file}")
while True:
    print("Checking for new screenshots")
    rename_screenshots()
    time.sleep(10)  # Wait 10 seconds before checking again