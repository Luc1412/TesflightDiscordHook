FROM python:3.11-slim-buster

WORKDIR /app

COPY requirements.txt ./

RUN pip install -U -r requirements.txt && \
    # remove caches
    rm -rf /root/.cache/pip/* && \
    find /usr/local -depth \
        \( \
            \( -type d -a \( -name test -o -name tests \) \) \
            -o \
            \( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
        \) -exec rm -rf '{}' +

COPY . .

ENTRYPOINT ["python", "-OO", "main.py"]
