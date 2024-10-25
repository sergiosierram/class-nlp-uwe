# NLP Class Materials

## Requirements

- Python 3.9 or higher
- `venv` for managing virtual environments
- A valid OpenAI API key stored in `.env` (You will receive one from the lecture tutors)

## Setup Instructions

Follow these steps to get the project up and running:

### 1. Clone the Repository
Open a terminal of you preference.

```bash
git clone <repository-url>
cd class-nlp-uwe
```

### 2. Set Up a Virtual Environment

It's recommended to use `venv` for managing dependencies in an isolated environment.

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

Once the virtual environment is activated, install the required packages:

> [!WARNING]  
> This could take a while!

```bash
pip install -r requirements.txt
```

If you are using mac, you need to install portaudio first:

```bash
brew install portaudio
```

Additionally, you need to download the necessary datasets/models for specific functions to work. 

```bash
python -m nltk.downloader popular
python -m nltk.downloader punkt_tab
python -m nltk.downloader stopwords
python -m nltk.downloader averaged_perceptron_tagger_eng
python -m nltk.downloader maxent_ne_chunker_tab
python -m nltk.downloader vader_lexicon
python -m spacy download en_core_web_sm
```

### 4. Set Up Environment Variables

Store your environment variables, including the OpenAI API key, in a `.venv` file in the root directory:

```bash
# .venv file contents
OPENAI_API_KEY=your-openai-api-key
```