FROM python:3

WORKDIR /app
COPY . .
RUN pip install .

ARG DATABASE_PUBLIC_URL

RUN init_db railway.ini
EXPOSE 8000
CMD ["pserve", "railway.ini"]
