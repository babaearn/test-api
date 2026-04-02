# Use official Python 3.11 as our base
FROM python:3.11-slim

# 1. Install Node.js (needed for pmxtjs bridge)
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean

# 2. Install pmxtjs globally (the Node extension pmxt needs)
RUN npm install -g pmxtjs

# 3. Set up the working directory
WORKDIR /app
COPY . .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Launch the validation test
CMD ["python", "pmxt_sdk_validation.py"]
