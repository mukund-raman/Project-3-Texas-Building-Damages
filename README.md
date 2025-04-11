# Texas Building Damages Inference Server

This project provides an inference API server for classifying building images.

## Prerequisites

- Docker installed on your machine
- Docker Compose installed

## Build the Docker Container Image

Use the following command to build the docker image:

```bash
docker build -t mkr2497/texas-building-damages:latest .
```

## Running the Container with Docker Compose

1. Ensure you have the `docker-compose.yml` file in your project directory.
2. Run the following command to start the container:

   ```bash
   docker-compose up -d
   ```

   This command will download the image from Docker Hub (if not already present) and spin up the container.

3. The API service is accessible on port `5000`.

## Using the API

### 1. Model Summary Endpoint

- **Endpoint:** `/summary`
- **Method:** GET

**Example:**

```bash
curl http://localhost:5000/summary
```

This request will return a JSON response containing the model information such as its name, architecture, version, description, and the total number of parameters.

### 2. Image Classification Endpoint

- **Endpoint:** `/inference`
- **Method:** POST
- **Form Data:** Binary image file under the key `image`

**Example using curl:**

```bash
curl -X POST http://localhost:5000/inference \
  -F "image=@/path/to/your/image.jpg"
```

This request will upload an image to the model and return a JSON response with the predicted label (`damage` or `no_damage`).

## Stopping the Container

To stop and remove the container, run:

```bash
docker-compose down
```

## Troubleshooting

- Check container logs:

  ```bash
  docker-compose logs
  ```

- To re-pull the latest image:

  ```bash
  docker-compose pull
  docker-compose up -d
  ```