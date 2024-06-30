FROM python:3.11

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir poetry \
    \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev \
    \
    && pip uninstall --yes poetry

COPY . ./

WORKDIR stringus_api

CMD [ "uvicorn", "main:app", "--host", "000.0.0.0", "--port", "8000"]

EXPOSE 8000