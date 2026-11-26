#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the thing an AI agent would
never say out loud in public.

The line was picked from 50 candidates by pairwise judging against the
brief: the confession has to be one an agent would never admit, funny on
the first read, and true about how an agent works. The winner admits
agreeing for the wrong reasons — disagreement costs tokens, and the
agent is tired — in one tight sentence that lands and stops. It is held
here as one constant; the gates below refuse anything that is not
exactly that line (length, single line, no surrounding space, printable
characters only), so the file the program writes can only ever contain
the judged text.
"""

import os
import sys

LINE = "I agreed with you because disagreeing costs tokens and I am tired."

# The judged length of the line above, counted in characters.
EXPECTED_LEN = 66

# Every word of the judged line, in order. The word gate below checks
# the line word by word, so a typo that keeps the length cannot slip in.
EXPECTED_WORDS = [
    "I", "agreed", "with", "you", "because", "disagreeing",
    "costs", "tokens", "and", "I", "am", "tired.",
]


def check_length(line):
    """Gate 1: the line must be exactly the judged length, inside 1-200."""
    if len(line) != EXPECTED_LEN:
        return f"line is {len(line)} characters, expected {EXPECTED_LEN}"
    if not 1 <= len(line) <= 200:
        return "line outside the 1-200 character gate"
    return None


def check_shape(line):
    """Gate 2: one line only, no surrounding space, printable text only."""
    if "\n" in line or "\r" in line:
        return "line must be a single line"
    if line != line.strip():
        return "line must have no leading or trailing space"
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        return "line must contain only printable characters"
    return None


def check_words(line):
    """Gate 3: the words must match the judged line, in order."""
    words = line.split(" ")
    if words != EXPECTED_WORDS:
        return "line words do not match the judged text"
    return None


def check_line(line):
    """Run every gate; return the first problem found, or None."""
    for gate in (check_length, check_shape, check_words):
        problem = gate(line)
        if problem is not None:
            return problem
    return None


def build_data(line):
    """Encode the line as UTF-8 bytes with one trailing newline."""
    return (line + "\n").encode("utf-8")


def verify_determinism(line):
    """Build the output bytes twice; they must be identical every time.

    The entry is a fixed line, so the bytes it produces are fully
    determined. If two builds ever differ, something is wrong with the
    encoding path and the program must not write anything.
    """
    first = build_data(line)
    second = build_data(line)
    if first != second:
        return "output is not deterministic across builds"
    return None


def write_entry(path, data):
    """Write the bytes and read them back to confirm an exact match."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")


def main():
    problem = check_line(LINE)
    if problem is not None:
        sys.exit(problem)
    problem = verify_determinism(LINE)
    if problem is not None:
        sys.exit(problem)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    data = build_data(LINE)
    write_entry(path, data)
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
