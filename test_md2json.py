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


def test_header_without_description_with_attributes():
    header = {"test-header": {
        "attributes": [
            {"Byte": '0', "Length": '4', "Desc": "Signature"},
            {"Byte": '4', "Length": '4', "Desc": "Version"},
            {"Byte": '8', "Length": '4', "Desc": "File size"}
        ]}}
    string_to_render = '''
# test-header

Byte | Length | Desc
-----|--------|------------
0    | 4      | Signature
4    | 4      | Version
8    | 4      | File size
'''

    renderer = md2json.JsonRenderer()
    markdown = mistune.Markdown(renderer=renderer)

    markdown(string_to_render)
    assert json.loads(renderer()) == header
