# alpine is minimal but 'tensorflow' not available on that so we use debian
FROM python:3.10

WORKDIR /app

# update system
RUN apt update && apt upgrade -y

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]