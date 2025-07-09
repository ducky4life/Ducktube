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

make sure you have [docker](https://www.docker.com) installed.

### Using pre-built images

1. get the correct package for your archetecture
   [amd64](https://github.com/ducky4life/ducktube/pkgs/container/ducktube%2Fducktube-amd64):
   ```
   docker pull ghcr.io/ducky4life/ducktube/ducktube-amd64:latest
   ```
   [arm64](https://github.com/ducky4life/ducktube/pkgs/container/ducktube%2Fducktube-arm64):
   ```
   docker pull ghcr.io/ducky4life/ducktube/ducktube-arm64:latest
   ```
2. run the docker container
   amd64:
   ```
   docker run -p 8080:8080 --name ducktube ghcr.io/ducky4life/ducktube/ducktube-amd64:latest
   ```
   arm64:
   ```
   docker run -p 8080:8080 --name ducktube ghcr.io/ducky4life/ducktube/ducktube-arm:latest
   ```
2. go to http://localhost:8080/

### Building the images from source (recommended)

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
4. build the docker image for your archetecture
   amd64:
   ```
   docker build -t ducktube:latest -f amd64.Dockerfile .
   ```
   arm64:
   ```
   docker build -t ducktube:latest -f arm64.Dockerfile .
   ```
5. run the docker container
   ```
   docker run -p 8080:8080 --name ducktube ducktube:latest
   ```
6. go to http://localhost:8080/


## to do list

1. publish docker images for arm64 and amd64 to github container registry
2. download playlists