FROM python

EXPOSE 5000

RUN adduser --system app

USER app

WORKDIR /app

COPY app /app

RUN pip install -r requirements.txt

CMD ["python", "-u" ,"app.py", "HHCTF{Fl4Gs_arE_Fun_iNDE3d}"]