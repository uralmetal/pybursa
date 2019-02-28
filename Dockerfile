FROM python:3

RUN mkdir src/
COPY python-requirenments.txt src/
WORKDIR /src/
RUN pip install -r python-requirenments.txt
ADD . /src/
EXPOSE 8000
ENTRYPOINT python3 manage.py runserver 0.0.0.0:8000
