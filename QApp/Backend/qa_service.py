# QApp/Backend/qa_service.py
from QApp.Backend.data_access import get_docs
import sys

sys.path.insert(0, 'workspace/MLOPs-Docker-app3')
def answer_question(question: str) -> str:
    docs = get_docs()
    q = question.lower()
    for keyword, answer in docs.items():
        if keyword in q:
            return answer
    return "I do not know. Try asking about docker, image, container, or port."

