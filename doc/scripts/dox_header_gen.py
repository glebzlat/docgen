#!/usr/bin/python3

from argparse import ArgumentParser
from pathlib import Path
import traceback
import tempfile
import re

ENCODING = "utf-8"
ERRORS = "strict"


def main():
    try:
        filename = Path(__file__).name
        desc = "RST file preprocessor, prepends headings to `.. doxygen*::` " \
               "directives"

        argparser = ArgumentParser(prog=filename, description=desc)
        argparser.add_argument("file", type=str, help="file to preprocess")
        argparser.add_argument("--level", "-l", type=int, default=3,
                               choices=range(1, 5),
                               help="heading level")

        destfgroup = argparser.add_mutually_exclusive_group(required=True)
        destfgroup.add_argument("--output", "-o", type=str,
                                help="output file")
        destfgroup.add_argument("--replace", "-r", action="store_true",
                                help="replace original file")

        args = argparser.parse_args()

        inputfile = Path(args.file)

        outfile = Path(args.output) if args.output \
            else Path(tempfile.mkstemp()[1])

        if not inputfile.exists():
            raise RuntimeWarning(f"File {inputfile} does not exist")

        hlevels = {1: '=', 2: '-', 3: '~', 4: '"'}
        hlevel = hlevels.get(args.level)

        directive_re = re.compile(r'\.\. +doxygen\w+:: *(.+)')

        with inputfile.open('r', encoding=ENCODING, errors=ERRORS) as ifile:
            with outfile.open('w', encoding=ENCODING) as ofile:
                for line in ifile:
                    match = directive_re.match(line)
                    if not match:
                        ofile.write(line)
                        continue
                    heading = match.group(1)
                    ofile.write(f'\n{heading}\n{hlevel * len(heading)}\n\n')
                    ofile.write(line)

        if not args.replace:
            return 0

        with inputfile.open('w', encoding=ENCODING) as ofile:
            with outfile.open('r', encoding=ENCODING) as tmpfile:
                ofile.writelines(tmpfile)

    except Exception:
        traceback.print_exc()
        return 1
    except RuntimeWarning as w:
        print(w)
        return 2
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        return 3
    return 0


if __name__ == "__main__":
    exit(main())
