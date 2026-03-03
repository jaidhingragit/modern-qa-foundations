import json

def calculate_similarity(expected, actual):
    # Lowercase and split into words
    expected_set = set(expected.lower().replace('.', '').split())
    actual_set = set(actual.lower().replace('.', '').split())
    
    # Calculate Jaccard Similarity (a common Data Science metric)
    intersection = expected_set.intersection(actual_set)
    union = expected_set.union(actual_set)
    return (len(intersection) / len(union)) * 100

# Load the data
with open('test_cases.json', 'r') as f:
    tests = json.load(f)

print(f"{'ID':<5} | {'Score':<10} | {'Status':<10}")
print("-" * 30)

for case in tests:
    score = calculate_similarity(case['ground_truth'], case['ai_response'])
    status = "PASS" if score > 50 else "FAIL (Low Similarity)"
    print(f"{case['id']:<5} | {score:<10.2f}% | {status:<10}")