from src.information_extraction.extractor import extract_entities_with_llm
import json
import re

sample_text = """
This agreement is made on August 5, 2025, between John Doe,
residing at 123 Fictional Lane, Chandigarh, India, and Jane Smith,
of 456 Example Ave, New Delhi. The primary property is located at
789 Test Street, Sector 17, Chandigarh.
"""

print("Sending text to LLM for entity extraction...")

llm_output = extract_entities_with_llm(sample_text)
clean_llm_output = re.sub(r"```json", "", llm_output)
clean_llm_output = re.sub(r"```", "", clean_llm_output)
try:
    data = json.loads(clean_llm_output)
    print("------Analysis Report------\n")
    
    entities_data = data['entities']
    print(f"Individual Names: {entities_data['individuals']}\n")
    print(f"Dates: {entities_data['dates']}\n")
    print(f"Addresses: {entities_data['addresses']}\n")
    print(f"Phone Numbers: {entities_data['phone_numbers']}\n")
    print(f"Emails: {entities_data['emails']}\n")
    print(f"Company Names: {entities_data['companies']}\n")
    print(f"Organization Names: {entities_data['organizations']}\n")
    
    print(f"Found {len(data['clauses'])} clauses:\n")
    for clause in data['clauses']:
        print(f"Clause Title: {clause['clause_title']}\n \
            Clause Type: {clause['clause_type']}\n \
            Clause Text: {clause['clause_text']}\n \
            Summary in Plain English: {clause['summary_in_plain_english']}\n \
            Potential Risks: {clause['potential_risks']}\n")
except json.JSONDecodeError:
    print("------ERROR------\n")
    print("Failed to parse JSON output from LLM. Please check the output format.\n")
    print("Raw output from LLM:", clean_llm_output)
    
from src.information_extraction.extractor import answer_user_questions

document_text = clean_llm_output
user_quesrion_1 = "Who is this agreement between?\n"
print(f"Question 1: {user_quesrion_1}\n")
answer_1 = answer_user_questions(document_text, user_quesrion_1)
print(f"Answer 1: {answer_1}\n")

user_quesrion_2 = "What is the penalty for late payment?"
print(f"Question 2: {user_quesrion_2}\n")
answer_2 = answer_user_questions(document_text, user_quesrion_2)
print(f"Answer 2: {answer_2}\n")