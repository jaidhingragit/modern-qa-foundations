# First QA Utility: Simple String Similarity Matcher
# This mimics how we check if an AI's response matches a "Ground Truth" answer.

def calculate_accuracy(expected, actual):
    expected_words = set(expected.lower().split())
    actual_words = set(actual.lower().split())
    
    # Find how many words match
    overlap = expected_words.intersection(actual_words)
    score = (len(overlap) / len(expected_words)) * 100
    return round(score, 2)

# TEST CASE
ground_truth = "The capital of France is Paris."
ai_response = "Paris is the capital city of France."

accuracy = calculate_accuracy(ground_truth, ai_response)

print(f"--- AI Response Validation ---")
print(f"Ground Truth: {ground_truth}")
print(f"AI Response: {ai_response}")
print(f"Accuracy Score: {accuracy}%")

if accuracy > 80:
    print("Result: PASS")
else:
    print("Result: FAIL - Potential Hallucination or Inaccuracy")