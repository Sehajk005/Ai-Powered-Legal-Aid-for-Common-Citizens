import sys
import os

# Add the project's root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.pipeline import process_pdf_for_text
from src.information_extraction.extractor import extract_entities_with_llm
from src.information_extraction.extractor import answer_user_questions
import tempfile
import json
import re
import streamlit as st 

if 'message_history' not in st.session_state:
    st.session_state.message_history = []
    
st.title("AI Powered Legial Aid For Common Citizens")
upload_file = st.file_uploader("Upload a PDF", type=['pdf'])
if upload_file is not None:
    if st.button("Analyze Document", type="primary"):
        with st.spinner("Processing PDF... This may take a few minutes..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tem_file: # create a temporary file
                tem_file.write(upload_file.getvalue()) # write the uploaded file to the temporary file
                tem_file_path = tem_file.name # get the temporary file path
    
            text = process_pdf_for_text(tem_file_path)
    
            llm_output = extract_entities_with_llm(text)
            try:
                start_index = llm_output.find("{")
                end_index = llm_output.rfind("}") + 1
                if start_index != -1 and end_index != 0:
                    json_data = llm_output[start_index:end_index]
                    data = json.loads(json_data)
                    st.code(data, language='json')
                    # Store the data in the Streamlit session
                    st.session_state.document_text = text
                    st.session_state.llm_output = json_data
                    st.session_state.analysis_data = data
                    st.session_state.analysis_complete = True
                else:
                    st.error("Could not find a valid JSON object in the LLM's response.")
                    data = {} # set data to an empty dictionary to avoid errors
            except json.JSONDecodeError as e:
                st.error(f"Error decoding JSON: {e}")
                st.code(llm_output, language='text') # display the raw LLM output
                data = {} # create an empty dictionary to avoid errors
if st.session_state.get('analysis_complete'):
    st.subheader("------Analysis Report------\n")
    
    report_data = st.session_state.analysis_data
    # Used the safer .get() method in case 'entities' is missing
    entities_data = report_data.get('entities', {})
    st.markdown(f"**Individual Names:** {entities_data.get('individuals', 'Not Found')}")
    st.markdown(f"**Dates:** {entities_data.get('dates', 'Not Found')}")
    st.markdown(f"**Addresses:** {entities_data.get('addresses', 'Not Found')}")
    st.markdown(f"**Phone Numbers:** {entities_data.get('phone_numbers', 'Not Found')}")
    st.markdown(f"**Emails:** {entities_data.get('emails', 'Not Found')}")
    st.markdown(f"**Company Names:** {entities_data.get('companies', 'Not Found')}")
    st.markdown(f"**Organization Names:** {entities_data.get('organizations', 'Not Found')}")
    
    st.subheader(f"Found {len(report_data.get('clauses', []))} clauses:")

    # Used the safer .get() method in case 'clauses' is missing
    for clause in report_data.get('clauses', []):
        # Used an expander to keep the UI clean
        with st.expander(f"**{clause.get('clause_title', 'Untitled Clause')}**"):
    
            st.markdown(f"""
            - **Clause Type:** *{clause.get('clause_type', 'N/A')}*
            - **Summary:** {clause.get('summary_in_plain_english', 'N/A')}
            - **Potential Risks:** {clause.get('potential_risks', 'N/A')}
            """)

            # Write the full clause text
            st.markdown("**Full Clause Text:**")
            st.write(clause.get('clause_text', 'N/A'))
    
    st.header("Ask questions regarding any queries from the document:")
    # display the chat history
    for message in st.session_state.message_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    # Get new user input using st.chat_input
    # The walrus operator (:=) assigns the input to prompt and checks if it's not None in one go
    if prompt := st.chat_input("Ask a question"):
        # 1. add user message to chat history
        st.session_state.message_history.append({"role": "user", "content": prompt})
        # 2. Display user message in chat
        with st.chat_message("user"):
            st.markdown(prompt)
        # 3. get the assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                doc_text = st.session_state.document_text
                response = answer_user_questions(doc_text, prompt)
                st.markdown(response)
                
        # 4. add assistant response to chat history
        st.session_state.message_history.append({"role": "assistant", "content": response})
        