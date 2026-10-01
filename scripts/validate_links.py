"""Validate local Markdown/HTML links; use --vault for Obsidian wikilinks."""

import argparse
from pathlib import Path
from _validation import finish, link_errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--vault", action="store_true")
    args = parser.parse_args()
    if not args.root.is_dir():
        return finish(["root directory does not exist"], "local links")
    return finish(link_errors(args.root.resolve(), wiki=args.vault), "local links")


if __name__ == "__main__":
    raise SystemExit(main())
