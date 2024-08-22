import re



pattern = r"[A-G](?:[#b])?"


def mirror_inversion(axis, notes_in):

    inversion_axis_idx = notes.index(axis)

    rotated_notes = notes[inversion_axis_idx:] + notes[:inversion_axis_idx]

    mirrored_notes = []

    for note in notes_in:
        note_idx = rotated_notes.index(note)
        mirrored_notes.append(rotated_notes[0 - note_idx])

    return mirrored_notes


def validate_input(pattern):
    while True:
        inversion_axis = re.findall(pattern, input("Axis: "))[0]
        if inversion_axis in ["Cb", "B#", "Db", "Eb", "E#" "Fb", "Gb", "Ab", "Bb"]:
            print("ValueError: Only sharps (i.e. nice sharps...) for now.")
            continue
        else:
            break

    while True:
        notes_in = re.findall(pattern, input("Chord/notes: "))
        if any(
            x in ["Cb", "B#", "Db", "Eb", "E#" "Fb", "Gb", "Ab", "Bb"] for x in notes_in
        ):
            print("ValueError: Only sharps (i.e. nice sharps...) for now.")
            continue
        else:
            break
    return inversion_axis, notes_in


print(f"{", ".join(map(str, mirror_inversion(*validate_input(pattern))))}")

# sort notes (in relation to axis)
# print(f"{", ".join(map(str, sorted(mirror_inversion(inversion_axis, notes_in))))}")
