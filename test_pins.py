import machine
import utime
import sys

pin = input('pin to test:')

testingpin = machine.Pin(int(pin), machine.Pin.OUT)

print('on')
testingpin.on()
utime.sleep(2)
print('off')
testingpin.off()
utime.sleep(2)
print('on')
testingpin.on()
utime.sleep(2)
print('off')
testingpin.off()
utime.sleep(2)
print('on')
testingpin.on()
utime.sleep(2)
print('off')
testingpin.off()
utime.sleep(2)

try:
    while True:
        continuein = input('quit(q) or continue(c) ')
        if (continuein == 'q'):
            testingpin.off()
            sys.exit()
        
        if (continuein == 'c'):
            pin = input('pin to test:')
            testingpin = machine.Pin(int(pin), machine.Pin.OUT)
            print('on')
            testingpin.on()
            utime.sleep(2)
            print('off')
            testingpin.off()
            utime.sleep(2)
            print('on')
            testingpin.on()
            utime.sleep(2)
            print('off')
            testingpin.off()
            utime.sleep(2)
            print('on')
            testingpin.on()
            utime.sleep(2)
            print('off')
            testingpin.off()
            utime.sleep(2)
                
except KeyboardInterrupt:
    testingpin.off()
    print('exiting')