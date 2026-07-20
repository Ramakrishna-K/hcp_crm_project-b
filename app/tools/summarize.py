from app.services.llm import llm


def summarize(text: str):

    prompt = f"""
    Summarize this doctor's interaction.

    {text}
    """

    response = llm.invoke(prompt)

    return response.content