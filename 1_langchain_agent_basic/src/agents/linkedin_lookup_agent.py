from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain_ollama import ChatOllama
from langchain import hub

from src.tools.tavily_search_tool import search_linkedin_profile_url

print("Linkedin Lookup Agent")


def lookup(name: str) -> str:
    llm = ChatOllama(temperature=0, model="llama3")
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile pages.
                  Your answer should contain only a URL"""

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google for linkedin profile page",
            func=search_linkedin_profile_url,
            description="useful for when you need get the Linkedin page url",
        )
    ]
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_url = result["output"]
    print("Response: ", linkedin_url)
    return linkedin_url


if __name__ == "__main__":
    load_dotenv()
    linkedin_url = lookup("Adarsh Kumar")
    print("*******************************")
    print(linkedin_url)
