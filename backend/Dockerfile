FROM python:3.10

COPY . /app/backend

WORKDIR /app

RUN pip3 install --upgrade pip

RUN pip3 install -r ./backend/requirements.txt

RUN python ./backend/setup.py

EXPOSE 8080

CMD python ./backend/main.py