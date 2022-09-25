#!/usr/bin/python3

import re
import sys
import argparse
from pathlib import Path
from mako.template import Template


def commandline():
    parser = argparse.ArgumentParser(description="just used to set the filename")
    parser.add_argument("inputfile", type=str, help="name of the input file")
    parser.add_argument("-o", "--outputfile", type=str, help="name of the output file", default=None)
    args = parser.parse_args()
    return vars(args)

def readFile(filename):
    shortcut = None
    text = None
    try:
        with open(filename) as f:
            shortcut = f.readline().strip()
            text = f.read().strip()
    except FileNotFoundError:
        print("file not found", file = sys.stderr)
        exit(1)
    return shortcut, text


def extractVariables(text):
    if text == None: return {}
    res = set(re.findall(r"\$[a-zA-Z]+\$", text)) - {"$selected$", "$end$"}
    return {x.replace("$", "") for x in res}


if __name__ == "__main__":
    args = commandline()
    path = args["inputfile"]
    myTemplate = Template(filename="template.mako")
    data = {}
    data["shortcut"], data["text"] = readFile(path)
    data["title"] = Path(path).stem
    data["variables"] = extractVariables(data["text"])
    for key, value in data.items(): assert value != None, f"generation error with {key}"
    result = myTemplate.render(**data)

    output = args["outputfile"]
    if output == None: output = data["title"] + ".snippet" 
    with open(output, "w") as f:
        f.write(result)
    
