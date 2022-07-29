FROM python:3.8.9-slim-buster
WORKDIR /app 
COPY . . 
RUN pip3 install -r requirements.txt
ENV DATABASE_PASSWORD=${DATABASE_PASSWORD}
ENV SERVER_NAME=${SERVER_NAME}
ENV SECRET_KEY=${SECRET_KEY}

#ARG DATABASE_URI

# RUN python3 create.py 


EXPOSE 5001
ENTRYPOINT ["python", "app.py"]