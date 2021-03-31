from flask import Flask, request, send_from_directory
from logic import dl


app = Flask(__name__, static_folder='../frontend/dist', template_folder='../frontend/dist')

@app.route('/', defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/api/download/mp4', methods=['POST'])
def download_mp4():
  link = request.data
  dl(link)

@app.route('/api/download/txt')
def download_txt():
    return send_file('output/transcript.txt',
                     mimetype='text/csv',
                     attachment_filename='transcript.txt',
                     as_attachment=True)

app.run(debug=True)