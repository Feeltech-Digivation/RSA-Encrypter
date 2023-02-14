# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9

EXPOSE 8080

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
ENTRYPOINT [ "python" ]
CMD ["run.py" ]
