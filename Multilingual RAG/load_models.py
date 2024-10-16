from sentence_transformers import SentenceTransformer

def load_embedding_model(model_name):
    model = SentenceTransformer(model_name, trust_remote_code=True)
    return model