# sam-app-connect-to-host-localhost

This is a minimal working example to figure out how to let a lambda running
locally via [SAM CLI](https://aws.amazon.com/serverless/sam/) can call a server
running on the host machine's localhost.

Referred to on StackOverflow question: [How to connect a lambda to a database accessible locally on Mac's localhost when using sam](https://stackoverflow.com/questions/74318930/how-to-connect-a-lambda-to-a-database-accessible-locally-on-macs-localhost-when)

Contents:

- `./hello.py`
  - A simple Python server that can be run on the host machine.
  - Accessible on `http://127.0.0.1:5000/`
- `./hello_world/app.py` :
  - A Lambda function that calls the server running on the host machine.
  - When deployed with SAM CLI, this is available on `http://127.0.0.1:3000/`

## Pre-requisites

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

### Install dependencies

```bash
pip3 install -r requirements.txt
```

## Deploy a python server locally on your machine

```bash
flask --app hello run
```

## Use the SAM CLI to build and run a lambda locally

### Build first time

```bash
sam build --use-container
```

### Build and run

```bash
sam build && sam local start-api
```
