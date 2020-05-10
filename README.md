# chord-manager-cli
 command line tools for simplifying music chords

### Installing

To perform an install within a virtual enviroment:

```
python -m venv .venv
.venv\bin\activate.bat
pip install -r requirements.txt
```

## Running the tests

```
pip install pytest
pytest
```

## Deployment

```bash
python setup.py sdist
pip install dist\chord_manager_cli-0.3.tar.gz
```

## Usage

```bash
$ cm
Usage: cm [-h] COMMAND {transpose,testing} [ARGS] ...

Positional Arguments:
  {transpose,testing}  Chord manager options
    transpose          transpose chords up or down specified number of steps
    testing            testing example help

Options:
  -h, --help           Show this help message and exit
```

```bash
$ cm transpose
Usage: cm transpose [-h] -c [CHORDS [CHORDS ...]] -s STEP

Options:
  -h, --help                Show this help message and exit
  -c [CHORDS [CHORDS ...]], --chords [CHORDS [CHORDS ...]]
                        The chords that need to be transposed
  -s STEP, --step STEP  The integer number of steps up or down to transpose
```

```bash
$ cm transpose
Usage: cm testing [-h] -t TESTING

Options:
  -h, --help                  Show this help message and exit
  -t TEST, --testing TESTING  example testing flag
```
