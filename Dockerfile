FROM python:3.13-slim
ARG ENV

# Установка системных пакетов
RUN apt-get update && apt-get -y dist-upgrade && apt-get install -y \
    curl \
    build-essential \
    libpq-dev \
    libmagic-dev \
    && rm -rf /var/lib/apt/lists/*

# Установка uv
#RUN curl -Ls https://astral.sh/uv/install.sh | bash
#ENV PATH="/root/.cargo/bin:${PATH}"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# SET ENV
ENV LIBRARY_PATH /lib:/usr/lib
ENV UV_PYTHON_INSTALL_DIR /opt/uv/python
ENV PYTHONUNBUFFERED 1

ADD . /app
WORKDIR /app

RUN rm -rf /app/.venv

# Копируем только pyproject.toml и устанавливаем зависимости
COPY pyproject.toml uv.lock ./
RUN uv venv && \
    uv sync --active --frozen --no-install-project
#    uv pip install --upgrade pip && \
#    uv pip install --system .

# Копируем остальной код
#COPY . .
COPY src/ /app/

# Collect static files
RUN uv run manage.py collectstatic --noinput

CMD ["uv", "run", "gunicorn", "--chdir", "/app", "worship47.wsgi:application", "--bind", "0.0.0.0:8000"]
