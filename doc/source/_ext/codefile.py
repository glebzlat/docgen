from sphinx.util.docutils import SphinxDirective
from sphinx.util import logging, parselinenos

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.nodes import Element

from pathlib import Path
from math import inf

import re

logger = logging.getLogger(__name__)


class FileReader(object):
    """
    FileReader reads given file and stores lines. It takes tag string and
    two nonnegative integers: begin and end.

    If the file is not found, exception FileNotFoundError will be raised.

    If tag string is not given, then it counts lines from the start of a file,
    stores and returs lines that are in the range [begin, end). If end is not
    given, then it reads lines to the end of a file. If begin is not given, it
    reads lines from the file start.

    If tag string is given, it returns lines from `<<{tag}>>` to `<</tag>>`
    without starting and ending tags. Tag line (tag-like line) must be the
    single comment line and tag must be right after the comment symbol:

        // <<{tag}>>

    Tag must contain only characters that can be matched with `(-|\\w)` regex.

    Every opening tag must have its closing tag:

        // <</{tag}>>

    Tag-like line is a line that contains valid tag, either opening or closing.

    If tag string, begin and end are given, then it returns lines in range
    [begin, end) within the tag scope.

    If inside the tag scope any tag-like line is occured, it will be removed
    from the output.

    If the opening tag has not its corresponding closing tag, warning will be
    raised, and file will be read from the opening tag to the file end.

    If the opening tag is not occured, no lines will be returned and warning
    will be raised.
    """

    def __init__(self, filepath: str, commentstart: str, tag: str = None,
                 lbegin: int = 0, lend: int = None):

        if tag:
            self._starttag = f"<<{tag}>>"
            self._endtag = f"<</{tag}>>"
            self._tag = False
        else:
            self._starttag = None
            self._tag = None

        self._comment = re.compile(fr'\s*{commentstart}\s*<</?(-|\w)+>>')
        self._begin = lbegin
        self._end = lend or inf
        self._file = Path(filepath).absolute()

    def read(self):
        if not self._file.exists():
            raise FileNotFoundError(f"File {self._file} not found")

        self._lines = []
        self._line_count = 0
        with open(self._file) as file:
            for line in file:
                self._add_line(line)
        if self._tag:
            logger.warning(f"Unmatched opening tag {self._starttag} in file "
                           f"{self._file}")
        return ''.join(self._lines), self._line_count

    def _add_line(self, line: str):
        if self._starttag:
            if self._starttag in line:
                self._tag = True
                return
            elif self._endtag in line:
                if not self._tag:
                    logger.warning(f"Unmatched closing tag {self._endtag} in "
                                   f"file {self._file}")
                self._tag = False
                return
            if self._tag:
                self._line_count += 1
        else:
            self._line_count += 1
        if self._tag is not None and not self._tag:
            return
        if self._comment.match(line):
            return
        if self._line_count >= self._begin and self._line_count < self._end:
            self._lines.append(line)


class IncludeFile(SphinxDirective):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    option_spec = {
        'lang': directives.unchanged,
        'tag': directives.unchanged,
        'begin': directives.nonnegative_int,
        'end': directives.nonnegative_int,
        'emphasize': directives.unchanged
    }

    LANG_COMMENT = {
        'cpp': '//',
        'python': '#'
    }

    def run(self):
        document = self.state.document

        filename = self.arguments[0]
        lang = self.options.get('land', None) \
            or self.env.temp_data.get('highlight_language',
                                      self.config.highlight_language)
        tag = self.options.get('tag', None)
        begin = self.options.get('begin', 0)
        end = self.options.get('end', None)

        comment = self.LANG_COMMENT.get(lang)
        if not comment:
            comment = self.LANG_COMMENT['cpp']

        try:
            freader = FileReader(filename, comment, tag, begin, end)
            content, lines = freader.read()

            literal: Element = nodes.literal_block(content, content,
                                                   source=filename)

            if 'emphasize' in self.options:
                hl_lines = parselinenos(self.options['emphasize'], lines)
                if any(i >= lines for i in hl_lines):
                    logger.warning("Emphasize line spec is out of range "
                                   f"{lines}: {self.options['emphasize']}")
                extra_args = literal['highlight_args'] = {}
                extra_args['hl_lines'] = [x + 1 for x in hl_lines if x < lines]
        except FileNotFoundError as e:
            return [document.reporter.warning(e, line=self.lineno)]

        literal['language'] = lang
        self.add_name(literal)
        return [literal]


def setup(app):
    app.add_directive('includefile', IncludeFile)
    return {
        'version': '0.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
