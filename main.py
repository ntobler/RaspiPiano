import RPi.GPIO as GPIO
import time
import fluidsynth


pinDict = {
    3 : 60
}

_fs = None 
_audio_driver = "alsa"
#_audio_driver = "jack"

def main():
    print('hello world')
    _fs = initFluidsynth()
    initPins(_fs)

    while True:
        time.sleep(2)
        GPIO.output(2, GPIO.LOW)

    GPIO.cleanup()

def testGpio():

    for i in range(4):
        on()
        time.sleep(1)
        off()
        time.sleep(1)

    GPIO.cleanup()

def initPins(_fs):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(3, GPIO.FALLING, callback=lambda pin: buttonCallback(pin, _fs), bouncetime=10)

def initFluidsynth():
    print('init fluidsynth')
    fs = fluidsynth.Synth(samplerate = 48000, gain = 0.8)

    #fs.setting(audio.period.size: 64)

    fs.start(_audio_driver)
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
    #print('button pressed arg is', pinDict[pin]
    _fs.noteon(0, pinDict[pin], 50)
    GPIO.output(2, GPIO.HIGH)

def testSound():
  
    _fs = initFluidsynth() 

    for i in range(4):
        print('note on')
        _fs.noteon(0, 60, 50)
        time.sleep(1)
        _fs.noteoff(0, 60)
        time.sleep(1)

if __name__ == '__main__':
    main()
    #testSound()

