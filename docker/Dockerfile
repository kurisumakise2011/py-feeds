FROM python:3.7-alpine
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers
COPY setup.py setup.py
RUN pip install -r setup.py
COPY ../. .
CMD ["python", ".app/main.py"]