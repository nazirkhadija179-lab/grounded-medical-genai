from models.vision_model import get_image_findings
from models.rag_retriever import retrieve

def build_evidence(image, history):

    return {
        "image_evidence": get_image_findings(image),
        "text_evidence": retrieve(history),
        "history": history
    }
