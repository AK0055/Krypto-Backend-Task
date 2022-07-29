FROM python:3.7-alpine
WORKDIR /app
COPY ../main.py .
COPY ../requirements.txt .
RUN apk update
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN uvicorn main:app --reload 
EXPOSE 8000
