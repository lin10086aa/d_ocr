FROM python:3.11-slim

ARG PIP_INDEX_URL=https://pypi.org/simple
ENV PADDLEOCR_HOME=/app/paddleocr_models

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --timeout 120 -i "${PIP_INDEX_URL}" -r requirements.txt

COPY backend/ ./backend/
COPY pyproject.toml .

RUN mkdir -p uploads outputs

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
