import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "setlist-card"
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "two_songs.json"

# Columns are 1-based, as in SPEC.md. Spaces are written out so the card
# text cannot lose its padding.
SONG1_LINE1 = (
    "01 "
    "Neon Mercy on the Late Train Hom"
    "F#m7a"
    "  98 "
    + (" " * 27)
)
SONG1_LINE2 = (
    "  count the pickup then hold the chorus through the last turnaround and "
)
SONG2_LINE1 = (
    "02 "
    "City Nights"
    + (" " * 21)
    + "G    "
    " 120 "
    "capo 2"
    + (" " * 21)
)
SONG2_LINE2 = "  "

EXPECTED = (
    SONG1_LINE1
    + "\n"
    + SONG1_LINE2
    + "\n\n"
    + SONG2_LINE1
    + "\n"
    + SONG2_LINE2
    + "\n"
)


class SetlistCardTest(unittest.TestCase):
    def test_two_song_fixture_exact_text(self):
        self.assertEqual(len(SONG1_LINE1), 72)
        self.assertEqual(len(SONG2_LINE1), 72)
        self.assertLessEqual(len(SONG1_LINE2), 72)
        self.assertEqual(SONG2_LINE2, "  ")
        self.assertTrue(SONG1_LINE1[45:].strip() == "")
        self.assertTrue(SONG2_LINE1[45:].startswith("capo 2"))
        self.assertNotIn("Tonight", SONG1_LINE1)

        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(FIXTURE)],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, EXPECTED)
        self.assertTrue(result.stdout.endswith("\n"))
        self.assertFalse(result.stdout.endswith("\n\n"))


if __name__ == "__main__":
    unittest.main()
