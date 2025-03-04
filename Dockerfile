FROM python:3.12

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /xorazmfc

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . . 

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]