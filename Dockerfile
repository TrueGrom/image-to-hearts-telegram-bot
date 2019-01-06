FROM alpine
LABEL authors="truegrom@gmail.com, aleksl0l@yandex.ru"
RUN apk --update add build-base python3 python3-dev libffi-dev openssl-dev jpeg-dev
RUN mkdir /app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip && python3 -m pip install -r requirements.txt
COPY . .
CMD ["python3", "bot.py"]
