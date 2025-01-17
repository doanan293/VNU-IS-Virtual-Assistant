from rank_bm25 import BM25Okapi
import string

# Sample list of documents (each document is a list of words)
documents = [
    "Machine learning is fascinating.",
    "Natural language processing is a subfield of artificial intelligence.",
    "Deep learning techniques are used in many applications.",
    "Artificial intelligence and machine learning are closely related.",
    "AI and ML are transforming industries.",
    # Add more documents here...
]


# Preprocess the documents
def preprocess(text):
    # Basic preprocessing: remove punctuation and convert to lowercase
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    return text.split()


# Search function to get the top 25 results
def bm25_search(query, documents, top_n=25):
    # Tokenize the documents
    tokenized_docs = [preprocess(doc) for doc in documents]

    # Initialize the BM25 object
    bm25 = BM25Okapi(tokenized_docs)
    # Preprocess the query
    tokenized_query = preprocess(query)

    # Get the BM25 scores for each document
    scores = bm25.get_scores(tokenized_query)

    # Rank the documents by score and get the top_n (25) indices
    ranked_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[
        :top_n
    ]

    # Return the top_n documents
    return [documents[i] for i in ranked_indices]
