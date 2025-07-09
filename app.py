from flask import Flask, request, render_template, send_from_directory
from threading import Thread
from waitress import serve
from downloader import download_audio

app = Flask('')

@app.route('/', methods=['GET', 'POST'])
def main_route():
    message = ""
    filepath = ""

    if request.method == 'POST':
        url = request.form.get('textbox', '')
        action = request.form.get('action')

        if url:
            try:
                if action == "Download Audio Only":
                    filename = download_audio(url, audio=True)

                else:
                    filename = download_audio(url, audio=False)

                filepath = filename.split("/")[-1].replace("\\", "/").replace("downloads/", "").replace(".webm", ".mp3")
                message = f"Downloaded and saved as: {filepath}"

            except Exception as e:
                message = f"Error: {e}"
        else:
            message = "Please enter a URL."
            
    return render_template("index.html", message=message, filepath=filepath)

def run():
    serve(app, host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()

@app.route('/downloads/<path:filename>')
def download_file(filename):
    return send_from_directory('downloads', filename, as_attachment=True)

keep_alive()
