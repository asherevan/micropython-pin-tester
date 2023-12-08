# micropython-pin-tester

A simple micropython program for finding the correct pins on your micropython board if they are incorrectly or not-at-all labeled.

Tested on ESP8266 only, but should work on any other board too.

If you want to directly download it to your board if it is internet enabled:
```python
import mip
mip.install('github:asherevan/micropython-pin-tester/test_pins.py')
```
It will be downloaded to /lib on your device's filesystem
