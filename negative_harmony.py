import re


notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

pattern = r"[A-G](?:[#])?"


def negative_harmony(root, notes_in):

    if root in ["B#, E#"]:
        raise ValueError("Let's use nice sharps for now.")

    root_idx = notes.index(root)

    rotated_notes = notes[root_idx:] + notes[:root_idx]

    neg_chord = []

    for note in notes_in:
        note_idx = rotated_notes.index(note)
        neg_chord.append(rotated_notes[7 - note_idx])

    return neg_chord


def validate_input(pattern):
    while True:
        root_key = re.findall(pattern, input("Root key: ").upper())[0]
        if root_key in ["Cb", "B#", "Db", "Eb", "E#" "Fb", "Gb", "Ab", "Bb"]:
            print("ValueError: Only sharps (i.e. nice sharps...) for now.")
            continue
        else:
            break

    while True:
        notes_in = re.findall(pattern, input("Chord/notes: ").upper())
        if any(
            x in ["Cb", "B#", "Db", "Eb", "E#" "Fb", "Gb", "Ab", "Bb"] for x in notes_in
        ):
            print("ValueError: Only sharps (i.e. nice sharps...) for now.")
            continue
        else:
            break
    return root_key, notes_in


print(f"{", ".join(map(str, negative_harmony(*validate_input(pattern))))}")
