# pip-Dependencies:
# - pip3 install mistletoe
# - pip3 install colorama

from mistletoe import Document
from mistletoe.block_token import Heading, CodeFence, Paragraph, List
from mistletoe.span_token import RawText, InlineCode, Link
from colorama import Fore
import sys
import os
import subprocess


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
        makemeDomain = []

        for element in ast.children:
            if isinstance(element, Heading):
                makemeDomain = makemeDomain[0:element.level-1]
                makemeDomain.append(element.children[0].content.lower().replace(" ", "_").strip())
                makeme[" ".join(makemeDomain)] = []
            else:
                makeme[" ".join(makemeDomain)].append(element)

        command = " ".join(map(lambda arg: arg.lower().replace(" ", "_"), sys.argv[1::]))
        execution = list(map(lambda element: element[1], filter(lambda element: element[0].endswith(("makeme " + command).strip()), makeme.items())))

        if len(execution) < 1:
            print("[Error] No command for: makeme", command)
        else:
            self.execute(execution[0])

    def executeSpanToken(self, execution: list):
        for element in execution:
            if isinstance(element, RawText):
                print(element.content, end="")
            elif isinstance(element, InlineCode):
                print(Fore.GREEN ,end="")
                print(element.children[0].content, end="")
                print(Fore.RESET, end="")
            elif isinstance(element, Link):
                print(Fore.YELLOW, end="")
                print(element.children[0].content, end="")
                print(" (" + element.target + ")", end="")
                print(Fore.RESET, end="")
            else:
                print(type(element), end="")

    def execute(self, execution: list):
        for element in execution:
            if isinstance(element, CodeFence):
                lines = element.children[0].content.strip().split("\n")
                print(Fore.GREEN, end="")
                if(element.language.upper() in ["BASH", "SHELL", "BATCH"]):
                    for line in lines:
                        print("$", line)
                    print(Fore.CYAN, end="")
                    if input("Want to run command(s)? (Y/n): ") != 'n':
                        for command in lines:
                            exitCode = os.system(command)
                            if exitCode != 0:
                                print("❌", command + " => exitcode: " + str(exitCode))
                                exit(exitCode)
                            else:
                                print("✅", command)
                else:
                    for line in lines:
                        print(line)
                print(Fore.RESET, end="")
            elif isinstance(element, Paragraph):
                self.executeSpanToken(element.children)
                print()
            elif isinstance(element, List):
                for listElement in element.children:
                    print("- ", end="")
                    self.execute(listElement.children)
            else:
                print(type(element))

if __name__ == '__main__':
    makeme = MakeMe()
    makeme.run(["README.md", "README"])
