FROM python:3.12.0-alpine3.18

WORKDIR /opt/app

COPY . .

RUN apk update && \
    apk add --no-cache \
        bash \
        binutils \
        openssl \
        curl  && \
    update-ca-certificates && \
    pip3 install --upgrade pip && \
    pip3 install -r requirments.txt && \
    rm requirments.txt && \
    mv ./src/* .

ENTRYPOINT ["/usr/local/bin/python" ]

CMD ["-u","main.py"]
