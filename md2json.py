from enum import Enum
import json
import sys

import mistune

class State(Enum):
    INIT = 0
    INFO = 1
    HEADER = 2
    KEYS = 3
    ATTRIBUTES = 4

class JsonRenderer(mistune.Renderer):
    def __init__(self):
        super().__init__()
        self.description = []
        self.item_name = None
        self.document = {}

    def __call__(self):
        return json.dumps(self.document)

    def block_code(self, code, language=None):
        return ""
    def block_quote(self, text):
        return ""
    def block_html(self, html):
        return ""
    def header(self, text, level, raw=None):
        self.item_name = text
        self.document = {self.item_name: None}
        return json.dumps(text)
    def hrule(self):
        return ""
    def list(self, body, ordered=True):
        return ""
    def list_item(self, text):
        return ""
    def paragraph(self, text):
        return text
    def table(self, header, body):
        return ""
    def table_row(self, content):
        return ""
    def table_cell(self, content, **flags):
        return ""
    def autolink(self, link, is_email=False):
        return ""
    def codespan(self, text):
        return ""
    def double_emphasis(self, text):
        return ""
    def emphasis(self, text):
        return ""
    def image(self, src, title, alt_text):
        return ""
    def linebreak(self):
        return ""
    def newline(self):
        return ""
    def link(self, link, title, content):
        return ""
    def strikethrough(self, text):
        return ""
    def text(self, text):
        return text
    def inline_html(self, text):
        return ""
    def footnote_ref(self, key, index):
        return ""
    def footnote_item(self, key, text):
        return ""
    def footnotes(self, text):
        return ""

if __name__ == '__main__':
    if len(sys.argv) > 1:
        inf = sys.argv[1]
        renderer = JsonRenderer()
        markdown = mistune.Markdown(renderer=renderer)
        with open(inf, 'r') as f:
            s = f.read()
            print(markdown(s))
