import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_semantic_similarity(expected, actual):
    # Vectorize the text (turn words into math vectors)
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([expected, actual])
    
    # Calculate how 'close' the vectors are in 3D space
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])
    return round(similarity[0][0] * 100, 2)

# Load the data
with open('test_cases.json', 'r') as f:
    tests = json.load(f)

print(f"{'ID':<5} | {'Semantic Score':<15} | {'Status':<10}")
print("-" * 40)

for case in tests:
    score = calculate_semantic_similarity(case['ground_truth'], case['ai_response'])
    # In Semantic testing, >70% is usually a strong match
    status = "PASS" if score > 70 else "FAIL (Low Meaning Match)"
    print(f"{case['id']:<5} | {score:<15.2f}% | {status:<10}")