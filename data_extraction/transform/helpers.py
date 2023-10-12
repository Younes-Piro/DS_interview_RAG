import re
import spacy
from sklearn.metrics.pairwise import cosine_similarity

def remove_enumeration(text):
    # Use regular expressions to remove enumeration (e.g., "1.", "2.")
    cleaned_text = re.sub(r'^\d+\.\s+', '', text)
    return cleaned_text

def are_questions_duplicates(q1, q2):

    # Load spaCy model
    nlp = spacy.load("en_core_web_sm")

    # Tokenize and vectorize the questions
    doc1 = nlp(q1)
    doc2 = nlp(q2)
    
    # Calculate cosine similarity between the question vectors
    similarity_score = cosine_similarity(doc1.vector.reshape(1, -1), doc2.vector.reshape(1, -1))[0][0]
    
    # Set a similarity threshold (experiment with different values)
    threshold = 0.9
    
    # Check if the questions are duplicates
    return similarity_score >= threshold

