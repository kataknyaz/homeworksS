class BaseIntents:
    def __init__(self):
        self.intents = [
            {
                "name": "greeting",
                "examples": ["привет", "здравствуй", "хай"],
                "responses": ["Привет! Чем могу помочь?"]
            },
            {
                "name": "help",
                "examples": ["помощь", "что ты умеешь", "команды"],
                "responses": ["Я могу генерировать изображения. Просто скажи: 'Нарисуй картину'."]
            }
        ]