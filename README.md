# Setup examples

First start a local poetry environment:

```shell
curl -sSL https://install.python-poetry.org | python3 -
export PATH="/home/<user>/.local/bin:$PATH"
cd <project>
poetry use env python3
poetry install
```

How to build and run a docker container:

```shell
docker build -t my-python-app .
docker run -it --rm --name my-running-app my-python-app
```
