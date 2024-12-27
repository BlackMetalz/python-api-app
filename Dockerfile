# Build stage
FROM python:3.10-alpine3.19

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TZ=Asia/Ho_Chi_Minh

WORKDIR /app
# Copy only requirements to cache them in docker layer
COPY requirements.txt .

# Switch to root user to install dependencies
USER root

RUN pip install --no-warn-script-location --upgrade pip \
    && pip install --no-cache-dir setuptools==70.0.0 \
    && pip install --no-cache-dir -r requirements.txt

# Create non-root user
RUN addgroup -S myapp && adduser -S myapp -G myapp
# Copy the application code and set ownership
COPY --chown=myapp:myapp . /app

# Switch to non-root user
USER myapp
# Expose port
EXPOSE 5000

ENTRYPOINT ["python", "app.py"]