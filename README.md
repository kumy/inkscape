# AI, PDF and EPS to SVG converter
Convertes files in `.ai`, `.pdf` and `.eps` format to `.svg` images using
Ghostscript and Inkscape. Based on [Inkscape as a service](https://github.com/as-a-service/inkscape).

### URL parameters:

* `file`: input file added as `multipart/form-data`

## Running the server locally

* Build with `docker build . -t inkscape`
* Start with `docker run -p 1234:8080 inkscape`
* Open in your browser at `http://localhost:1234"`

## Deploy to Google Cloud

[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://deploy.cloud.run)