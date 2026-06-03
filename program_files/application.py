#アプリケーションオーケストレーション



from app.context import AppContext

class Application:

    def __init__(self):
        self.context = AppContext(user_id = "default")
