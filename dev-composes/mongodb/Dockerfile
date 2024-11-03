FROM mongo:8.0.3

# Copy the init script to the container
COPY ./mongodb/init-mongo.sh /docker-entrypoint-initdb.d/init-mongo.sh

# Ensure the script has execute permissions
RUN chmod +x /docker-entrypoint-initdb.d/init-mongo.sh
