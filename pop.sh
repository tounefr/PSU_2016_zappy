#!/bin/bash

TEAM="team1"
COUNT=100

function usage()
{
    echo -e "USAGE\n\t./script [-n team] [-c count]"
    exit 1
}

if [ $# -gt 4 ]
then
    usage
    exit 1
fi

while getopts c:n: option
do
    case $option in
  c)  COUNT=$OPTARG ;;
  n)  TEAM=$OPTARG ;;
  \?)  usage ;;
    esac
done

echo -e "team: $TEAM"
echo -e "count: $COUNT"

BIN="python3 ./src/client/ZappyClient.py"
PRM="-p 4242 -n $TEAM"

for (( c=0; c<$COUNT; c++ ))
do
    sleep 0.2
    eval "$BIN $PRM&"
done
