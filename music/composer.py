import random
from midiutil import MIDIFile

# Ноты
KICK = 36
SNARE = 38
HIHAT = 42

# Прогрессия C - G - Am - F
CHORDS = [
    [60, 64, 67],   # C
    [67, 71, 74],   # G
    [69, 72, 76],   # Am
    [65, 69, 72],   # F
]
BASS = [36, 43, 45, 41]           # корневые на октаву ниже
SCALE = [60, 62, 64, 65, 67, 69, 71, 72]   # C major

# Создаём MIDI с 4 треками
midi = MIDIFile(4)

# --- Трек 0: барабаны (канал 9 = барабаны) ---
midi.addTempo(0, 0, 120)
for i in range(0, 16, 2):
    midi.addNote(0, 9, KICK, i, 0.5, 100)
for i in range(1, 16, 2):
    midi.addNote(0, 9, SNARE, i, 0.5, 90)
t = 0
while t < 16:
    midi.addNote(0, 9, HIHAT, t, 0.25, 70)
    t = t + 0.5

# --- Трек 1: аккорды ---
midi.addTempo(1, 0, 120)
for i, chord in enumerate(CHORDS):
    for note in chord:
        midi.addNote(1, 0, note, i * 4, 4, 80)

# --- Трек 2: бас ---
midi.addTempo(2, 0, 120)
for i, note in enumerate(BASS):
    midi.addNote(2, 0, note, i * 4, 4, 110)

# --- Трек 3: мелодия ---
midi.addTempo(3, 0, 120)
for i in range(16):
    note = random.choice(SCALE)
    midi.addNote(3, 0, note, i, 1, 90)

with open("music/track.mid", "wb") as f:
    midi.writeFile(f)

print("Создан music/track.mid")