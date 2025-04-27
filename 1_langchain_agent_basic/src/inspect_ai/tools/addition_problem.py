"""
    Run using `inspect eval ./src/inspect_ai/tools/addition_problem.py --limit 50  --model google/gemini-2.0-flash`
"""

from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import match
from inspect_ai.solver import generate, use_tools
from inspect_ai.tool import tool


@tool
def add():
    async def execute(x: int, y: int):
        """
        Add two numbers.

        Args:
            x (int): First number to add.
            y (int): Second number to add.

        Returns:
            The sum of the two numbers.
        """
        return x + y

    return execute


@task
def addition_problem():
    return Task(
        dataset=[
            Sample(input="What is 1 + 1?", target=["2", "2.0"]),
            Sample(input="What is 3 + 2?", target=["5", "5.0"]),
            Sample(input="What is 6 - 1?", target=["5", "5.0"]),
        ],
        solver=[use_tools(add()), generate()],
        scorer=match(numeric=True),
    )
