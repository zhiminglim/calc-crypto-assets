#!/bin/bash

set -e

set -a
source config.env
set +a

python balance-kc.py > output.txt