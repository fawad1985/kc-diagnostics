FROM python:2.7.16


RUN apt-get install -y
RUN curl -s https://bootstrap.pypa.io/get-pip.py | python
RUN pip install \
    pep8 \
    pipenv \
    pytest \
    pytest-cov \
    pytest-mock \
    pytest-watch


RUN echo "alias ll='ls -alFh --color=auto'" >> /root/.bashrc
RUN echo "alias l='ls -alFh --color=auto'" >> /root/.bashrc


RUN mkdir /code
WORKDIR /code