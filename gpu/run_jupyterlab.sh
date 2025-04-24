#!/bin/bash

ipaddr=$(hostname -I | cut -d' ' -f 1)
uid=$(id -u)
port=$((50001 + uid))

jupyter lab --ip=${ipaddr}  --port=${port}

