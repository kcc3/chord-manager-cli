import click
from chord_manager_cli.chord_manager import chord_transpose, pretty_print


@click.group()
def cli():
    pass


@click.command(name="transpose", help="Transpose chords")
@click.option("--chords", default="", nargs="*", required=True, help="The chords to transpose")
@click.option("--step", default=1, type=int, required=True, help="show available memory")
def transpose(chords, step):
    original_chords, tranposed_chords = chord_transpose(chords, step)
    pretty_print(step, original_chords, tranposed_chords)


cli.add_command(transpose)