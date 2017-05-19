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
        self.property_name = None
        self.value_list = []
        self.row_items = []
        self.headers = []
        self.is_header = True
        self.state = State.INIT
        self.keys = []
        self.buffer = []
        self.item_name = None
        self.item = None
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
        print("header: {}".format(text))
        print(self.buffer)
        # self.item_name = ''.join(self.buffer)
        # self.buffer.clear()
        # self.state = State.HEADER
        # name = self.property_name
        # self.property_name = text
        # if name is not None:
        #     return "{{{name}:{items}}}".format(
        #         name=name, items=json.dumps(self.value_list))
        self.document = {text: None}
        return json.dumps(text)
    def hrule(self):
        return ""
    def list(self, body, ordered=True):
        return ""
    def list_item(self, text):
        return ""
    def paragraph(self, text):
        print("paragraph:{}".format(text))
        return text
    def table(self, header, body):
        self.is_header = True
        # print("table")
        # return ""
        # print(self.headers)
        return "header: {}\nbody: {}".format(header, body)
    def table_row(self, content):
        # print("table_row")
        # return content
        print("headers: {}".format(self.headers))
        self.keys = list(self.headers)
        self.is_header = False
        self.headers.clear()
        return "row: {}".format(content)
    def table_cell(self, content, **flags):
        print("table_cell")
        if self.is_header:
            self.headers.append(content)
        return "cell: {}".format(content)
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
        print("text: {}".format(text))
        self.buffer.append(text)
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
    # assert len(sys.argv) > 1
    # inf = sys.argv[1]

    renderer = JsonRenderer()
    markdown = mistune.Markdown(renderer=renderer)

    markdown('# test')
    print(renderer())

    # with open(inf, 'r') as f:
    #     s = f.read()
    #     print(markdown(s))
