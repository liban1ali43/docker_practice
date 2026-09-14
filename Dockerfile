FROM python:3.8-slim
WORKDIR /app
COPY flask_mysql_connect.py .
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/* \
    && pip install flask mysqlclient
EXPOSE 5003
CMD ["python", "flask_mysql_connect.py"]