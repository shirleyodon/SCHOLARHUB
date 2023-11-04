FROM python:alpine
EXPOSE 5000
WORKDIR /backend
COPY . /backend
RUN pip install -r requirements.txt
CMD ["gunicorn", "-b", ":5000", "run:app"]

