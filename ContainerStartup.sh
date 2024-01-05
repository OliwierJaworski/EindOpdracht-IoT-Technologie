#!/bin/bash

#the path to the github repo
DOCKERREPO="oliwierjaworski/simple-python-script"
DOCKERTAG="Oli-Dev"

#pull from the docker repo
docker pull "$DOCKERREPO:$DOCKERTAG"

#latest image is saved here
LATEST_IMAGE_ID=$(docker inspect --format '{{.Id}}' "$DOCKERREPO:$DOCKERTAG")

#remove old image with xargs which holds the image id $1=name, $2 = tag, $3=id
IMAGEID=$(docker image ls | grep "<none>" | awk '{print $3}')

# Find containers using the image to be removed
CONTAINERS_TO_REMOVE=$(docker ps -q --filter ancestor="$IMAGEID")

# Check if there are any containers to remove
if [ -n "$CONTAINERS_TO_REMOVE" ]; then
    echo "Containers using image $IMAGEID found. Forcefully removing them."
    docker rm -f $CONTAINERS_TO_REMOVE
fi

docker rmi $IMAGEID

#starts a container using the newest image in detached mode by the name of --name
docker run --name pythonapplication -d $LATEST_IMAGE_ID
