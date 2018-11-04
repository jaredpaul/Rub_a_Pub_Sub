FROM python:3.6.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ADD userFile.py
ENTRYPOINT ["python"]
CMD ["python", "./userFile.py"]

