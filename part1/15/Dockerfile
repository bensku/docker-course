FROM python:3.9

RUN mkdir /app
RUN pip install aiohttp
COPY main.py /app

CMD [ "python", "/app/main.py" ]