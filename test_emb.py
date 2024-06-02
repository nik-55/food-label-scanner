from gemini import genai
import numpy as np
import pickle


model = "models/embedding-001"


def find_best_passage(query, dataframe):
    """
    Compute the distances between the query and each document in the dataframe
    using the dot product.
    """
    query_embedding = genai.embed_content(
        model=model, content=query, task_type="retrieval_query"
    )
    dot_products = np.dot(
        np.stack(dataframe["Embeddings"]), query_embedding["embedding"]
    )
    idx = np.argmax(dot_products)
    return dataframe.iloc[idx]["Text"]


with open("embedding.pkl", "rb") as f:
    df = pickle.load(f)

query = "How do you shift gears in the Google car?"
passage = find_best_passage(query, df)
print(passage)
