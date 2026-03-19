#!/bin/bash

protocol=$1
scenario=$2

locust --config=./scenarios/${protocol}/gateway/${scenario}/v1.0.conf --show-task-ratio-json > locust_${protocol}_gateway_${scenario}_ratio.json

locust --config=./scenarios/${protocol}/gateway/${scenario}/v1.0.conf

load-testing-hub upload-locust-report --yaml-config=./scenarios/${protocol}/gateway/${scenario}/load_testing_hub.yaml