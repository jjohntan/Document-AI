def  generate_prompt(query, context):
    prompt = f"""You are a helpful assistant. Answer the following question based on the provided context.

Use ONLY the context below to answer the question. Do not use prior knowledge.
If the context does not contain the answer, say "I cannot answer from the
provided context" and stop.

Question: {query}

Context: {context}"""

    return prompt