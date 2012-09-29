import datetime

class entry:
    def __init__(self, line):
        items = line.split("&")

        # date string to datetime object
        self.datetime = datetime.datetime.strptime(items[0], "%Y-%m-%dT%H:%M:%S+00:00")
        self.user_id = self.get_user_id(items).strip()
        self.body = self.get_body(items)
        self.genre = self.get_genre(items).strip()

    def get_user_id(self, items):
        for item in items:
            if "login=" in item:
                return item[6:]
        return ""

    def get_body(self, items):
        for item in items:
            if "text=" in item:
                return item[5:]
        return ""

    def get_genre(self, items):
        for item in items:
            if "genre=" in item:
                return item[6:]
        return ""

