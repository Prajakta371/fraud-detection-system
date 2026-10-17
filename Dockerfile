# 1. Start from a ready-made Linux image that already has Python 3.11
FROM python:3.11-slim

# 2. XGBoost needs this system library; the slim image doesn't include it
RUN apt-get update && apt-get install -y --no-install-recommends libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# 3. Make /app the working folder inside the container
WORKDIR /app

# 4. Copy only requirements first, then install libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the backend code and model files
COPY backend/ backend/

# 6. Document the port the app listens on
EXPOSE 8000

# 7. The command that starts the app (same as your Procfile)
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]