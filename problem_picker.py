#!/usr/bin/python3
import re

from os import access, R_OK
from random import randrange
from sys import argv


class ProblemReader:
    """
    ProblemReader reads all the suggested problem assignments from a
    designated file, such as README.md.
    """
    START = re.compile("\s*?<ol>")
    END = re.compile("\s*?</ol>")
    LINE = re.compile("\s*?<li>(.+)")

    def __init__(self, filename):
        if not access(filename, R_OK):
            raise ValueError("File \"%s\" is not readable" % filename)

        self.filename = filename
        
    def __iter__(self):
        return self._iterator()

    def _iterator(self):
        """
        ProblemReader scans the given file top-to-bottom. When it encounters the
        <ol> tag, it starts recording the suggested problems, stopping when it
        reaches </ol>. It handles carefully pathological cases, such as </ol>
        before <ol>, missing <ol> etc.
        """
        inside = False

        with open(self.filename, "r") as inputfile:
            for l in inputfile:
                if not inside and self.END.match(l):
                    raise ValueError(
                            "</ol> tag comes before <ol> tag in %s or <ol> is missing" %
                            self.filename
                    )
                if self.START.match(l):
                    inside = True
                    continue
                elif self.END.match(l):
                    inside = False
                    break

                if inside:
                    match = self.LINE.match(l)
                    
                    yield match.group(1)

            # We left the loop never meeting the </ol> tag
            if inside:
                print(
                    "[%s] WARNING: Ending tag </ol> never met in %s" %
                    (argv[0], self.filename)
                )


def main():
    default_filename = "README.md"
    choice = None
    filename = input("Enter source filename [defaults to %s]: " % default_filename)

    if not filename:
        filename = default_filename

    problems = list(ProblemReader(filename))
    choice = randrange(0, len(problems)) # randrange() does not include the endpoint

    print("And your assigned choice is...\n\t\t\t*** %s ***" % problems[choice])


if __name__ == "__main__":
    main()
