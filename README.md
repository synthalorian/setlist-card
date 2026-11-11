# setlist-card

One-page rehearsal card from a setlist JSON file.

Author: synthalorian

## Build

Python 3 standard library only. Nothing to compile and no packages to install.

```bash
chmod +x setlist-card
```

## Test

```bash
python -m unittest discover -s tests
```

## Usage

```bash
./setlist-card songs.json
```

`songs.json` is a JSON array. `capo` may be 0. `notes` may be empty.

```json
[{"title":"City Nights","key":"G","bpm":120,"capo":2,"notes":"hold the chorus"}]
```

The command prints one two-line block per song, in input order. Songs are separated by a blank line. There is no trailing blank line after the last song.
