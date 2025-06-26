FROM python:3.11-slim

# Install Poetry
RUN pip install poetry

# Configure Poetry to not create a virtual environment (we are already in the container)
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VENV_IN_PROJECT=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

# Copy dependency files
COPY pyproject.toml poetry.lock ./

# Install dependencies (production only)
RUN poetry install --only=main && rm -rf $POETRY_CACHE_DIR

# Copy application code
COPY src/ ./src/

# Expose port
EXPOSE 8080

# Command to run with uvicorn for FastAPI
CMD ["poetry", "run", "uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8080"]