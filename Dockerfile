# Use the official Python image as the base image
FROM python:3.11.1

RUN pip install --upgrade pip

ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . /app/


# Expose the server port
EXPOSE 8080

# Command to start the server
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]