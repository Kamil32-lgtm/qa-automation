from midiutil import MIDIFile

midi = MIDIFile(1)
midi.addTempo(0, 0, 120)

KICK = 36
SNARE = 38
HIHAT = 42

# 4 такта = 16 четвертей
# Kick на 1 и 3 (0, 2, 4, 6, 8, 10, 12, 14)
for i in range(0, 16, 2):
    midi.addNote(0, 9, KICK, i, 0.5, 100)

# Snare на 2 и 4 (1, 3, 5, 7, 9, 11, 13, 15)
for i in range(1, 16, 2):
    midi.addNote(0, 9, SNARE, i, 0.5, 90)

# Hi-hat на каждую восьмую (0, 0.5, 1, 1.5, ...)
t = 0
while t < 16:
    midi.addNote(0, 9, HIHAT, t, 0.25, 70)
    t = t + 0.5

with open("music/drums.mid", "wb") as f:
    midi.writeFile(f)

print("Создан music/drums.mid")