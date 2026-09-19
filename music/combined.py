import random
from midiutil import MIDIFile

midi = MIDIFile(2)              # 2 трека
midi.addTempo(0, 0, 120)
midi.addTempo(1, 0, 120)

# Трек 1: три ноты (C-E-G)
midi.addNote(0, 0, 60, 0, 1, 100)
midi.addNote(0, 0, 64, 1, 1, 100)
midi.addNote(0, 0, 67, 2, 1, 100)

# Трек 2: случайная мелодия из 8 нот
notes = [60, 62, 64, 65, 67, 69, 71, 72]
for i in range(8):
    note = random.choice(notes)
    midi.addNote(1, 1, note, i, 1, 100)

with open("music/combined.mid", "wb") as f:
    midi.writeFile(f)

print("Создан music/combined.mid")