FROM jupyter/scipy-notebook:latest

RUN pip install 'jupyter-ai[all]' pytest ipytest

COPY config.json /tmp/config.json

ENV JUPYTER_ENABLE_LAB=yes
ENV JUPYTER_TOKEN=123

USER root
COPY jupyter-start.sh /jupyter-start.sh
RUN chmod +x /jupyter-start.sh
USER jovyan

ENTRYPOINT ["/jupyter-start.sh"]
