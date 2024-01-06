#!/bin/bash

#the path to the github repo
DOCKERREPO="oliwierjaworski/simple-python-script"
DOCKERTAG="Oli-Dev"

#pull from the docker repo
docker pull "$DOCKERREPO:$DOCKERTAG"

#latest image is saved here
LATEST_IMAGE_ID=$(docker inspect --format '{{.Id}}' "$DOCKERREPO:$DOCKERTAG")

#find the container to restart 
IMAGEIDREBOOT=$(docker image ls | grep "$DOCKERTAG" | awk '{print $3}')
#find the container to update and remove old image with xargs which holds the image id $1=name, $2 = tag, $3=id
IMAGEIDUPDATE=$(docker image ls | grep "<none>" | awk '{print $3}')

echo -e "found the following image: "$IMAGEIDREBOOT"."

if [ -z "$IMAGEIDREBOOT" ]; then
        echo -e "No file with $DOCKERTAG was found."

elif [ -n "$IMAGEIDREBOOT" ]; then
        echo -e "Found the image:$DOCKERTAG"

        #restart container if it exited
        CONTAINERS_TO_RESTART=$(docker ps -a -q -f status=exited --filter ancestor="$IMAGEIDREBOOT")

        if [ -n "$CONTAINERS_TO_RESTART" ]; then
                echo -e "the following container will be restarted : $CONTAINERS_TO_RESTART"
                sudo docker restart $CONTAINERS_TO_RESTART
        else
                echo -e "no container to be restarted was found"
        fi
fi
if [ -n "$IMAGEIDUPDATE" ]; then

        # Find containers using the image to be removed
        CONTAINERS_TO_REMOVE=$(docker ps -a -q --filter ancestor="$IMAGEIDUPDATE")

        # Check if there are any containers to remove
        if [ -n "$CONTAINERS_TO_REMOVE" ]; then
            echo -e "Containers using image $IMAGEIDUPDATE found. Forcefully removing them."
            sudo docker rm -f $CONTAINERS_TO_REMOVE
            sudo docker rmi $IMAGEIDUPDATE

            #starts a container using the newest image in detached mode by the name of --name
            sudo docker run --name pythonapplication -d $LATEST_IMAGE_ID

        else
             echo -e "No container was found to remove"
        fi
fi

