[![Codewars.nl](https://codewars.nl/static/img/logo.png)](https://codewars.nl/)

[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)
[![Build Status](https://travis-ci.org/0x78f1935/codewars.svg?branch=master)](https://travis-ci.org/0x78f1935/codewars)
![Website](https://img.shields.io/website/https/codewars.nl/static/docs/index.html.svg?down_message=Offline&label=Documentation&up_message=Online)
![GitHub issues](https://img.shields.io/github/issues/0x78f1935/codewars.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dd/codewars.svg)


>Make sure to install all the dependencies needed for each individual module.

## Dependencies
### Required: 
    - `sudo apt-get install gcc`
### Bluetooth
    - `sudo apt-get install libbluetooth-dev`
### Scraping
    - `sudo apt-get install python3-lxml`

---
## Install latest version (stable)

    pip install codewars

### Alternative versions

    1. Go to "https://github.com/0x78f1935/codewars/releases" and do
    2. Download the latest version, unzip it.
    3. Open a virtualenv and navigate to the extracted folder.
    4. Now install the wheel package:
        `python -m pip install codewars-x_x_x_whl`

## Install development version (unstable)

    pip install git+https://github.com/0x78f1935/codewars@master

## Docker

Docker is supported. A image with pre-installed codewars and python3.8 in it.
You can visit the [Docker Hub Repo](https://cloud.docker.com/repository/registry-1.docker.io/codewarsnl/codewars) to download
the latest docker image. There are two tags available. `latest` and `stable`. It's recommended to use the `stable` build.

# Examples
## Info

You can use `import codewars` to check if all dependencies are insalled.

#### Refer for detailed documentation to [here](https://codewars.nl/static/docs/index.html)

>In the following section you will find a brief example on how to use this
>code. This library is ment to grow over time so more examples to come... 

## Logger

    Example:
    ```
    from codewars.logger import Logger
    logger = Logger(appname="test", mode="DEBUG", write=False)
    logger._testLoggerClass()
    logger.info("Hello World!")
    ```

>Note
>----
>The whole module makes use of the `Logger` class instead of the `print` method.

## UnitTests

    Example:
    ```
    from codewars.unittest import Test
    print(Test().run())
    ```

## BlueTooth

    Example:
    ```
    from codewars.bluetooth import Bluetooth
    bt = Bluetooth()  # Initialize the class, Scans once
    scan_results1 = bt.scan()  # Scan area for the default 10 seconds, this is \
    # also executed when this class initializes
    scan_results2 = bt.run_until_discovered()  # Scan until a device is found
    print("Scan results1: {}".format(scan_results1))
    print("Scan results2: {}".format(scan_results2))
    ```

## Wifi

    Example:
    ```
    from codewars.wifi import Wifi
    wifi = Wifi("enp0s31f6")
    sniff_results = wifi.sniff(totalResults=10)
    print(sniff_results)
    info_results = wifi.info(sniff_results)
    print(info_results)
    wifi.sniff_forever(duration=300)
    ```

## Surfer

    Example:
    ```
    from codewars.surf import Surfer
    from asyncio import get_event_loop
    surf = Surfer(loop=get_event_loop())
    # GET METHODS
    print(surf.get(url='http://httpbin.org/get')) # Read page
    print(surf.get(url='http://httpbin.org/get', json=True)) # Read json
    print(surf.get(url='http://httpbin.org/basic-auth/test/test1123', auth=('test', 'test1123'), json=True))
    # POST METHODS
    print(surf.post(
        url='http://httpbin.org/post',
        header={'api_key': 'special-key'},
        data={
            "id": 0x78f1935,
            "username": "codewars",
        },
        json=True
        ))
    ```

## Scraper

    Example
    ```
    from codewars.scraper import Scraper
    scraper = Scraper(debug=True)
    scraper.hrefs(url = 'https://codewars.nl/space')
    ```

---
#### Refer for detailed documentation to [here](https://codewars.nl/static/docs/index.html)

[![GitHub](https://codewars.nl/static/img/github.png)](https://github.com/0x78f1935/codewars)