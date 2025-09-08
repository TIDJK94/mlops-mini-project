FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy only requirements first for better layer caching
COPY requirements.txt /app/requirements.txt

# Install runtime dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy application code (including regression.joblib)
COPY . /app

# Create a non-root user and switch to it (optional but recommended)
RUN adduser --disabled-password --gecos "" appuser \
    && chown -R appuser:appuser /app
USER appuser

RUN python train_model.py

EXPOSE 5094

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5094"]