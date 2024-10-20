# # need to implement the natural language processing part -- take the extracted text from pdf_text_extraction.py and analyze it 
# # see if perplexity did it properly
# # change the ui of the upload pdf so that it works
# # create a toggle to show the user the extracted text from the pdf (don't show if not wanted)
# # could create a chatbot using llama api key to train it to answer questions on the case at hand
# # hold on the speech part of the application until this is done -- if this takes too much time, then no speaking application -- just brag about this and the chatbot

# # model.py

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.ensemble import RandomForestClassifier
# from .text_processing import preprocess_text

# def extract_features(processed_text):
#     sentences = [' '.join(sentence) for sentence in processed_text]
#     vectorizer = TfidfVectorizer(max_features=1000)
#     features = vectorizer.fit_transform(sentences)
#     return features, vectorizer

# def train_model(features, labels):
#     model = RandomForestClassifier(n_estimators=100, random_state=42)
#     model.fit(features, labels)
#     return model

# def analyze_debate_case(text, model, vectorizer):
#     sections = extract_sections(text)
#     feedback = []

#     for section_name, section_content in sections.items():
#         processed_text = preprocess_text(section_content)
#         features = vectorizer.transform([' '.join(sentence) for sentence in processed_text])
#         predictions = model.predict(features)
        
#         section_feedback = analyze_section(section_name, section_content, predictions)
#         feedback.extend(section_feedback)
    
#     return feedback

# def extract_sections(text):
#     sections = {
#         "Resolution": "",
#         "Value": "",
#         "Value Criterion": "",
#         "Definitions": "",
#         "Contentions": ""
#     }
    
#     current_section = None
#     for line in text.split('\n'):
#         if "resolved:" in line.lower():
#             current_section = "Resolution"
#         elif "value" in line.lower() and "criterion" not in line.lower():
#             current_section = "Value"
#         elif "criterion" in line.lower():
#             current_section = "Value Criterion"
#         elif "definition" in line.lower():
#             current_section = "Definitions"
#         elif "contention" in line.lower():
#             current_section = "Contentions"
        
#         if current_section:
#             sections[current_section] += line + "\n"
        
#         if any(phrase in line.lower() for phrase in ["thus, i affirm", "thus, i negate", "i strongly urge", "for all these reasons"]):
#             break
    
#     return sections

# def analyze_section(section_name, content, predictions):
#     feedback = []
#     sentences = sent_tokenize(content)
    
#     if section_name == "Resolution":
#         feedback.append(f"Resolution: {sentences[0].strip()}")
#         feedback.append("Suggestion: Ensure the resolution is clearly stated and addresses the topic.")
    
#     elif section_name == "Value":
#         if content:
#             feedback.append(f"Value: The case presents '{sentences[0].strip()}' as the value.")
#             feedback.append("Suggestion: Ensure the value is relevant to the resolution and well-justified.")
#         else:
#             feedback.append("Value: No explicit value stated. Consider stating a clear value.")
    
#     elif section_name == "Value Criterion":
#         if content:
#             feedback.append(f"Value Criterion: The case uses '{sentences[0].strip()}' as the criterion.")
#             feedback.append("Suggestion: Verify that the criterion effectively measures the value and is well-explained.")
#         else:
#             feedback.append("Value Criterion: No explicit criterion stated. Consider stating a clear value criterion.")
    
#     elif section_name == "Definitions":
#         feedback.append("Definitions: The case provides definitions for key terms.")
#         feedback.append("Suggestion: Ensure all crucial terms are defined and sources are credible.")
    
#     elif section_name == "Contentions":
#         claims, evidence = analyze_argument_structure(content)
#         feedback.append(f"The case presents {len(claims)} main claims and {len(evidence)} pieces of evidence.")
#         feedback.append("Suggestion: Ensure each claim is well-supported by evidence and reasoning.")
        
#         for i, (sentence, prediction) in enumerate(zip(sentences, predictions)):
#             if prediction == 'argument':
#                 feedback.append(f"Strong argument: {sentence}")
#             elif prediction == 'evidence':
#                 feedback.append(f"Good evidence provided: {sentence}")
#             elif prediction == 'conclusion':
#                 feedback.append(f"Clear conclusion: {sentence}")
#             else:
#                 feedback.append(f"Consider improving this point: {sentence}")
    
#     return feedback

# def analyze_argument_structure(text):
#     doc = nlp(text)
#     claims = []
#     evidence = []
    
