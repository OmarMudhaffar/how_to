import os
import logging
import anthropic


def ask_ai(question):
    if not os.getenv("ANTHROPIC_API_KEY"):
        return "No AI key found. Put ANTHROPIC_API_KEY in the .env file."

    try:
        client = anthropic.Anthropic()
        response = client.messages.create(
            model="claude-opus-5-5",
            max_tokens=4000,
            output_config={"effort": "low"},
            system="You are a kind dad. Explain how to do things in max 5 short simple lines.",
            messages=[{"role": "user", "content": question}],
        )
    except anthropic.AuthenticationError:
        return "The AI key in .env is wrong."
    except anthropic.APIConnectionError:
        return "No internet connection."
    except anthropic.APIStatusError as error:
        logging.error("ai error: " + str(error.status_code))
        return "AI is busy now, try again later."

    texts = [block.text for block in response.content if block.type == "text"]
    return " ".join(texts)
