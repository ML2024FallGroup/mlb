## Prerequisites
- Have docker installed and running on your system

## Getting Started
Create a python virutal environment

```bash
python3 -m venv venv
```

Activate the virual environment

```bash
\venv\Scripts\activate
```
mac
```bash
source \venv\bin\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run a rabbitMq instance

```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4.0-management
```

Run a redis instance
 ```bash
docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest
```

Start Celery
 ```bash
celery -A project worker --loglevel=info -P gevent
```
Do not close the celery terminal. use a different terminal

Start the server
```bash
python3 manage.py runserver
```
