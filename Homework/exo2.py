import re

def extract_phone_numbers(text):  
    
    pattern = r'\(555\) \d{3}-\d{4}|\+\d{1}\-\d{3}\-\d{3}\-\d{4}|\+\d{2} \d{2} \d{4}\ \d{4}'
    num = re.findall(pattern, text)
    return num

# Test the function with provided text
print(extract_phone_numbers("US format: (555) 444-7890 (666) 344-7890 +1-800-555-2468, +44 20 7946 0958"))
