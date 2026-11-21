FROM ghcr.io/astral-sh/uv:0.13.9-python3.13-trixie-slim
WORKDIR /crawler
COPY pyproject.toml uv.lock README.md ./
RUN uv sync --locked --no-install-project
COPY src/ src/
RUN uv sync --locked
ENV UV_NO_DEV=1 UV_NO_SYNC=1
CMD ["uv", "run", "crawler"]
