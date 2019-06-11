class Actions:
    def __init__(self, conn):
        self.conn = conn
        pass

    def add_action(self, action_json):
        """ Accepts an action in the form of json and stores it
        Parameters:
        action_json (str): A json string of an action - {"action": "jump", "time": 100}
        """
        pass

    def get_stats(self):
        """ Returns an json string of average of times per action
        Returns:
        str: A json array of averaged actions and their types
        """
        pass

