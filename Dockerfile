FROM python:2.7-slim

# Configure environment
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONPATH=/etc/binders:$PYTHONPATH \
    BINDERS_HOME=/home/binders

WORKDIR /app

# Create binders user & install dependencies
RUN useradd -U -m binders && \
    apt-get update && \
    apt-get install -y \
        build-essential \
        libssl-dev && \
    pip install flask-appbuilder

# Add project source
COPY . /app

RUN python setup.py install

# Configure Filesystem
COPY scripts/binders-init.sh /binders-init.sh
RUN chmod +x /binders-init.sh
VOLUME /etc/binders
WORKDIR /home/binders

# Deploy application
EXPOSE 8080
HEALTHCHECK CMD ["curl", "-f", "http://localhost:8080/health"]
ENTRYPOINT ["binders"]
CMD ["runserver"]
USER binders
