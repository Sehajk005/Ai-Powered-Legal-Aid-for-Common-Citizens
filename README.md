# AI-Powered Legal Aid for Common Citizens

## Overview

**AI-Powered Legal Aid for Common Citizens** is a Streamlit-based application that leverages advanced AI and natural language processing to help everyday users understand complex legal documents. The app extracts key information, translates legal jargon into plain English, and provides intelligent clause-by-clause analysis with risk assessments. It also features an integrated chatbot for document-specific Q&A and a feedback mechanism to support research in Responsible AI and LLM Alignment.

---

## Features

- **PDF Document Upload**: Upload legal documents in PDF format for analysis
- **Entity Extraction**: Automatically identifies names, dates, addresses, organizations, and other key entities
- **Clause Analysis**: Splits documents into distinct clauses with summaries and risk assessments
- **Interactive Q&A Chat**: Ask specific questions about your document and receive AI-powered answers
- **Feedback Interface**: Rate responses and provide comments to help improve the AI
- **Privacy-Focused**: Secure Google Sheets integration for anonymized feedback collection

---

## Research Purpose

This project serves a dual purpose:

1. **Democratizing Legal Knowledge**: Making legal documents accessible to common citizens without legal expertise
2. **Advancing Responsible AI Research**: Collecting feedback data to improve:
   - **Responsible AI**: Transparency, fairness, safety, and explainability in legal AI systems
   - **LLM Alignment**: Ensuring large language models provide reliable, unbiased, and safe legal information

---

## How to Use

1. **Upload** your legal PDF document
2. **Review** extracted entities, dates, names, and organizations
3. **Explore** clause-by-clause summaries with risk analysis
4. **Ask Questions** using the interactive chatbot
5. **Provide Feedback** by rating responses (👍/👎) and leaving comments

---

## Data Collection & Ethics

### What We Collect
- User questions and AI responses
- Feedback ratings and optional comments
- Timestamp information
- Usage patterns (anonymized)

### What We DON'T Collect
- Personal identifying information (unless voluntarily provided)
- Uploaded document contents (processed locally, not stored)
- IP addresses or tracking data

### Your Rights
- All feedback is anonymized and used solely for academic research
- You may request data removal at any time
- Participation is voluntary and can be withdrawn

**Contact for data removal**: sehajk2048@gmail.com

---

## Technology Stack

- **Frontend**: Streamlit
- **LLM/NLP**: Google Gemini 1.5 Flash API
- **PDF Processing**: pdfplumber, PyPDF2
- **OCR**: Tesseract (optional)
- **Data Storage**: Google Sheets via `streamlit-gsheets`
- **Deployment**: Streamlit Community Cloud

---

## Installation & Setup

### Prerequisites
- Python 3.8+
- Google Gemini API key
- Google Cloud Service Account (for Sheets integration)

### Local Installation

```bash
# Clone the repository
git clone https://github.com/Sehajk005/Ai-Powered-Legal-Aid-for-Common-Citizens.git

# Install dependencies
pip install -r requirements.txt

# Set up secrets
# Create .streamlit/secrets.toml with your API keys and service account credentials
```

### Configuration

Create `.streamlit/secrets.toml`:

```toml
# Gemini API
GEMINI_API_KEY = "your-api-key-here"

# Google Sheets Connection
[connections.gsheets]
spreadsheet = "your-google-sheet-url"
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-private-key-id"
private_key = "your-private-key"
client_email = "your-service-account-email"
client_id = "your-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "your-cert-url"
```

### Run Locally

```bash
streamlit run app.py
```

---

## Deployment

This app is deployed on Streamlit Community Cloud:

**Live App**: http://ai-powered-legal-aid-for-common-citizens.streamlit.app/

To deploy your own version:
1. Fork this repository
2. Connect your GitHub repo to [Streamlit Community Cloud](https://streamlit.io/cloud)
3. Add your secrets in the Streamlit Cloud dashboard
4. Deploy!

---

## 📝 Feedback & Participation

We encourage users to participate in our research by:

- **Using the app** and providing ratings/comments on AI responses
- **Filling out our survey**: https://docs.google.com/forms/d/e/1FAIpQLSfbnCaBoyoMc7Ui0IUkliSQRckk2ZlmRDRkukNLczoClEqbTw/viewform?usp=header
- **Reporting bugs** via GitHub Issues
- **Contributing code** via Pull Requests

---

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

Please ensure your code follows best practices for Responsible AI and includes appropriate documentation.

---

## Documentation

For more details on the project structure and implementation:

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Gemini API](https://ai.google.dev/docs)
- [Responsible AI Practices](https://ai.google/responsibility/responsible-ai-practices/)

---

## Citation

If you use this work in your research, please cite:

```bibtex
@misc{legalAidAI2025,
  title={AI-Powered Legal Aid for Common Citizens},
  author={Sehaj Khurana},
  year={2025},
  howpublished={\url{https://github.com/Sehajk005/Ai-Powered-Legal-Aid-for-Common-Citizens.git}},
  note={A Responsible AI research project for LLM alignment in legal domain}
}
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Disclaimer

**This application is for educational and research purposes only. It does NOT constitute legal advice. For actual legal matters, please consult a qualified attorney.**

---

## Contact

**Sehaj Khurana**
- Email: sehajk2048@gmail.com
- LinkedIn: www.linkedin.com/in/sehaj-khurana-8b0200359
- GitHub: [@Sehajk005](https://github.com/Sehajk005)

---

## Acknowledgments

- Thanks to all beta testers and feedback contributors
- Google Gemini API for powering the AI capabilities
- Streamlit for the excellent framework
- The Responsible AI research community

---

## Roadmap

- [ ] Multi-language support
- [ ] Fine-tuning on legal domain data
- [ ] RAG (Retrieval-Augmented Generation) implementation
- [ ] Mobile app version
- [ ] Support for more document formats (DOCX, images)
- [ ] Advanced analytics dashboard for feedback

---

**⭐ If you find this project helpful, please star the repository!**
