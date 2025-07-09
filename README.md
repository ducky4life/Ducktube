# Ducktube - YouTube Web Downloader

ducktube is a self-hosted flask YouTube web downloader for both video and audio using yt-dlp.

saved files are available by link and in /downloads on your server.

just a fun project for myself, im sure there are better alternatives

## Usage (Python)

make sure you have [python](https://www.python.org/downloads/) installed.

1. clone the repository
   ```
   git clone https://github.com/ducky4life/ducktube.git
   ```
2. move into directory
   ```
   cd Ducktube
   ```
3. create downloads folder
   ```
   mkdir downloads
   ```
4. install dependencies
   ```
   pip install -r requirements.txt
   ```
5. run the app
   ```
   python app.py
   ```
6. go to http://localhost:8080/

## Usage (Docker)
> [!IMPORTANT]
> Note that you might have to delete `arm64v8/` from the first line of the Dockerfile: `FROM arm64v8/python:3.11-slim` if using another archetecture

1. clone the repository
   ```
   git clone https://github.com/ducky4life/Ducktube.git
   ```
2. move into directory
   ```
   cd Ducktube
   ```
3. create downloads folder
   ```
   mkdir downloads
   ```
4. build the docker image
   ```
   docker build -t ducktube:latest -f Dockerfile .
   ```
5. run the docker container
   ```
   docker run -p 8080:8080 --name ducktube ducktube:latest
   ```
6. go to http://localhost:8080/
