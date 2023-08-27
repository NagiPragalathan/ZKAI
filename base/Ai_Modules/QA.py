import numpy as np
import nltk as nlp
import random
import re
from .Content_gen import respond_to_input
import random
import nltk
from nltk.corpus import wordnet as wn


def clean_text(text):
    lines = text.strip().split('\n')  # Remove leading/trailing whitespaces and split by lines
    cleaned_lines = []

    for line in lines:
        words = line.split()
        if len(words) >= 6:  # Only include lines with 6 or more words
            cleaned_lines.append(" ".join(words))  # Join words back into a string

    cleaned_text = "\n".join(cleaned_lines)  # Join lines back into a single string
    return cleaned_text

class MCQTest:

    def __init__(self, data, noOfQues):
        self.question_pattern = [
            "What does {} refer to?",
            "Which of the following best describes {}?",
            "How is {} typically used?",
            "Which term is most closely related to {}?",
            "What is a common application of {}?",
            "Is it true that {}?",
            "Is {} considered a best practice?",
            "Is {} commonly used in the industry?",
            "Is {} generally considered obsolete?",
            "Does {} have multiple components?",
            "Is {} related to security risks?",
            "What is the purpose of the code `{}`?",
            "What will the code `{}` output?",
            "What does the code `{}` do?",
            "Which programming language likely uses the code `{}`?",
        ]
        
        self.grammar = r"""
            CHUNK: {<NN>+<IN|DT>*<NN>+}
            {<NN>+<IN|DT>*<NNP>+}
            {<NNP>+<NNS>*}
        """
        self.summary = data
        self.noOfQues = noOfQues

    def extract_code(self):
        return re.findall(r'`(.*?)`', self.summary)
    
    def generate_test(self):
        sentences = nlp.sent_tokenize(self.summary)
        cp = nlp.RegexpParser(self.grammar)
        question_answer_dict = dict()

        for sentence in sentences:
            tagged_words = nlp.pos_tag(nlp.word_tokenize(sentence))
            tree = cp.parse(tagged_words)
            for subtree in tree.subtrees():
                if subtree.label() == "CHUNK":
                    temp = ""
                    for sub in subtree:
                        temp += sub[0]
                        temp += " "
                    temp = temp.strip()
                    if temp not in question_answer_dict:
                        question_answer_dict[temp] = sentence

        code_snippets = self.extract_code()
        for code in code_snippets:
            question_answer_dict["CODE: " + code] = "This is a code snippet: `" + code + "`"

        if len(question_answer_dict) == 0:
            return "No keywords found to generate questions."

        keyword_list = list(question_answer_dict.keys())
        question_answer = list()

        for _ in range(int(self.noOfQues)):
            rand_num = np.random.randint(0, len(keyword_list))
            selected_key = keyword_list[rand_num]
            answer = question_answer_dict[selected_key]
            
            if "CODE: " in selected_key:
                question_format = self.question_pattern[11:]
                selected_key = selected_key.replace("CODE: ", "")
            elif "Is " in selected_key or "Does " in selected_key:
                question_format = self.question_pattern[5:11]
            else:
                question_format = self.question_pattern[:5]
            
            rand_num = np.random.randint(0, len(question_format))
            question = question_format[rand_num].format(selected_key)
            
            is_true_false = "Is " in question or "Does " in question
            
            if is_true_false:
                options = ["True", "False"]
                correct_answer = random.choice(options)
            else:
                wrong_answers = random.sample(keyword_list, 3)
                while selected_key in wrong_answers:
                    wrong_answers = random.sample(keyword_list, 3)
                
                options = [answer] + [question_answer_dict[k] for k in wrong_answers]
                random.shuffle(options)
                correct_answer = options.index(answer)
            
            question_answer.append({
                "question": question, 
                "options": options, 
                "answer": correct_answer
            })
        
        return question_answer

def generate_mcq(text, num_questions=5):
    # Step 1: Tokenize Sentences
    sentences = nltk.sent_tokenize(text)
    
    questions = []
    for sentence in sentences:
        # Step 2: Identify Keywords
        words = nltk.word_tokenize(sentence)
        tagged_words = nltk.pos_tag(words)
        nouns = [word for word, tag in tagged_words if tag in ["NN", "NNP", "NNS", "NNPS"]]
        
        if len(nouns) > 0:
            # Randomly select a noun to replace
            keyword = random.choice(nouns)
            
            # Step 3: Create Questions
            question = sentence.replace(keyword, "_____", 1)
            
            # Step 4: Generate Distractors
            distractors = set()
            for syn in wn.synsets(keyword):
                for lemma in syn.lemmas():
                    if lemma.name() != keyword:
                        distractors.add(lemma.name())
            distractors = list(distractors)[:3]  # Limiting to 3 distractors
            
            questions.append({
                'question': question,
                'answer': keyword,
                'options': [keyword] + distractors,
                'Correct Answer': 0
            })
            
        if len(questions) >= num_questions:
            break
            
    return questions


def generate_question(keyword):
    content = clean_text(respond_to_input(keyword))
    mcq_generator = MCQTest(content, 10)
    mcq_generator1 = generate_mcq(content, 10)
    questions = mcq_generator.generate_test()
    questions.extend(mcq_generator1)
    return questions

# questions = generate_question("what is python")
# print(questions)

# if questions == "No keywords found to generate questions.":
#     print(questions)
# else:
#     for i, q in enumerate(questions):
#         print(f"Question {i+1}: {q['Question']}")
#         for j, opt in enumerate(q['Options']):
#             print(f"Option {j+1}: {opt}")
#         if isinstance(q['Correct Answer'], int):
#             print(f"Correct Answer: Option {q['Correct Answer'] + 1}")
#         else:
#             print(f"Correct Answer: {q['Correct Answer']}")
#         print("----")
