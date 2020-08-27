FROM python:3.8

WORKDIR /code

COPY Requirements.txt .

RUN pip install -r Requirements.txt

COPY ./src .    

CMD ["python" , "./app.py"]