#     for sent in doc.sents:
#         if any(token.dep_ == "ROOT" and token.pos_ == "VERB" for token in sent):
#             claims.append(sent.text)
#         elif any(token.text.lower() in ["because", "since", "as", "therefore"] for token in sent):
#             evidence.append(sent.text)
    
#     return claims, evidence

# nlp = spacy.load("en_core_web_sm")


# # model.py

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.ensemble import RandomForestClassifier
# from .text_processing import preprocess_text

# def extract_features(processed_text):
#     sentences = [' '.join(sentence) for sentence in processed_text]
#     vectorizer = TfidfVectorizer(max_features=1000)
#     features = vectorizer.fit_transform(sentences)
#     return features, vectorizer

# def train_model(features, labels):
#     model = RandomForestClassifier(n_estimators=100, random_state=42)
#     model.fit(features, labels)
#     return model

# def analyze_debate_case(text, model, vectorizer):
#     sections = extract_sections(text)
#     feedback = []

#     for section_name, section_content in sections.items():
#         processed_text = preprocess_text(section_content)
#         features = vectorizer.transform([' '.join(sentence) for sentence in processed_text])
#         predictions = model.predict(features)
        
#         section_feedback = analyze_section(section_name, section_content, predictions)
#         feedback.extend(section_feedback)
    
#     return feedback

# def extract_sections(text):
#     sections = {
#         "Resolution": "",
#         "Value": "",
#         "Value Criterion": "",
#         "Definitions": "",
#         "Contentions": ""
#     }
    
#     current_section = None
#     for line in text.split('\n'):
#         if "resolved:" in line.lower():
#             current_section = "Resolution"
#         elif "value" in line.lower() and "criterion" not in line.lower():
#             current_section = "Value"
#         elif "criterion" in line.lower():
#             current_section = "Value Criterion"
#         elif "definition" in line.lower():
#             current_section = "Definitions"
#         elif "contention" in line.lower():
#             current_section = "Contentions"
        
#         if current_section:
#             sections[current_section] += line + "\n"
        
#         if any(phrase in line.lower() for phrase in ["thus, i affirm", "thus, i negate", "i strongly urge", "for all these reasons"]):
#             break
    
#     return sections

# def analyze_section(section_name, content, predictions):
#     feedback = []
#     sentences = sent_tokenize(content)
    
#     if section_name == "Resolution":
#         feedback.append(f"Resolution: {sentences[0].strip()}")
#         feedback.append("Suggestion: Ensure the resolution is clearly stated and addresses the topic.")
    
#     elif section_name == "Value":
#         if content:
#             feedback.append(f"Value: The case presents '{sentences[0].strip()}' as the value.")
#             feedback.append("Suggestion: Ensure the value is relevant to the resolution and well-justified.")
#         else:
#             feedback.append("Value: No explicit value stated. Consider stating a clear value.")
    
#     elif section_name == "Value Criterion":
#         if content:
#             feedback.append(f"Value Criterion: The case uses '{sentences[0].strip()}' as the criterion.")
#             feedback.append("Suggestion: Verify that the criterion effectively measures the value and is well-explained.")
#         else:
#             feedback.append("Value Criterion: No explicit criterion stated. Consider stating a clear value criterion.")
    
#     elif section_name == "Definitions":
#         feedback.append("Definitions: The case provides definitions for key terms.")
#         feedback.append("Suggestion: Ensure all crucial terms are defined and sources are credible.")
    
#     elif section_name == "Contentions":
#         claims, evidence = analyze_argument_structure(content)
#         feedback.append(f"The case presents {len(claims)} main claims and {len(evidence)} pieces of evidence.")
#         feedback.append("Suggestion: Ensure each claim is well-supported by evidence and reasoning.")
        
#         for i, (sentence, prediction) in enumerate(zip(sentences, predictions)):
#             if prediction == 'argument':
#                 feedback.append(f"Strong argument: {sentence}")
#             elif prediction == 'evidence':
#                 feedback.append(f"Good evidence provided: {sentence}")
#             elif prediction == 'conclusion':
#                 feedback.append(f"Clear conclusion: {sentence}")
#             else:
#                 feedback.append(f"Consider improving this point: {sentence}")
    
#     return feedback

# def analyze_argument_structure(text):
#     doc = nlp(text)
#     claims = []
#     evidence = []
    
#     for sent in doc.sents:
#         if any(token.dep_ == "ROOT" and token.pos_ == "VERB" for token in sent):
#             claims.append(sent.text)
#         elif any(token.text.lower() in ["because", "since", "as", "therefore"] for token in sent):
#             evidence.append(sent.text)
    
#     return claims, evidence

# nlp = spacy.load("en_core_web_sm")