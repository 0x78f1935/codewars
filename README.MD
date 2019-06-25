[![Codewars.nl](https://codewars.nl/static/img/logo.png)](https://codewars.nl/)

Make sure the dependencies are installed before using

`sudo apt-get install libbluetooth-dev`

# Install latest version (stable)

    pip install codewars

# Install development version (unstable)

    pip install git+https://github.com/Annihilator708/codewars@master

# Info

    More to come...

# Logger

    Example:
    ```
    from codewars.logger import Logger
    logger = Logger(appname="test", mode="DEBUG", write=False)
    logger._testLoggerClass()
    ```

Note
----
The whole module makes use of the logger.

# BlueTooth

    Example:
    ```
    from codewars.bluetooth import Bluetooth
    bt = Bluetooth()  # Initialize the class, Scans once
    scan_results1 = bt.scan()  # Scan area for the default 10 seconds
    scan_results2 = bt.run_until_discovered()  # Scan until a device is found
    print("Scan results1: {}".format(scan_results1))
    print("Scan results2: {}".format(scan_results2))
    ```
Refer to docstrings for more detailed documentation