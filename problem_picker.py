#!/usr/bin/env python3

import argparse
import re
import sys

from os import access, R_OK
from random import randrange
from sys import argv


"""
Script designed to pick up a random problem for the undecided developer.
"""


class ProblemReader:
    """
    ProblemReader reads all the suggested problem assignments from a
    designated file, such as README.md.
    """
    START = re.compile("\s*?<ol>")
    END = re.compile("\s*?</ol>")
    LINE = re.compile("\s*?<li>\s?(.+)")

    def __init__(self, filename):
        if not access(filename, R_OK):
            raise ValueError(
                "File \"%s\" does not exist or is not readable" % filename
            )

        self.filename = filename

    def __iter__(self):
        return self._iterator()

    def _iterator(self):
        """
        ProblemReader scans the given file top-to-bottom. When it encounters
        the <ol> tag, it starts recording the suggested problems, stopping
        when it reaches </ol>. It handles carefully pathological cases, such
        as </ol> before <ol>, missing <ol> etc.
        """
        inside = False

        with open(self.filename, "r") as inputfile:
            for l in inputfile:
                if not inside and self.END.match(l):
                    raise ValueError(
                        "</ol> tag comes before <ol> tag in %s or <ol> is "
                        "missing" % self.filename
                    )
                if self.START.match(l):
                    inside = True
                    continue
                elif self.END.match(l):
                    inside = False
                    break

                if inside:
                    match = self.LINE.match(l)

                    if match:
                        yield match.group(1)

            # We left the loop never meeting the </ol> tag
            if inside:
                print(
                    "[%s] WARNING: Ending tag </ol> never met in %s" %
                    (argv[0], self.filename), file=sys.stderr
                )


def main():
    parser = argparse.ArgumentParser(description="Choose a suggested problem")
    parser.add_argument(
        "--src", action="store", type=str,
        dest="source_filename", metavar="<filename>", default="README.md",
        help="Source file name where to extract problem tracks from "
        "(Markdown format)."
    )
    args = parser.parse_args()

    try:
        p = ProblemReader(args.source_filename)
    except ValueError:
        print(
            "No file named %s exists or is readable" %
            args.source_filename, file=sys.stderr
        )
        exit(1)
    problems = tuple(p)
    # randrange() does not include the endpoint
    choice = randrange(0, len(problems))

    print("And your assigned choice is...\n\t\t\t*** %s ***"
          % problems[choice])


if __name__ == "__main__":
    main()
