import json
import pandas as pd
from collections import Counter

# Load the JSON file containing the user data
with open('json_rand_users_5000.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    
# Extract the 'results' list that contains the user data
users = data['results']
    
# Extract the 'nat' field (nationality) from each user and count occurrences
nationalities = [user['nat'] for user in users]
country_counts = Counter(nationalities)

# Sort the countries by the number of users in descending order
sorted_countries = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)

results = {}
json_result = {}
array = []
for i, (country, count) in enumerate(sorted_countries, start=1):  # Use items() directly
    json_result[country] = count  # Storing the country and its count
array.append(json_result)
results['results'] = array
api_answer=json.dumps(results, ensure_ascii=False)
output_code=200
print(api_answer)
print(output_code)