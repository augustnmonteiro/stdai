#!/bin/bash

HOST="localhost"
PORT=9999

"$@" 2> >(tee /dev/tty | nc localhost 9999) > >(tee /dev/tty)