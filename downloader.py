import yt_dlp

def download_audio(url, audio=False):
    if audio:
        ydl_opts = {
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }, {
                'key': 'EmbedThumbnail',
            }, {
                'key': 'FFmpegMetadata',
                'add_metadata': True,
            }]
        }
    else:
        ydl_opts = {
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'format': 'best[ext=mp4][acodec!=none][vcodec!=none]/bestvideo+bestaudio/best',
            'writethumbnail': True,
            'merge_output_format': 'mp4',
            'postprocessors': [{
                'key': 'EmbedThumbnail',
            }, {
                'key': 'FFmpegMetadata',
                'add_metadata': True,
            }]
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        return filename
