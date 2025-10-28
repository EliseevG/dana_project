FROM python:3

WORKDIR /usr/src/attack

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
COPY . .

CMD ["python", "attack.py"]