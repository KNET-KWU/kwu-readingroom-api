FROM python:3.10

COPY . /app/readingroom_crawler

WORKDIR /app

RUN pip3 install --upgrade pip

RUN pip3 install -r ./readingroom_crawler/requirements.txt

RUN python ./readingroom_crawler/setup.py

CMD python ./readingroom_crawler/main.py