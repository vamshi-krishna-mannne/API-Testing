FROM python:3.7-alpine



WORKDIR /
RUN pip3 install -r requirements.txt
COPY . /
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]