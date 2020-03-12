# AI, PDF and EPS to SVG converter
Convertes files in `.ai`, `.pdf` and `.eps` format to `.svg` images using
Ghostscript and Inkscape. Based on [Inkscape as a service](https://github.com/as-a-service/inkscape).

### POST parameters:

* `file`: input file added as `multipart/form-data`

## Running the server locally (docker)

* Build with `docker build . -t inkscape`
* Start with `docker run -p 8080:8080 inkscape`
* Open in your browser at `http://localhost:8080"`

## Running the server locally (docker-compose)

* Run/Build using `docker-compose up --build`
* Open in your browser at `http://localhost:8080"`

## Deploy to Google Cloud

[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://deploy.cloud.run)