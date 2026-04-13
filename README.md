# Fixing Songs in Spotify's Local Files

This repository contains a Python script to standardize audio sample rates, specifically designed to fix playback issues in Spotify's Local Files.

## Why?
I'm someone who listens to a lot of unreleased music and I use spotify to listen to the songs I download. Unfortunately there was an annoying issue where if I were to try to play my local files playlist, songs would not autoplay. They would simply stay stuck at **0:00** without playing. After a lot of researching, I found out the issue was the sample rate set for the audio file. Spotify specifically is quite strict on what they want songs to be at (I'm assuming that is) and if songs aren't set to **44.1kHz**, then it will simply not autoplay songs. So after learning this, I went through each song and checked to see if they were set at 44.1kHz, and lo and behold, a lot of them were set at 48.0kHz. 


# Requirements

## Python Version
This script is verified to work with python 3.12 only! Please do not use any other versions if you wish to use this script!

## Dependencies
This script uses `pydub` to handle audio manipulation and requires `ffmpeg` installed on your system to process mp3 files

1. Install python dependencies
```bash
pip install -r requirements.txt
```
2. External Dependency:
You must have `ffmpeg` installed and added to your system's PATH for `pydub` to export files.

You can check by running:
```bash
ffmpeg -version
```

## How it Works
The script iterates through a specified directory, identifies all .mp3 files, checks their sample rate, resamples them to 44.1kHz, and replaces the original file.

[CAUTION]
***Metadata Warning: Because this script exports a new version of the audio file to change the sample rate, some metadata (like custom song cover art) may be lost. It is recommended to back up your folder before running the script.***

#### Configuration
Update the `folder_path` variable in the script to point to your music directory:
```python
folder_path = r"place your song folder path here"
```

#### Execution
Run the script directly:
```bash
python main.py
```
