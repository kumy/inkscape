FROM python:3-alpine

ENV APP_HOME /app
WORKDIR $APP_HOME

RUN apk add inkscape \
        build-base \
        # Install fonts
        msttcorefonts-installer fontconfig && \
    update-ms-fonts && \
    fc-cache -f

RUN apk add ghostscript-fonts ghostscript

RUN pip install Flask requests gevent

RUN apk add --update nodejs npm
RUN npm install -g @tracespace/cli
RUN tracespace -h

COPY . $APP_HOME

CMD ["python", "inkscape.py"]
