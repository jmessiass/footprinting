# Python API WpScan
## Web API Server using Python and WpScan

This tool is writed in python and we have a web API server using flask and python. We need to make a POST request passing an output file from WpScan tool and the api.py will return a clean json answer.

## Features

- API creation using Python with few line codes;
- Read, write and answer in JSON;
- Read the output file from WpScan;
- Information's organization collected from WpScan;
- Easy to run and can be reused to others output files;

## Tech

It was used some open source projects;

- [Python] - Language used to write the code.
- [Flask] - Python framework to create the API.
- [WpScan] - Tool that find information about WordPress.

## Installation

To use this tool you need an output file in JSON format from WpScan tool that you already runned in a WordPress application.


```sh
wpscan --url http://sitewordpress.com/ -f json -o wpscan
```

It was used Python version 3.9.2 in the PoC.

Do clone of the project. Access the folder python-api-wpscan and install the flask lib using pip.


```sh
git clone https://github.com/jmessiass/python-api-wpscan.git
cd footprinting
pip install flask
```

## How to Use

After do the previous steps just run the api.py script.

```sh
python api.py
```
Will be created an API in port 5000. After that you need to execute a CURL request in your created API. Pass the output file in JSON format from WpScan.

```sh
curl -X POST -H "Content-Type: application/json" -d '{"url":"~/wpscan"}' http://localhost:5000/wordpress
```
After you realized the POST request the tool will return a JSON output with the information cleaned about the WordPress application. Returning just the most important information about the app. This script can be customized and adapt to others scenarios that you need.
