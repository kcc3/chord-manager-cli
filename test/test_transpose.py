from pychord import ChordProgression
from chord_manager_cli.chord_manager import chord_transpose
import pytest


@pytest.mark.parametrize("test_chord_transpose_original, expected", [
    (["E", "B", "G#", "F#"], ChordProgression(["E", "B", "G#", "F#"])),
    (["C", "D", "E", "F", "G"], ChordProgression(["C", "D", "E", "F", "G"])),
    (["Bb", "C", "E"], ChordProgression(["Bb", "C", "E"])),
    (["C#", "E", "F#"], ChordProgression(["C#", "E", "F#"]))
])
def test_chord_transpose_original(test_chord_transpose_original, expected):
    step = 3
    o, t = chord_transpose(test_chord_transpose_original, step)
    assert o == expected


@pytest.mark.parametrize("test_chord_transposed, expected", [
    (["E", "B", "G#", "F#"], ChordProgression(["G", "D", "B", "A"])),
    (["C", "D", "E", "F", "G"], ChordProgression(["Eb", "F", "G", "Ab", "Bb"])),
    (["Bb", "C", "E"], ChordProgression(["Db", "Eb", "G"])),
    (["C#", "E", "F#"], ChordProgression(["E", "G", "A"]))
])
def test_chord_transposed(test_chord_transposed, expected):
    step = 3
    o, t = chord_transpose(test_chord_transposed, step)
    assert t == expected


@pytest.mark.parametrize("test_chord_transposed_steps, expected", [
    (1, ChordProgression(["F", "C", "A", "G"])),
    (2, ChordProgression(["Gb", "Db", "Bb", "Ab"])),
    (3, ChordProgression(["G", "D", "B", "A"])),
    (4, ChordProgression(["Ab", "Eb", "C", "Bb"])),
    (5, ChordProgression(["A", "E", "Db", "B"])),
    (6, ChordProgression(["Bb", "F", "D", "C"])),
    (7, ChordProgression(["B", "Gb", "Eb", "Db"])),
    (8, ChordProgression(["C", "G", "E", "D"])),
    (9, ChordProgression(["Db", "Ab", "F", "Eb"])),
    (10, ChordProgression(["D", "A", "Gb", "E"])),
    (11, ChordProgression(["Eb", "Bb", "G", "F"])),
    (12, ChordProgression(["E", "B", "Ab", "Gb"]))
])
def test_chord_transposed_steps(test_chord_transposed_steps, expected):
    chords = ["E", "B", "G#", "F#"]
    o, t = chord_transpose(chords, test_chord_transposed_steps)
    assert t == expected