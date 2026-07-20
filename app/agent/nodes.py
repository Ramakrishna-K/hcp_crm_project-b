


from app.tools.extract_interaction import extract_interaction
from app.tools.summarize import summarize
from app.tools.recommend_next_action import recommend_next_action


def extract_node(state):

    data = extract_interaction(state["message"])

    return {
        **state,
        **data
    }


def summarize_node(state):

    summary = summarize(state["message"])

    return {
        **state,
        "summary": summary
    }


def recommendation_node(state):

    recommendation = recommend_next_action(state["summary"])

    return {
        **state,
        "next_action": recommendation
    }