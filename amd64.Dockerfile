FROM python:3.11-slim

LABEL org.opencontainers.image.source="https://github.com/ducky4life/Ducktube"

WORKDIR /

COPY static static

COPY templates templates

COPY app.py downloader.py requirements.txt /

RUN mkdir /downloads

RUN apt-get update && apt-get install -y ffmpeg

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]