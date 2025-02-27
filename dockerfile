FROM python

WORKDIR /app

COPY requirments.txt requirments.txt

RUN pip install -r requirments.txt


COPY . .


EXPOSE 5000

CMD [ "python","app.py"]