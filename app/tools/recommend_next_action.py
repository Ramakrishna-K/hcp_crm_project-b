from app.services.llm import llm


def recommend_next_action(summary: str):

    prompt = f"""
    Based on this summary recommend the next sales action.

    {summary}
    """

    response = llm.invoke(prompt)

    return response.content