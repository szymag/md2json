import json

import mistune

import md2json

def test_header_only():
    header = {'test-header': None}
    string_to_render = '# test-header'

    renderer = md2json.JsonRenderer()
    markdown = mistune.Markdown(renderer=renderer)

    markdown(string_to_render)
    assert json.loads(renderer()) == header
