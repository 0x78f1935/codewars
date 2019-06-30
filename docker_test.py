import codewars # Check for dependencies
## Test WIFI
# from codewars.wifi import Wifi
# wifi = Wifi("eth0")
# sniff_results = wifi.sniff(totalResults=10)
# print(sniff_results)
# info_results = wifi.info(sniff_results)
# print(info_results)
# # wifi.sniff_forever(duration=300)
# # ssid_san = wifi.sniff_ssid(forever=False)
# # print(ssid_san)

# # Test BLUETOOTH
# from codewars.bluetooth import Bluetooth
# try:
#     bt = Bluetooth()  # Initialize the class, Scans once
#     scan_results1 = bt.scan()  # Scan area for the default 10 seconds
#     # scan_results2 = bt.run_until_discovered()  # Scan until a device is found
#     print("Scan results1: {}".format(scan_results1))
#     # print("Scan results2: {}".format(scan_results2))
# except OSError:
#     pass

# # # Test LOGGER
# from codewars.logger import Logger
# logger = Logger(appname="test", mode="DEBUG", write=False)
# logger._testLoggerClass()

# # # Test SURF
# from codewars.surf import Surfer
# from asyncio import get_event_loop
# surf = Surfer(loop=get_event_loop())
# # GET METHODS
# data = surf.get(url='https://codewars.nl/static/docs/index.html') # Read page
# print(surf.get(url='http://httpbin.org/get', json=True)) # Read json
# print(surf.get(url='http://httpbin.org/basic-auth/test/test1123', auth=('test', 'test1123'), json=True))
# # POST METHODS
# print(surf.post(
#     url='http://httpbin.org/post',
#     header={'api_key': 'special-key'},
#     data={
#         "id": 0x78f1935,
#         "username": "codewars",
#     },
#     json=True
#     ))

# from codewars.scraper import Scraper
# scraper = Scraper(debug=True)
# print(scraper.hrefs(data[1].decode()))

from codewars.unittest import Test
print(Test().run())

