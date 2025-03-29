FROM python:3.12.9-bookworm

WORKDIR /flask

COPY . .
RUN pip install -r requirements.txt

CMD ["python", "src/main.py"]