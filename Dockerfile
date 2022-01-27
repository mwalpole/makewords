FROM python:3.8-slim-buster
WORKDIR /app
COPY . .
RUN pip3 install -rrequirements.txt
RUN pip3 install .
CMD ["makewords"]