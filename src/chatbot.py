from transformers import pipeline

class GenAIChatbot:
    def __init__(self):
        self.qa_pipeline = pipeline("question-answering", model="distilbert/distilbert-base-cased-distilled-squad")

    def get_answer(self, question, context):
        if not question:
            return {'answer': ""}
        if not context:
            return {'answer': "Context is required to provide an answer."}
        return self.qa_pipeline(question=question, context=context)