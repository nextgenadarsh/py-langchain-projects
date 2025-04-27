from typing import Any, Dict, List
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser


class Summary(BaseModel):
    summary: str = Field(description="Summary")
    facts: List[str] = Field(description="Interesting facts about them")

    def to_dict(self) -> Dict[str, Any]:
        return {"summmary": self.summary, "facts": self.facts}


summary_parser = PydanticOutputParser(pydantic_object=Summary)
