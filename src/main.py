# pip-Dependencies:
# - pip3 install mistletoe

from mistletoe import Document
from mistletoe.block_token import Heading, CodeFence, Paragraph

import re
import sys


class MakeMe(object):
    def __init__(self):
        pass

    def loadContent(self, path: str):
        try:
            with open(path, "r") as fp:
                return fp.read()
        except:
            return ""

    def run(self, paths: list[str]):
        content = "\n".join(map(lambda path: self.loadContent(path), paths))

        ast = Document(content)

        makeme = {}
        makeme_domain = []

        for element in ast.children:
            if isinstance(element, Heading):
                makeme_domain = makeme_domain[0:element.level-1]
                makeme_domain.append(element.children[0].content.lower().replace(" ", "_").strip())
                makeme[" ".join(makeme_domain)] = []
            else:
                makeme[" ".join(makeme_domain)].append(element)

        command = " ".join(map(lambda arg: arg.lower().replace(" ", "_"), sys.argv[1::]))
        execution = list(map(lambda element: element[1], filter(lambda element: element[0].endswith(("makeme " + command).strip()), makeme.items())))

        if len(execution) < 1:
            print("[Error] No command for: makeme", command)
        else:
            self.execute(execution[0])

    def execute(self, execution: list):
        for element in execution:
            if isinstance(element, CodeFence):
                lines = element.children[0].content.strip().split("\n")
                for line in lines:
                    print("$", line)
                input("Want to run command(s)? (Y/n): ")
            elif isinstance(element, Paragraph):
                print(element.children[0].content)
            else:
                print(type(element))

if __name__ == '__main__':
    makeme = MakeMe()
    makeme.run(["README.md", "README"])
