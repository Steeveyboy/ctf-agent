FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends curl iputils-ping \
    && rm -rf /var/lib/apt/lists/*
CMD ["sleep", "infinity"]
