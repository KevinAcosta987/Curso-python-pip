FROM python:3.10.12

WORKDIR /web-server
COPY requirements.txt /web-server/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /web-server/requirements.txt

COPY . /web-server
CMD ["uvicorn", "main:web-server", "--host", "0.0.0.0", "--port", "80:80"]

