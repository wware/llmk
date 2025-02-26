#!/bin/bash -xe

mkdir -p /home/jovyan/.local/share/jupyter/jupyter_ai
sed "s/ollama:LANGUAGE_MODEL/ollama:${LANGUAGE_MODEL}/" \
    < /tmp/config.json \
    > /home/jovyan/.local/share/jupyter/jupyter_ai/config.json

jupyter lab --ip=0.0.0.0 --allow-root