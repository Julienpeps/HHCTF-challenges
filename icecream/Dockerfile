FROM python

EXPOSE 5000

RUN adduser --system app

WORKDIR /app

COPY app /app

COPY flag.txt /flag.txt

RUN chown -R root:root /app

USER app

RUN pip install -r requirements.txt

CMD ["python", "-u", "app.py"]
