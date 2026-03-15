def evaluate_retrieval(question, docs):
    """
    Simple heuristic to check if retrieved docs contain question keywords.
    """

    question_words = set(question.lower().split())

    matched_chunks = 0

    for doc in docs:
        text_words = set(doc.page_content.lower().split())

        if question_words.intersection(text_words):
            matched_chunks += 1

    score = matched_chunks / len(docs)

    return score


def evaluate_context_length(docs):
    """
    Measure total retrieved context length.
    """

    total_length = sum(len(doc.page_content) for doc in docs)

    return total_length


def evaluate_answer(answer):
    """
    Basic heuristic to check answer completeness.
    """

    word_count = len(answer.split())

    if word_count < 20:
        return "Answer too short"

    return "Answer length acceptable"