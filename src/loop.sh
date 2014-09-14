#!/usr/bin/env bash

unset sleepPID
trap 'echo TERMinated; kill $sleepPID; exit' TERM

while true; do
  date  +"  %Y-%m-%d %H:%M:%S %Z looping every 10 seconds"
  sleep 10 & sleepPID=$!; wait
done
