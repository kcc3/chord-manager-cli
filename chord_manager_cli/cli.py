from chord_manager_cli.chord_manager import chord_transpose, pretty_print
import argparse


# Entry Point
def main():
    parser = argparse.ArgumentParser(description="This script transposes chords to different keys")
    parser.add_argument("command", choices=["transpose", "testing"], help="Call to transpose chords")
    parser.add_argument("-c", "--chords", help="The chords that need to be transposed", nargs="*", required=True)
    parser.add_argument("-s", "--step", help="The integer number of steps up or down to transpose", type=int, required=True)
    args = parser.parse_args()
    # Check for transpose
    if args.command == "transpose":
        o, c = chord_transpose(args.chords, args.step)
        pretty_print(args.step, o, c)
    elif args.command == "testing":
        print("Testing")


if __name__ == '__main__':
    main()
