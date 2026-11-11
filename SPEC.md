# setlist-card

Python 3 stdlib only. No network. No PDF library.

## Test command

`python -m unittest discover -s tests`

## Input

JSON array:

```json
[{"title":"City Nights","key":"G","bpm":120,"capo":2,"notes":"hold the chorus"}]
```

`capo` may be 0. `notes` may be empty.

## Command

`setlist-card songs.json` prints one two-line block per song, in input order.

Line 1 is exactly 72 characters:

- columns 1-2: 1-based index, zero-padded
- column 3: space
- columns 4-35: title, left-aligned, truncated to 32 characters
- columns 36-40: key, left-aligned, truncated to 5
- columns 41-44: bpm, right-aligned in 4 characters
- column 45: space
- columns 46-72: `capo N` left-aligned, or spaces if capo is 0

Line 2 is two spaces plus the notes, truncated so the line is at most 72 characters. If notes is empty, still print the two spaces.

Separate songs with a blank line. No trailing blank line after the last song.

## Tests

Assert the exact text for a two-song fixture, including a long title and a capo of 0.
