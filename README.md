# Screenshot Renamer

Screenshot Renamer is a Python automation script that continuously monitors a folder for new screenshots and renames them to an incrementing number and a timestamp.


## Quickstart

1.
```bash
git clone https://github.com/drewnw/Screenshot-Renamer.git
cd Screenshot-Renamer
```
2. On line 5 in ```ssrenamer.py```, replace the current file path with the absolute file path to your screenshot folder
3. Run ```ssrenamer.py```

## Features

- Continuously monitors a folder for new screenshots
- Automatically renames each screenshot using a clean, consistent format
- Runs silently in the background using a loop and sleep interval
- Ensures no duplicates by incrementing the screenshot number
- Easy to configure for any operating system or screenshot naming convention


## Customize

1. You can adjust the sleep interval to check for new files more or less frequently
2. Modify the naming convention to fit your personal preferences
3. Add logging or notification features if you want confirmation each time a screenshot is renamed
