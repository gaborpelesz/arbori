# AR bori python image classification backend (a.k.a. Black Box API)

## Init/Install project

First clone the repo.

```bash
git clone https://${USERNAME}@bitbucket.org/exahexa/ar-bori-model.git
```

At first, the command **make dev** will create the docker image (After that you can rebuild with **make build**)

```bash
make run
```

## Makefile commands
```bash
# Build the python service image and force remove previous instance
make build

# Push to docker hub
make push

# Run all the service containers with compose (docker-compose up) and force recreate container for python service
make run

# Run developement environment (make run with docker-compose.dev.yml)
make dev

# Get into the python service's container shell
make exec

# Turn down running docker-compose services
make down
```

---

## Usage

**Server will be listening on port 3000**

### API endpoints:
- POST /predict

### POST /predict
Receives an image and tries to predict its class.

- request: **POST /predict**
- required headers: **{Content-Type: application/json}**

JSON properties:
```json
{
  "image": "/9j/4ROSR ... FAf/Z"
}
```

- **image**: Base64 encoded image that contains the object.

**Response:**
```json
{
    "status": "Success", 
    "prediction": {
        "class": "phone", 
        "probability": "0.9996686"
        }, 
    "processing_runtime": "1125.247ms"
}
```

- **status**: Indicates the result of the request.
- **prediction**:
    - *class*: The predicted class of the image.
    - *probability*: The probability of the image being the instance of that class
- **processing_runtime**: The total runtime of transforming and predicting the image's class

---

### Error handling (HTTP 400, HTTP 500)

All internal server errors and bad request has the following JSON response structure sent with the appropriate status code:
```json
{
  "status": "Failed",
  "status_message": " ...Developers explonation... ",
  "error_message": " ...Error from the application... "
}
```

---

## Postman

Postman collection file: `postman_example/armuseumguide.postman_collection.json`.

© gaborpelesz 2019