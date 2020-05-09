from pychord import ChordProgression


def chord_transpose(chords, step):
    """Function that tranposes the chords by specified step amount

    Args:
        chords (list): List of chords to transpose
        step (int): The number of steps to transpose up (positive integer) or down (negative integer)

    Returns:
        list: tuple containing list of original chords and list of transposed chords
    """
    original_chords = ChordProgression(chords)
    transposed_chords = ChordProgression(chords)
    transposed_chords.transpose(step)
    return original_chords, transposed_chords


def pretty_print(step, original_chords, transposed_chords):
    """Function that outputs input and results of transposing the chords

    Args:
        step (int): The steps to transpose up or down
        original_chords (list): The list of original chords
        transposed_chords (list): The list of transposed chords

    Returns:
        None
    """
    print("\n\n****************************")
    print("***** Chord Transposer *****")
    print("****************************\n")
    print("Steps: {steps}\n".format(steps=step))
    print("Original Chords: \t {chords}\n".format(chords=original_chords))
    print("Transposed Chords: \t {chords}\n\n".format(chords=transposed_chords))
