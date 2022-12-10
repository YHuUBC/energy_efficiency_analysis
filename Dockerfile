# Docker image for Energy efficiency analysis project
# Date: Dec 10, 2022x

FROM jupyter/scipy-notebook:85f615d5cafa

RUN  conda install python=3.10.8
