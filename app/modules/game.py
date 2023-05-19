import json
from .question import Question


class Game:
    def __init__(self, game_file: str) -> None:
        self.path = self._load(game_file)

    @staticmethod
    def _load(game_path: str) -> dict:
        questions: dict = {}
        with open(game_path, "r") as game:
            j = json.load(game)
            j.append({"ID": 0, "Question": 0, "Answers": {}, "Exec": "exit"})
            for data in j:
                a = data.get("Answers").copy()
                data["Answers"] = {}
                for k, v in a.items():
                    data["Answers"][k.lower()] = v
                    print(data["Answers"])
                questions[data.get("ID")] = Question(**data)
        return questions

    def __call__(self):
        # Start game
        self.work_path = 1
        self.running = True
        while self.running:
            try:
                self.work_path = self.path.get(self.work_path)()
            except Exception as e:
                print(f"Game Error: {type(e)} ~> {str(e)}")
                self.running = False
