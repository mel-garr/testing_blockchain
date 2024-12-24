FROM python:3.9

WORKDIR /app

RUN apt-get update && apr-get install -y vim

RUN useradd -m -u 1000 mel-garr && \
    chown -R mel-garr:mel-garr /app

USER mel-garr

CMD ["python", "manage.py", "0.0.0.0:8000"]