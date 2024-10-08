FROM python:3.12.3-alpine
WORKDIR /app
COPY . /app
RUN apk add --no-cache bash
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "main.py"]