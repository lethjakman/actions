import json

class Actions:
    def __init__(self, conn):
        self.conn = conn
        self.cur = self.conn.cursor()

    def add_action(self, action_json):
        """ Accepts an action in the form of json and stores it
        Parameters:
        action_json (str): A json string of an action - {"action": "jump", "time": 100}
        """
        action_result = json.loads(action_json)

        # Fetching as an key like this will allow us to except when the key is missing
        action = action_result["action"]
        time = action_result["time"]
        self.cur.execute("INSERT INTO actions (action, time) VALUES (%s, %s)", [action, time])

    def get_stats(self):
        """ Returns an json string of average of times per action
        Returns:
        str: A json array of averaged actions and their types
        """
        # TODO: Remove. Just for testing purposes
        return '[{"action": "jump", "avg": 0}, {"action": "run", "avg": 75}]'
