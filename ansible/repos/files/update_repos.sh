#!/bin/bash

BASE_PATH=$(pwd)
REPOS=("erp")

for repo in "${REPOS[@]}"; do
    echo "Updating repo: ${BASE_PATH}/${repo}"
    createrepo_c --update ${BASE_PATH}/${repo}
done
