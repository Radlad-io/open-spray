import machine
import time

speaker = machine.PWM(machine.Pin(0))
speaker.duty_u16(0)
notes = {
    "A4": 220,
    "A#4": 233,
    "B4": 247,
    "C4": 261,
    "C#4": 277,
    "D4": 294,
    "D4#": 311,
    "E4": 330,
    "F4": 349,
    "F#4": 370,
    "G4": 392,
    "G#4": 415,
    "C5": 523
    }

class Sound:
    
    def __init__(self):
        self.duty = int(65535/2)
        self.muted = False
    
    def play_note(self, note, duration):
        if self.muted == False:
            frequency = notes[note]
            speaker.duty_u16(self.duty)
            speaker.freq(frequency)
            time.sleep(duration)
            speaker.duty_u16(0)
    
    def play_knob_change(self):
        self.play_note("C4", 1/100)
        
    def play_intro(self):
        self.play_note("G4", 1/8)
        time.sleep(3/8)
        self.play_note("G4", 1/8)
        self.play_note("E4", 1/8)
        self.play_note("D4", 1/8)
        self.play_note("C4", 1/4)
        time.sleep(2/8)
        self.play_note("C5", 1/8)

