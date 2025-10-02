import os
from dotenv import load_dotenv
import google.generativeai as genai

# This line loads the variables from your .env file
load_dotenv()

# This safely gets the key from the environment
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash-001")

def extract_entities_with_llm(text):
    full_prompt = f"""You are an expert legal assistant. From the following document provided, you need to perform the following tasks:\
        Task 1: Extract entities from the document:\
        1. the full name of the individual mentioned\
        2. All dates mentioned\
        3. All addresses or specific locations mentioned\
        4. All phone numbers\
        5. All emails\
        6. All names of companies\
        7. All names of organizations\
            
        Task 2: Extract key clauses from the document:\
        Analyze the document and identify key clauses that the document contains.\
        provide the result in the following JSON format:\
        1. 'clause_title': A short descriptive title for the clause.(eg: 'Termination clause')\
        2. 'clause_type': Categorize the clause into a high level category from the following:[Termination, Payment, Liability, Confidentiality, Governing Law, Force Majeure, General, Other]\
        3. 'clause_text': Extract the text of the clause exactly as it appears in the document.
        4. 'summary_in_plain_english': Summarize the clause in plain English so that a non-legal person can understand the clause.
        5. 'potential_risks': assess the potential risks for the citizen and provide a short summary of the potential risks.
        6. Analyze the entire document and return the result as a JSON array of all the clauses you can identify.\
        Here is the document: {text}"""
    response = model.generate_content(full_prompt)
    return response.text

def answer_user_questions(document_text, user_question):
    prompt = f"""You are a helpful Q&A chatbot Assistant. Your task is to answer the user question solely based on the provided document \
        text and not from any other source if the answer to the question is not found in the document text just simply return with \
        'The answer is not found in the provided document.'. give the answer in simple plain English so that the normal citizen can understand.\
        -----DOCUMENT TEXT-----\
            {document_text}\
        -----END OF DOCUMENT TEXT-----\
        Based on the document above, answer the following question:\
        USER QUESTION:{user_question}\
        ANSWER: """
    response = model.generate_content(prompt)
    return response.text