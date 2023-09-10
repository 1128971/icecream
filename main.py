import tkinter as tk

class QuestionnaireApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Опрос")

        self.questions = [
            "Выпускник школы или колледжа?",
            "Количество баллов ЕГЭ?",
            "В какие вузы вы еще подавали документы?",
            "Когда Вы приняли решение о том, что будете подавать документы в РУТ?",
            "На момент подачи документов вы знали о ВИШ?",
            "Изучали ли вы сайт Академии – rut.digital, когда подавали документы?",
            "Участвовали ли вы в каких-либо всероссийских конкурсах для школьников? Если 'да', то в каких? или напишите 'нет'",
            "Можете ли Вы сказать, что достаточно хорошо понимаете содержание своей будущей специальности?",
        ]
        self.answers = []

        self.current_question = 0

        self.question_label = tk.Label(root, text=self.questions[self.current_question])
        self.question_label.pack()

        self.answer_entry = tk.Entry(root)
        self.answer_entry.pack()

        self.next_button = tk.Button(root, text="Следующий вопрос", command=self.next_question)
        self.next_button.pack()

        self.result_label = tk.Label(root, text="", wraplength=300)
        self.result_label.pack()
        self.result_label["state"] = "disabled"

    def next_question(self):
        answer = self.answer_entry.get()
        self.answers.append(answer)
        self.answer_entry.delete(0, tk.END)

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question])
        else:
            self.next_button["state"] = "disabled"  # Отключаем кнопку "Следующий вопрос" после завершения опроса
            self.display_results()

    def display_results(self):
        result = "Ваши ответы:\n\n"
        for i, question in enumerate(self.questions):
            result += f"{question}: {self.answers[i]}\n"

        # Здесь вы можете добавить логику для анализа ответов и вывода результата

        self.question_label.destroy()
        self.answer_entry.destroy()
        self.result_label.config(text=result)
        self.result_label["state"] = "active"

if __name__ == "__main__":
    root = tk.Tk()
    app = QuestionnaireApp(root)
    root.mainloop()

