from flask import Flask, after_this_request, render_template, request, send_from_directory
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

app = Flask(__name__)

@app.route('/download')
def download():
    @after_this_request
    def add_header(response):
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        download_type = request.form.get('download_type')
        yt = YouTube(url)

        if download_type == 'audio':
            ys = yt.streams.get_audio_only()
        else:
            ys = yt.streams.get_highest_resolution()
            
        download_path = ys.download()
        if download_type == 'audio':
            mp4_path = download_path
            mp3_path = mp4_path.replace(".mp4", ".mp3")
            audioclip = AudioFileClip(mp4_path)
            audioclip.write_audiofile(mp3_path)
            audioclip.close()
            os.remove(mp4_path)
            return send_from_directory(os.path.dirname(mp3_path), os.path.basename(mp3_path), as_attachment=True)
        else:
            return send_from_directory(os.path.dirname(download_path), os.path.basename(download_path), as_attachment=True)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)