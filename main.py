import RPi.GPIO as GPIO
import time
import fluidsynth

class RaspiPiano:

    # This dictionary connects Raspberrypi GPIO numbers with MIDI tone keys
    # remove entries to disable keys
    pinDict = {
        3 : 60,
        4 : 61,
        5 : 62,
        6 : 63,
        7 : 64
    }

    def __init__(self, audio_driver="alsa"):
        self._fs = None 
        self._audio_driver = audio_driver

    def start(self):
        print('hello world')
        self.initFluidsynth()
        self.initPins()

        self.playScale()

        while True:
            time.sleep(2)
            GPIO.output(2, GPIO.LOW)

        GPIO.cleanup()

        return self

    def testGpio(self):

        for i in range(4):
            on()
            time.sleep(1)
            off()
            time.sleep(1)

        GPIO.cleanup()

    def initPins(self):
        GPIO.setmode(GPIO.BCM)
        for pinNr in self.pinDict.keys():
            GPIO.setup(pinNr, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
            GPIO.add_event_detect(pinNr, GPIO.FALLING, callback=lambda pin: self.buttonCallback(pin), bouncetime=10)
        GPIO.setup(2, GPIO.OUT)

    def initFluidsynth(self):
        print('init fluidsynth')
        fs = fluidsynth.Synth(samplerate = 48000, gain = 0.8)

        #fs.setting(audio.period.size: 64)

        fs.start(self._audio_driver)
        sfid = fs.sfload('/usr/share/sounds/sf2/FluidR3_GM.sf2')
        fs.program_select(0, sfid, 0, 0)
        print('fluidsynth initialized')
        self._fs = fs

    def on():
        print('on')
        GPIO.output(2, GPIO.HIGH)

    def off():
        print('off')
        GPIO.output(2, GPIO.LOW)

    def buttonCallback(self, pin):
        #print('button pressed arg is', pinDict[pin]
        self._fs.noteon(0, self.pinDict[pin], 50)
        GPIO.output(2, GPIO.HIGH)

    def testSound(self):
  
        for i in range(4):
            print('note on')
            self._fs.noteon(0, 60, 50)
            time.sleep(1)
            self._fs.noteoff(0, 60)
            time.sleep(1)

    def playScale(self):
        scale = [60, 62, 64, 65, 67, 69, 71, 72]
        for i in scale:
            self._fs.noteon(0, i, 50)
            time.sleep(0.1)


if __name__ == '__main__':
    RaspiPiano("alsa").start()

