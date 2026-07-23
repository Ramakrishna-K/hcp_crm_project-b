


import json

from langchain_core.messages import SystemMessage, HumanMessage

from app.services.llm import llm
from app.agent.prompts import SYSTEM_PROMPT


def extract_interaction(message: str):

    response = llm.invoke([
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=message)
    ])

    content = response.content.strip()

    # Remove markdown if the model adds it
    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    print("\n===== EXTRACTED RESPONSE =====")
    print(content)
    print("==============================\n")

    try:
        return json.loads(content)

    except json.JSONDecodeError:

        print("Invalid JSON returned by LLM.")

        return {
            "hcp_name": "",
            "interaction_type": "",
            "date": "",
            "time": "",
            "attendees": [],
            "topics": [],
            "materials": [],
            "samples": [],
            "sentiment": "",
            "outcomes": "",
            "follow_up": ""
        }
