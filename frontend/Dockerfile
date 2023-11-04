FROM python:alpine
EXPOSE 5001
WORKDIR /frontend
COPY . /frontend
RUN pip install -r requirements.txt
CMD ["gunicorn", "-b", ":5001", "run:app"]