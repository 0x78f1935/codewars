[![Codewars.nl](https://codewars.nl/static/img/logo.png)](https://codewars.nl/)

Make sure the dependencies are installed before using

`sudo apt-get install libbluetooth-dev`

# Install

    pip install codewars

# Info

    More to come...

# BlueTooth

    Example:
    ```
    from codewars.bluetooth import Bluetooth
    bt = Bluetooth() # Initialize the class, Scans once
    scan_results = bt.scan()  # Scan and overwrite history of scans
    print(scan_results)
    ```
Refer to docstrings for more detailed documentation