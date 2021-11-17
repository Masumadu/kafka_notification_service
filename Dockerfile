# build image from python
FROM python:3.9

# send app logs to terminal
ENV PYTHONUNBUFFERED 1

# set working directory in container
WORKDIR /app

#install poetry in container
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# copy specified files to container app directory
COPY pyproject.toml poetry.lock* /app/

# Install dev dependencies to run tests
ARG INSTALL_DEV=true
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

# copy all files in current directory to container's app directory
COPY . .

# run command when container starts
#CMD [ "flask", "run", "--host=0.0.0.0", "--port=5002"]

ENTRYPOINT ["app/script/entrypoint"]
