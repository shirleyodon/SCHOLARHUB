FROM python:alpine
EXPOSE 5000

# ENV POSTGRES_USER=YWRtaW4=
# ENV POSTGRES_DB=bWVtb2lyZQ==
# ENV POSTGRES_PASSWORD=YWRtaW4=
# ENV POSTGRES_HOST=bG9jYWxob3N0

WORKDIR /backend
COPY . /backend/
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "-w", "5", "-b", ":5000", "launch:app", "--reload"]
