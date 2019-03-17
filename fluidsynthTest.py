import time
import fluidsynth

def main():
    print('hello world')
    play()

# works
def play():
    fs = fluidsynth.Synth()
    fs.start('alsa')
    sfid = fs.sfload("/usr/share/sounds/sf2/FluidR3_GM.sf2")
    fs.program_select(0, sfid, 0, 0)

    for i in range(20):
        print('playing note')
        fs.noteon(0,60, 50)
        fs.noteon(0,67, 50)
        fs.noteon(0,76, 50)
        time.sleep(1.0)
        fs.noteoff(0,60)
        fs.noteoff(0,67)
        fs.noteoff(0,66)
        time.sleep(1.0)

if __name__ == '__main__':
    main()
