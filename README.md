# image-to-hearts-telegram-bot

Create docker image

``` shell
docker build -t <image name> .
```
ENV file example

``` shell
TOKEN=telegram:token
IMG_PATH=/images
```

Run

``` shell
docker run --env-file <path to the ENV file> -v <your local directory for images>:<IMG_PATH from the ENV file> <image name>
```
