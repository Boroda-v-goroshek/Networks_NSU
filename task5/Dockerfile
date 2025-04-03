FROM python:3.12.3
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install psycopg2
WORKDIR /task5
COPY task5.py .
CMD ["python3", "task5.py"]