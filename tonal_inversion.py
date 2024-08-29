import re

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

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

modes = [
    "major",
    "dorian",
    "phrygian",
    "lydian",
    "mixolydian",
    "minor",
    "locrian",
]

scales = {
    "whole-tone": [0, 2, 4, 6, 8, 10],
    "acoustic scale": [0, 2, 4, 6, 7, 9, 10],
    "lydian dominant": [0, 2, 4, 6, 7, 9, 10],
    # Changed 9 to 8 (G# instead of Ab, shrug emoji)
    "algerian": [0, 2, 3, 6, 7, 8, 11, 12, 14, 15, 17],
    # Testing custom pitch sets.
    "custom": [0, 2, 4, 5, 7, 9, 10, 11]
}

def get_scale():
    root = re.findall(pattern, input("Root: "))[0]

    scale = input("Scale/mode: ").lower().strip()

    if scale == "aeolian":
        scale = "minor"

    elif scale == "ionian":
        scale = "major"

    if scale in modes:
        scale_mode_idx = modes.index(scale)
        tonality = [n for n in major_keys if root == n[scale_mode_idx]]
        tonality = tonality[0]
        rotated_tonality = tonality[scale_mode_idx:] + tonality[:scale_mode_idx]
        print(f"Chosen tonality: {", ".join(map(str, rotated_tonality))}")
        inversion_axis = get_inversion_axis()
        axis_idx = rotated_tonality.index(inversion_axis)
        rotated_to_axis = rotated_tonality[axis_idx:] + rotated_tonality[:axis_idx]

# TODO: For my "skeletons", rotated_to_root also needs to be transposed 
# to the relevant strings in cases of multiple string groupings.
# Two tonality variables may be necessary and then require concatenation.
    else:
        if scale_set := scales.get(scale):
            root_idx = notes.index(root)
            rotated_to_root = notes[root_idx:] + notes[:root_idx]
            tonality = [rotated_to_root[i % 12] for i in scale_set]
            print(f"Chosen tonality: {", ".join(tonality)}")
            inversion_axis = get_inversion_axis()
            axis_idx = tonality.index(inversion_axis)
            rotated_to_axis = tonality[axis_idx:] + tonality[:axis_idx]

    notes_in = re.findall(pattern, input("Chord/notes: "))

    return rotated_to_axis, notes_in


def get_inversion_axis():
    inversion_axis = re.findall(pattern, input("Axis: "))[0]
    return inversion_axis


def tonal_inversion(rotated_to_axis, notes_in):

    inversion = []

    # Invert the notes
    for note in notes_in:
        note_idx = rotated_to_axis.index(note)
        inversion.append(rotated_to_axis[-note_idx])

    return inversion


print(f"{", ".join(map(str, tonal_inversion(*get_scale())))}")
