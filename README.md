# md2json [![Build Status](https://travis-ci.org/hryniuk/md2json.svg?branch=master)](https://travis-ci.org/hryniuk/md2json)

Markdown to JSON converter for documentation files.

It's mostly created to convert [d2s-format](https://github.com/krisives/d2s-format)'s
`README.md` to a JSON document that can be then used to parse a binary `.d2s`
file, which then can help you set desired attributes of your Diablo 2 character.

## Example

`md2json` converts this markdown document:

```markdown
# object 1

description of object1's structure

attr 1 | attr 2 | name
-------|--------|------------
a      |    1   | field 1
b      |    2   | [field 2](#field-2)
c      |    3   | field 3

## field 2

description of field 2's structure

value  | name
-------|-------
123    | fx
456    | fy
789    | fz
```

to this JSON:

```json
{
    "object 1":
    {
        "description": "description of object1's structure",
        "attributes":
        [
            {"attr 1": "a", "attr 2": 1, "name": "field 1"},
            {"attr 1": "b", "attr 2": 2, "name": "field 2"},
            {"attr 1": "c", "attr 2": 3, "name": "field 3"}
        ],
        "objects":
        {
            "field 2":
            {
                "123": "fx",
                "456": "fy",
                "789": "fz"
            }
        }
    }
}
```
