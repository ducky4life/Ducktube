FROM --platform=linux/arm64/v8 arm64v8/python:3.11-slim

LABEL org.opencontainers.image.source="https://github.com/ducky4life/Ducktube"

RUN apt-get update && apt-get install -y ffmpeg

COPY requirements.txt /

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN mkdir /downloads

WORKDIR /

COPY static static

COPY templates templates

COPY app.py downloader.py /

EXPOSE 8080

CMD ["python", "app.py"]