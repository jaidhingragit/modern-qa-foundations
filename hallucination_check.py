import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_semantic_similarity(expected, actual):
    # This turns sentences into math vectors to compare meaning
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([expected, actual])
    
    # Calculate how 'close' the meaning is (0 to 100)
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])
    return round(similarity[0][0] * 100, 2)

# Load your test cases
try:
    with open('test_cases.json', 'r') as f:
        tests = json.load(f)
except FileNotFoundError:
    print("Error: test_cases.json not found!")
    tests = []

print(f"{'ID':<5} | {'Semantic Score':<15} | {'Status':<10}")
print("-" * 45)

for case in tests:
    score = calculate_semantic_similarity(case['ground_truth'], case['ai_response'])
    # In AI QA, a semantic score > 70 is usually considered a pass
    status = "PASS" if score > 70 else "FAIL (Low Meaning Match)"
    print(f"{case['id']:<5} | {score:<15.2f}% | {status:<10}")