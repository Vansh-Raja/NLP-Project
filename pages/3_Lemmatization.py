import streamlit as st

from Tokenisation import tokenisation as tkn
from Lemmatization import lemmatization as lmt

st.set_page_config(page_title="NLP Project", page_icon=":book:", layout="wide")

example_text_Lemmatization = "best well better was were is am"

with st.expander("Learn about Lemmatization: "):
    "Different types of spacy models:"

    st.text("1. **en_core_web_sm**: Small model with basic vocabulary, syntax, and named entity recognition,")
    st.text("suitable for lightweight text processing tasks.")

    st.text("2. **en_core_web_md**: Medium-sized model offering improved accuracy and coverage with additional")
    st.text("features compared to the small model, suitable for a wide range of text processing tasks.")

    st.text("3. **en_core_web_lg**: Large model providing high accuracy and coverage, including word vectors")
    st.text("and extra data, suitable for advanced text analysis requiring more computational resources.")

    st.text("4. **en_core_web_trf**: Transformer-based model using state-of-the-art architecture for text")
    st.text("processing tasks, offering top performance but requiring significant computational resources.")
    
st.header("Test it out:")

#Choose a method
lemma_option = st.selectbox(label="Choose a method for Lemmatization", 
                                    options=("Nltk Lemmatizer",
                                            "Spacy Lemmatizer",
                                            "Stanza Lemmatizer",
                                            "Lemminflect Lemmatizer"),
                                    placeholder="Lemmatization method",
                                    index=None,
                                    key="lem_methodSel")

# If option is chosen as Nltk Lemmatizer give option for either auto or manual pos tagging
if lemma_option == "Nltk Lemmatizer":
    nltk_mode = st.selectbox(label="Choose a method for Lemmatization", 
                                    options=("Auto POS Tagging",
                                            "Manual POS Tagging"),
                                    placeholder="Lemmatization method",
                                    index=None,
                                    key="nltk_modeSel")
    
    if nltk_mode == "Manual POS Tagging":
        nltk_pos = st.selectbox(label="Choose a POS for Lemmatization",
                                    options=("n", "v", "a", "r"),
                                    placeholder="Select POS tag of the words",
                                    index=None,
                                    key="nltk_posSel")

if lemma_option == "Spacy Lemmatizer":
    spacy_model = st.selectbox(label="Choose a Spacy model for Lemmatization", 
                                    options=("en_core_web_sm", "en_core_web_md", "en_core_web_lg", "en_core_web_trf"),
                                    placeholder="Spacy model",
                                    index=None,
                                    key="spacy_modelSel_Lemma")

# Area to take text input
text_inp = st.text_input(label="Enter Words in form of sentence for Lemmatization",
                            placeholder=example_text_Lemmatization,
                            key="lem_inp")

# Area to take user file upload
text_upload = st.file_uploader("Upload File", type=["txt"], key="lem_uploader")

lemmatization_output = None

# If there is text input or file upload
if text_inp or text_upload is not None:
    
    # If there is text input, use that, else use the uploaded file
    if text_inp:
        content = text_inp
    else:
        content = text_upload.read().decode("utf-8")
        
    # content = tkn.word_tokenisation(content)
        
    # If the user selects Nltk Lemmatizer
    if lemma_option == "Nltk Lemmatizer":
        
        content = tkn.word_tokenisation(content)
        
        if nltk_mode == "Manual POS Tagging":
            lemmatization_output = (lmt.nltk_lemma(content, pos=nltk_pos))
            
        if nltk_mode == "Auto POS Tagging":
            lemmatization_output = (lmt.nltk_lemma_auto(content))
            
    if lemma_option == "Spacy Lemmatizer":
        lemmatization_output = (lmt.spacy_lemma(content, model=spacy_model))
        
    if lemma_option == "Stanza Lemmatizer":
        lemmatization_output = (lmt.stanza_lemma(content))
        
    if lemma_option == "Lemminflect Lemmatizer":
        
        content = tkn.word_tokenisation(content)
        lemmatization_output = (lmt.lemminflect_lemma(content))
    
if lemmatization_output:
    st.write(lemmatization_output)
else:
    st.info("Select a method and input text or upload files to see the output.")