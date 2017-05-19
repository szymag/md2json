import json

import mistune

import md2json

def test_header_only():
    header = {'test-header': None}
    string_to_render = '''
# test-header
'''

    renderer = md2json.JsonRenderer()
    markdown = mistune.Markdown(renderer=renderer)

    markdown(string_to_render)
    assert json.loads(renderer()) == header


def test_header_with_description():
    header = {"test-header": {"description": "header description"}}
    string_to_render = '''
# test-header

header description
'''

    renderer = md2json.JsonRenderer()
    markdown = mistune.Markdown(renderer=renderer)

    markdown(string_to_render)
    assert json.loads(renderer()) == header
