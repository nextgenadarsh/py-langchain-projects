from langchain.tools import Tool
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from agents.qrcode_agent import get_qrcode_agent_executor
from agents.csv_agent import get_csv_agent_executor
from langchain_ollama import OllamaLLM


def get_router_agent_executor() -> AgentExecutor:
    tools = [
        Tool(
            name="Python Agent",
            func=get_qrcode_agent_executor().invoke,
            description="""Useful when you need to transform natural language to python and execute the python code, returning the results of the code execution
            DOES NOT ACCEPT CODE AS INPUT""",
        ),
        Tool(
            name="CSV Agent",
            func=get_csv_agent_executor().invoke,
            description="""Useful when you need to answer question over episode_info.csv file, takes an input the entire question and returns the answer after running pandas calculations""",
        ),
    ]

    base_prompt = hub.pull("langchain-ai/react-agent-template")
    prompt = base_prompt.partial(instructions="")

    router_agent = create_react_agent(
        prompt=prompt, llm=OllamaLLM(temperature=0, model="llama3"), tools=tools
    )

    router_agent_executor = AgentExecutor(agent=router_agent, tools=tools, verbose=True)
    return router_agent_executor
