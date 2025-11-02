FROM python:3

WORKDIR /app
COPY . .
RUN pip install .

EXPOSE 8000
CMD ["pserve", "development.ini"]
