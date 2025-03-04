FROM python:3-alpine3.15
WORKDIR /chatbot
COPY . /chatbot
RUN pip install -r requirements.txt
EXPOSE 3000
CMD python ./app.py