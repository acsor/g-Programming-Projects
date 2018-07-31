#!/usr/bin/env python3

import re
import sys

from os import access, R_OK


"""
The .png image was converted to text and stored to the README.md file by means
of an OCR software. To tackle any possible problems and convert automatically
the output of the OCR to the one required by the README.md file this script
was set up. It checks whether any numbered element is missing and does an
automatic conversion to the <ol>-styled list.
"""


class MarkdownFormatter:
    """
    Reads a textual file containing numbered problem assignments in the
    line format "<problem_no> <problem_description>" and converts it to a
    format suitable for Markdown.
    """

    LINE = re.compile("^(\d{1,4})\s(.+?)$", re.S | re.M)

    def __init__(self, filename):
        if not access(filename, R_OK):
            raise ValueError(
                "File \"%s\" does not exist or is not readable" % filename
            )
        self.filename = filename

    def format(self, outfile):
        """
        Converted the agreed-upon format to the format to be stored in the
        README.md format.
        """
        with open(self.filename, "r") as infile:
            text = infile.read(-1)

        matches = self.LINE.findall(text)

        outfile.write("<ol>\n")

        for m in matches:
            outfile.write("<li> %s\n" % m[1])

        outfile.write("</ol>\n")

    def missing_numpoints(self):
        """
        Returns any eventually missing numbered point in the raw text
        format.
        """
        with open(self.filename, "r") as infile:
            text = infile.read(-1)

        matches = self.LINE.findall(text)
        lower, upper = int(matches[0][0]), int(matches[-1][0])
        existing_points = {int(i[0]) for i in matches}

        if lower >= upper:
            raise ValueError(
                "Minimum and maximum points are in invalid relation: %d >= %d"
                % (lower, upper)
            )

        whole_points = set(range(lower, upper + 1))

        return whole_points - existing_points


def main():
    m = MarkdownFormatter("textual_list")
    missing_points = sorted(m.missing_numpoints())

    print("Missing numbered points = ", end="")

    if missing_points:
        print(*missing_points, sep=", ")
    else:
        print("None")

    m.format(sys.stdout)


if __name__ == "__main__":
    main()
