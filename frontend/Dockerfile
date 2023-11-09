FROM python:alpine
EXPOSE 5001

# ENV BACKEND_HOST=bG9jYWxob3N0

WORKDIR /frontend
COPY . /frontend/

RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "-w", "5", "-b", ":5001", "launch:app", "--reload"]