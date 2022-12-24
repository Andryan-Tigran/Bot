FROM python:3.10-slim

COPY . .


EXPOSE 8888

CMD ["python", "main.py"]
