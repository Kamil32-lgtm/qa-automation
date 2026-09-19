from midiutil import MIDIFile

midi = MIDIFile(1)
midi.addTempo(0, 0, 120)

# Корневые ноты аккордов C - G - Am - F, но на октаву ниже
bass_notes = [36, 43, 45, 41]
# C2=36, G2=43, A2=45, F2=41

for i, note in enumerate(bass_notes):
    midi.addNote(0, 0, note, i, 1, 110)

with open("music/bass.mid", "wb") as f:
    midi.writeFile(f)

print("Создан music/bass.mid")