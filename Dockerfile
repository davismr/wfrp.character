FROM python:3

WORKDIR /app
COPY . .
RUN pip install .

RUN init_db development.ini
EXPOSE 8000
CMD ["pserve", "development.ini"]
