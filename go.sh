#!/bin/bash -xe

# change the kernel
start() {
    jupyter kernelspec uninstall -y llmk || true
    jupyter kernelspec install --user llmk/
    jupyter lab --ip=0.0.0.0 --allow-root
}

pip install jupyter-client ipykernel pyzmq jupyterlab notebook

start
