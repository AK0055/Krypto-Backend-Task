FROM python:3.7-alpine
WORKDIR /app
COPY ../main.py .
COPY ../requirements.txt .
RUN apk add --update alpine-sdk
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install --upgrade pip
RUN pip install pydantic
RUN pip install jwt
RUN pip install fastapi
RUN pip install mailer
RUN pip install PyJWT
RUN pip install pymongo
RUN pip install redis
RUN pip install uvicorn
RUN pip install requests
RUN uvicorn main:app --reload --host 0.0.0.0 --port 80
EXPOSE 80
