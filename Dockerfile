FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 82
 
ENTRYPOINT ["uvicorn","model_app:app" ,"--host" , "0.0.0.0" ,"--port" , "82"]