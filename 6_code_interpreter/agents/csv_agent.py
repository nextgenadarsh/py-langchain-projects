from langchain_ollama import OllamaLLM
from langchain.agents import AgentExecutor
from langchain_experimental.agents import create_csv_agent


def get_csv_agent_executor() -> AgentExecutor:
    csv_agent = create_csv_agent(
        path="episode_info.csv",
        llm=OllamaLLM(temperature=0, model="llama3"),
        verbose=True,
        allow_dangerous_code=True,
    )
    return csv_agent


def execute_csv_agent():
    csv_agent = get_csv_agent_executor()
    csv_agent.invoke(
        input={"input": "how many columns are there in file episode_info.csv"}
    )
    csv_agent.invoke(
        input={
            "input": "print seasons ascending order of the number of episodes they have."
        }
    )
