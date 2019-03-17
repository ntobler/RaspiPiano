import RPi.GPIO as GPIO
import time
import fluidsynth


pinDict = {
    3 : 60
}

_fs = 'baah' 

def main():
    print('hello world')
    _fs = initFluidsynth()
    initPins(_fs)

    print('fs is', _fs)

    while True:
        time.sleep(10)

    #for i in range(4):
    #    on()
    #    time.sleep(1)
    #    off()
    #    time.sleep(1)
#
    #GPIO.cleanup()

def initPins(_fs):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(3, GPIO.FALLING, callback=lambda pin: buttonCallback(pin, _fs), bouncetime=10)

def initFluidsynth():
    print('init fluidsynth')
    fs = fluidsynth.Synth()
    fs.start('alsa')
    sfid = fs.sfload('/usr/share/sounds/sf2/FluidR3_GM.sf2')
    fs.program_select(0, sfid, 0, 0)
    print('fluidsynth initialized')
    return fs

def on():
    print('on')
    GPIO.output(2, GPIO.HIGH)

def off():
    print('off')
    GPIO.output(2, GPIO.LOW)




def buttonCallback(pin, _fs):
    #print('button pressed arg is', pinDict[pin])
    _fs.noteon(0, pinDict[pin], 50)



def foo():
    print("foo printet")


if __name__ == '__main__':
    main()
