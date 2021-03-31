from flask import Flask, request, send_from_directory
from logic import dl


app = Flask(__name__, static_folder='../frontend/dist', template_folder='../frontend/dist')

@app.route('/', defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/api/download/mp4', methods=['POST'])
def download_mp4():
  r = request.get_json()
  link = r['link']
  dl(link)

@app.route('/api/download/txt', methods=['POST'])
def download_txt():
    return send_file('output/transcript.txt',
                     mimetype='text/csv',
                     attachment_filename='transcript.txt',
                     as_attachment=True)

@app.route('/test', methods=['POST'])
def test():
    sample = request.data
    return sample


app.run(debug=True)