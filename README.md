# AWS Cognito EXAMPLE

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is used to mock the steps to use AWS Cognito identity pool with developer provider name.

`Update the config.properties values to make the example working`

## Mock up steps
1. Assume the openid is already acquired
2. Create the identity id from Cognito identity pool
3. Get token from STS
4. Use the temporary credentials to access s3 service

## Configurations

- create virtualenv

```shell script
python -m venv venv
```

- activate virtualenv
- install packages from requirements.txt

```shell script
pip install -r requirements.txt
```

More details can be find in [blog](https://www.yuque.com/wayneshen/aws/ohgn7x)