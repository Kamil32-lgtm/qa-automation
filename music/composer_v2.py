import random
import argparse
from midiutil import MIDIFile

# --- Аргументы командной строки ---
parser = argparse.ArgumentParser(description="Генератор MIDI-треков")
parser.add_argument("--tempo", type=int, default=120, help="Темп (BPM)")
parser.add_argument("--bars", type=int, default=4, help="Сколько тактов")
parser.add_argument("--output", default="music/track_v2.mid", help="Куда сохранить")
args = parser.parse_args()

# --- Ноты ---
KICK = 36
SNARE = 38
HIHAT = 42

CHORDS = [
    [60, 64, 67],
    [67, 71, 74],
    [69, 72, 76],
    [65, 69, 72],
]
BASS = [36, 43, 45, 41]
SCALE = [60, 62, 64, 65, 67, 69, 71, 72]

midi = MIDIFile(4)

# --- Барабаны ---
midi.addTempo(0, 0, args.tempo)
for i in range(0, args.bars * 4, 2):
    midi.addNote(0, 9, KICK, i, 0.5, 100)
for i in range(1, args.bars * 4, 2):
    midi.addNote(0, 9, SNARE, i, 0.5, 90)
t = 0
while t < args.bars * 4:
    midi.addNote(0, 9, HIHAT, t, 0.25, 70)
    t = t + 0.5

# --- Аккорды ---
midi.addTempo(1, 0, args.tempo)
for i in range(args.bars):
    chord = CHORDS[i % 4]
    for note in chord:
        midi.addNote(1, 0, note, i * 4, 4, 80)

# --- Бас ---
midi.addTempo(2, 0, args.tempo)
for i in range(args.bars):
    note = BASS[i % 4]
    midi.addNote(2, 0, note, i * 4, 4, 110)

# --- Мелодия ---
midi.addTempo(3, 0, args.tempo)
for i in range(args.bars * 4):
    note = random.choice(SCALE)
    midi.addNote(3, 0, note, i, 1, 90)

# --- Сохранение ---
with open(args.output, "wb") as f:
    midi.writeFile(f)

print(f"Создан {args.output}")
print(f"Темп: {args.tempo} BPM, тактов: {args.bars}")