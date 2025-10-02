import os
from dotenv import load_dotenv
import google.generativeai as genai

# This line loads the variables from your .env file
load_dotenv()

# This safely gets the key from the environment
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-flash-latest")


def extract_entities_with_llm(text):
    full_prompt = f"""You are an expert legal assistant. From the document text provided, perform two tasks:
    
    Task 1: Extract key entities.
    Task 2: Analyze and extract key clauses.

    Return your response as a single, raw JSON object with two top-level keys: "entities" and "clauses".

    The "entities" key should contain an object with the following fields:
    - "individual_names"
    - "dates"
    - "addresses_locations"
    - "phone_numbers"
    - "emails"
    - "company_names"
    - "organization_names"

    The "clauses" key should contain a JSON array where each object in the array represents a clause and has the following fields:
    - "clause_title"
    - "clause_type" (Categorize from: [Termination, Payment, Liability, Confidentiality, Governing Law, Force Majeure, General, Other])
    - "clause_text" (The exact text of the clause)
    - "summary_in_plain_english"
    - "potential_risks"

    IMPORTANT: Your entire output must be only the raw JSON object, starting with {{ and ending with }}. Do not include any other text or markdown formatting.

    Here is the document:
    ---
    {text}
    ---
    """
    response = model.generate_content(full_prompt)
    return response.text

def answer_user_questions(full_context, user_question):
    prompt = f"""You are an expert legal Q&A assistant. Your task is to answer the user's question based on the context provided below.
    The context contains two parts: the original document text and a detailed JSON analysis of that document which includes summaries and identified potential risks.
    
    When answering, synthesize information from BOTH parts. For questions about risks, summaries, or specific clauses, rely heavily on the "DETAILED ANALYSIS" section.
    
    Answer in simple, plain English. If the answer cannot be found in the provided context, say "The answer is not found in the provided document."

    ----- CONTEXT -----
    {full_context}
    ----- END OF CONTEXT -----

    Based on the context above, answer the following question:
    USER QUESTION: {user_question}
    ANSWER: """
    response = model.generate_content(prompt)
    return response.text

