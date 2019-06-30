name = "codewars"
__created_by__ = "codewars.nl"

from pip._internal import main

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        main(['install', package])
        
packages = [
    'aiohttp',
    'beautifulsoup4',
    'ipython',
    'lxml',
    'PyBluez',
    'scapy[basic]'
]
for item in packages: import_or_install(item)