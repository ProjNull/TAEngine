class Question:
    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get("ID")
        self.questions = str(kwargs.get("Question", "Hello World;"))
        if not self.questions.endswith(";"):
            self.questions += ";"
        self.questions = self.questions.split(";")
        for i, v in enumerate(self.questions):
            try:
                self.questions[i] = int(v)
            except ValueError:
                continue
        self.answers = kwargs.get("Answers")
        self.exec = [eval(i) for i in kwargs.get("Exec", "print;").split(";") if len(i)]

    def __call__(self):
        for c, a in zip(self.exec, self.questions):
            c(a)
        for k in self.answers.keys():
            print(f"> {k.title()}")
        answer = None
        while True:
            answer = input(">> ").lower()
            if answer not in self.answers.keys():
                print("Invalid choice!")
                continue
            break
        return self.answers.get(answer)
