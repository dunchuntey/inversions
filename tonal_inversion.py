import re

major_keys = [
    ["C", "D", "E", "F", "G", "A", "B"],
    ["G", "A", "B", "C", "D", "E", "F#"],
    ["D", "E", "F#", "G", "A", "B", "C#"],
    ["A", "B", "C#", "D", "E", "F#", "G#"],
    ["E", "F#", "G#", "A", "B", "C#", "D#"],
    ["B", "C#", "D#", "E", "F#", "G#", "A#"],
    ["F#", "G#", "A#", "B", "C#", "D#", "E#"],
    ["C#", "D#", "E#", "F#", "G#", "A#", "B#"],
    ["F", "G", "A", "Bb", "C", "D", "E"],
    ["Bb", "C", "D", "Eb", "F", "G", "A"],
    ["Eb", "F", "G", "Ab", "Bb", "C", "D"],
    ["Ab", "Bb", "C", "Db", "Eb", "F", "G"],
    ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"],
    ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"],
    ["Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb"],
]

pattern = r"[A-G](?:[#b])?"

scales_modes = ["major", "dorian", "phrygian", "lydian", "mixolydian", "minor", "locrian"]


def get_scale():
    root = re.findall(pattern, input("Root: "))[0]

    scale = input("Scale/mode: ").lower().strip()
    scale_mode_idx = scales_modes.index(scale)

    if scale == "aeolian":
        scale = "minor"

    if scale == "ionian":
        scale = "major"

    inversion_axis = re.findall(pattern, input("Axis: "))[0]
    rotate_to_scale = tonality[scale_mode_idx:] + tonality[:scale_mode_idx]
    axis_idx = rotate_to_scale.index(inversion_axis)
    print(f"Chosen tonality: {tonality}")


    tonality = [notes for notes in major_keys if root == notes[scale_mode_idx]]
    tonality = tonality[0]


    notes_in = re.findall(pattern, input("Chord/notes: "))


# Rotate to start from the axis note
    rotated_to_axis = rotate_to_scale[axis_idx:] + rotate_to_scale[:axis_idx]
    
    return rotated_to_axis, notes_in


def tonal_inversion(rotated_to_axis, notes_in):

    inversion = []

    # Invert the notes
    for note in notes_in:
        note_idx = rotated_to_axis.index(note)
        inversion.append(rotated_to_axis[- note_idx])
    
    return inversion



print(f"{", ".join(map(str, tonal_inversion(get_scale())))}")

# print(f"{", ".join(map(str, sorted(tonal_inversion(key, scale, inversion_axis, notes_in))))}")

# sort notes (in relation to axis)
# print(f"{", ".join(map(str, sorted(mirror_inversion(inversion_axis, notes_in))))}")
