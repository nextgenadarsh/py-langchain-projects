from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import exact
from inspect_ai.solver import generate


@task
def hello_world():
    return Task(
        dataset=[
            Sample(
                input="Just reply with Hello World",
                target="Hello World",
            ),
            Sample(
                input="Greet in morning",
                target="Good morning",
            ),
        ],
        solver=[generate()],
        scorer=exact(),
    )
