FROM python:3.9-slim
RUN apt-get update \
    && apt-get install -y \
        libcairo2 \
    && rm -rf /var/lib/apt/lists/*
RUN pip install cairosvg Pillow
WORKDIR /
COPY . .
CMD ["python", "/convert-svg.py"]
