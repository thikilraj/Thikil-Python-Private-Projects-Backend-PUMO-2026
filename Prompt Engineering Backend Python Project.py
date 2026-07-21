# Prompt Engineering Backend Project

def create_prompt(topic, audience, tone):
    prompt = f"""
You are an expert content writer.

Task:
Explain the topic: {topic}

Target Audience:
{audience}

Tone:
{tone}

Instructions:
1. Explain the topic clearly.
2. Use simple language.
3. Give one real-world example.
4. Organize the answer with headings.
5. Keep the answer concise.
"""

    return prompt


# Get user input
topic = input("Enter topic: ")
audience = input("Enter audience: ")
tone = input("Enter tone: ")

# Generate prompt
final_prompt = create_prompt(topic, audience, tone)

# Display output
print("\n----- GENERATED PROMPT -----")
print(final_prompt)