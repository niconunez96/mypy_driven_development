from typing import Dict, Literal, Type


class Tool:
    def act(self) -> None:
        raise NotImplementedError


class Hammer(Tool):
    def act(self) -> None:
        print("Hammering 🔨...")


class Saw(Tool):
    def act(self) -> None:
        print("Slicing 🪚...")


class Spanner(Tool):
    def act(self) -> None:
        print("Adjusting 🔧...")


bad_tools: Dict[str, Tool] = {"hammer": Hammer}  # mypy complains ❌

"""
Dict[str, Tool] --> this means a dictionary that has:
strings as key
Tool "instances" as value

Using Dict[str, Type[Tool]] we say now:
strings as key
Tool "classes" as value
"""

tools: Dict[str, Type[Tool]] = {
    "hammer": Hammer,
    "saw": Saw,
    "spanner": Spanner,
}


def use_tool(tool_name: str) -> None:
    if tool_name not in tools.keys():
        print("Tool does not exist 🫠")
        return
    tool = tools[tool_name]()
    tool.act()


ToolType = Literal["hammer", "saw", "spanner"]
tools2: Dict[ToolType, Type[Tool]] = {
    "hammer": Hammer,
    "saw": Saw,
    "spanner": Spanner,
    "martillo": Spanner,  # mypy complains here ❌
}


def use_tool_2(tool_name: ToolType) -> None:
    """
    We don't need this validation anymore
    Mypy already check this for us! 🥳🥳🥳
    """
    # if tool_name not in tools.keys():
    #     print("Tool does not exist 🫠")
    #     return
    tool = tools[tool_name]()
    tool.act()


def main() -> None:
    use_tool("hammer")
    """
    We need to introduce defensive code here
    We cannot allow clients to send any string
    Constants do not save us from adding defensive code 💩
    """
    use_tool("🔨")
    use_tool_2("hammer")
    use_tool_2("martillo")  # mypy complains here ❌
