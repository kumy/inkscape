import os
import shutil
import requests
import tempfile
import logging

from gevent.pywsgi import WSGIServer
from flask import Flask, after_this_request, render_template, request, send_file, abort
from subprocess import call


UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = set(['pdf', 'eps', 'ai', 'svg'])


app = Flask(__name__)


def convert_file(input_file_path, output_dir, output_file_path):
    extension = input_file_path.rsplit('.', 1)[1].lower()

    if extension == "pdf":
        call('inkscape --file %s --export-plain-svg %s --without-gui' %
            (input_file_path, output_file_path), shell=True)

    elif extension == "svg":
        call('inkscape --file %s --export-plain-svg %s --without-gui' %
            (input_file_path, output_file_path), shell=True)

    elif extension == "ai":
        call('inkscape --file %s --export-plain-svg %s --without-gui' %
            (input_file_path, output_file_path), shell=True)

    elif extension == "eps":
        work_dir = os.path.dirname(output_file_path)
        temp_file_path = os.path.join(work_dir, 'temp.pdf')

        call(["ps2pdf -dEPSCrop %s %s" % (input_file_path, temp_file_path)], shell=True)

        call('inkscape --file %s --export-plain-svg %s --without-gui' %
            (temp_file_path, output_file_path), shell=True)


@app.route('/', methods=['GET', 'POST'])
def api():
    # Return UI page
    if request.method == 'GET':
        return render_template('index.html')

    # Convert file
    if request.method == 'POST':
        work_dir = tempfile.TemporaryDirectory()
        output_file_path = os.path.join(work_dir.name, 'output.svg')

        # check if the post request has the file part
        if 'file' not in request.files:
            logging.error("No file detected in request files")
            abort(400)

        file = request.files['file']
        if not file:
            logging.error("No file found")
            abort(400)

        if file.filename == '':
            logging.error("Filename is empty")
            abort(400)

        input_extension = file.filename.rsplit('.', 1)[1].lower()
        input_file_path = os.path.join(work_dir.name, 'input.' + input_extension)

        if not input_extension in ALLOWED_EXTENSIONS:
            logging.error("Unsupported file extension")
            abort(400)

        # Store input file to disk
        file.save(input_file_path)

        # Convert and store output file
        convert_file(input_file_path, work_dir.name, output_file_path)

        # Delete files after conversion
        @after_this_request
        def cleanup(response):
            work_dir.cleanup()
            return response

        if os.path.exists(output_file_path):
            return send_file(output_file_path, mimetype='image/svg+xml')

        else:
            logging.error("Could not convert file")
            return abort(500)


if __name__ == "__main__":
    http_server = WSGIServer(('', int(os.environ.get('PORT', 8080))), app)
    http_server.serve_forever()
