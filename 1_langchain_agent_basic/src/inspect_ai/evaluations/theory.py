from inspect_ai import Task, task
from inspect_ai.dataset import example_dataset
from inspect_ai.scorer import model_graded_fact
from inspect_ai.solver import chain_of_thought, generate, self_critique

"""_summary_
    The @task decorator applied to the theory_of_mind() function is what enables inspect eval to find and run the eval in the source file passed to it.
Returns:
    _type_: _description_
"""


@task
def theory_of_mind():
    return Task(
        dataset=example_dataset("theory_of_mind"),
        solver=[chain_of_thought(), generate(), self_critique()],
        scorer=model_graded_fact(),
    )
