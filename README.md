# Kucoin Scripts

This project contains a script to retrieves real-time information from KuCoin account.

The current version compute sum of all assets and print out the value on your terminal.

## Requirements

- You will need a KuCoin account with an API Key created.
- You will also need python3 (>=v3.6) on your machine to run the python script locally.

## How to use this script

> **Note**: Apikeys are for GET requests only.

First, create a file in the root directory `config.env`, and paste the following variables into the file. Fill in the values for apikey, secret and passphrase which you would have created and generated from your KuCoin account:

```env
API_KEY="xxx"
API_SECRET="xxx"
API_PASSPHRASE="xxx"
BASEURL="https://api.kucoin.com"
```

There are also some libraries used in the python script which you may need to download onto your machine. For that, use `pip` or any package manager to download accordingly the packages which are missing.

```shell
$ pip install time hmac hashlib base64 requests json
```

Next, run `chmod +x run.sh` to ensure you have execute privileges. Once done, execute `./run.sh` from your CLI.

Example output:

```shell
$ ./run.sh 
Initializing main function...
response code=200 when hitting /api/v1/prices
response code=200 when hitting /api/v1/accounts

Computing sum of all asset values...
holding of XNO has balance of 10.0000000 with market price $1.03870770
holding of USDT has balance of 333.12345678 with market price $1.00020000
total asset values (USD) = $xxx.xxx
```

<br />

# References

[KuCoin Developers' Docs](https://docs.kucoin.com/#rest-api-2)