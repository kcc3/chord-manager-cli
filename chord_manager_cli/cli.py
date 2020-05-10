from chord_manager_cli.chord_manager import chord_transpose, pretty_print
import argparse


def transpose(args: argparse.Namespace):
    """Transpose chords and output command line results

    Args:
        args (argparse.Namespace): argparse namespace with [chords (list), step (int)] flags passed in

    Returns:
        None: Outputs the step, original chords, and transposed chords to command line
    """
    o, c = chord_transpose(args.chords, args.step)
    pretty_print(args.step, o, c)


def test_function(args: argparse.Namespace):
    """Test Function (for testing additional subparse options

    Args:
        args (argparse.Namespace): argparse namespace with example test flag

    Returns:
        None: Outputs "Test Function"
    """
    print("Test Function")
    print(args)


def setup_parsers():
    """Setup the parser and subparsers with specified chord manager calls

    Returns:
        parser (argparse.ArgumentParser): initialized parser
    """
    parser = argparse.ArgumentParser(description="This script transposes chords to different keys")
    subparsers = parser.add_subparsers(help="chord manager options")

    # Transpose function setup
    transpose_parser = subparsers.add_parser("transpose", help="transpose chords up or down specified number of steps")
    transpose_parser.add_argument("-c", "--chords", help="The chords that need to be transposed", nargs="*", required=True)
    transpose_parser.add_argument("-s", "--step", help="The integer number of steps up or down to transpose", type=int, required=True)
    transpose_parser.set_defaults(func=transpose)

    # Test function #2 setup
    testing_parser = subparsers.add_parser("testing", help="testing example help")
    testing_parser.add_argument("-t", "--testing", required=True)
    testing_parser.set_defaults(func=test_function)
    return parser


# Entry Point
def main():
    # Setup / initialize parsers
    parser = setup_parsers()
    args = parser.parse_args()

    # Call user specified function or print out usage info
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
