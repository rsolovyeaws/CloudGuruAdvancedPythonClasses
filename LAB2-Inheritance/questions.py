from random import sample

class Question:
    def __init__(self, question_text, choices, correct_choice):
        self.question_text = question_text
        self.choices = choices
        self.correct_choice = str(correct_choice)
        self.selected_answer = None
    
    def __str__(self) -> str:
        output = self.question_text + "\n\n"
        for index, choice in enumerate(sample(self.choices, len(self.choices))):
            output += f"{index + 1}. {choice}\n"
        
        return output
    
    def select(self, choice) -> None:
        self.selected_answer = str(choice)
        
    def grade(self) -> bool:
        return self.correct_choice == self.selected_answer
       
class TrueFalseQuestion(Question):
    def __init__(self, question_text, correct_choice) -> None:
        question_text = self.__prefix_if_necessary(question_text)
        super().__init__(question_text, [True, False], correct_choice)
        
    def __prefix_if_necessary(self, question_text) -> str:
        if question_text.lower().startswith('true') or question_text.lower().startswith('false'):
            return question_text
        else:
            return f"True/False: {question_text}"

class MultipleSelectQuestion(Question):
    def __init__(self, question_text, choices, correct_choices) -> None:
        question_text = self.__add_suffix(question_text, correct_choices)
        super().__init__(question_text, choices, correct_choices)
        self.correct_choice = self.__sorted_string_list(correct_choices)
    
    def __add_suffix(self, question_text, correct_choices) -> str:
        return f"{question_text} (select {len(correct_choices)})"
    
    def __sorted_string_list(self, list_of_items):
        return list(sorted(map(str, list_of_items)))
    
    def select(self, choices) -> None:
        self.selected_answer = self.__sorted_string_list(choices)