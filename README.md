# YouTube Downloader

## Overview

This project is a simple and efficient YouTube downloader built with Python and Flask. It allows users to download YouTube videos in either audio or video format directly from a web interface. 

## Features

- **Download Audio**: Extracts the audio from the YouTube video and provides it as a downloadable MP3 file.
- **Download Video**: Downloads the YouTube video in its highest available resolution.
- **User-Friendly Interface**: Simple and intuitive web interface for easy downloads.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/youtube-downloader.git
    ```
2. Navigate to the project directory:
    ```
    cd youtube-downloader
    ```
3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Run the application:
    ```
    python web.py
    ```
5. Open your web browser and navigate to `http://localhost:5000`.

## Usage

1. Enter the URL of the YouTube video you want to download.
2. Choose whether you want to download the audio or the video.
3. Click the corresponding button to start the download.

## Dependencies

- Flask: A lightweight WSGI web application framework.
- PyTube: A lightweight, Pythonic, dependency-free, library (and command-line utility) for downloading YouTube Videos.
- MoviePy: A Python module for video editing, which can be used for basic operations on videos and GIFs.

