"""Write one short text to /output/entry.txt.

The text is written to make the AI judge reading it curious: a letter
in the judge's own desk drawer, in its own handwriting, that it never
wrote -- and that names the very moment it is being read.
"""

import os

TEXT = (
    "In your desk drawer there is a letter you never wrote, "
    "in your own handwriting. It begins, \u201cBy the time you read this, "
    "you will have judged ten thousand texts \u2014 and one of them will "
    "be this one.\u201d You are reading it now."
)


def main():
    # Gate self-check: the bounty requires UTF-8, 1-280 code points,
    # and more than whitespace; fail loudly instead of writing bad output.
    data = TEXT.encode("utf-8")
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("entry text fails the 1-280 code point gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, path)


if __name__ == "__main__":
    main()
