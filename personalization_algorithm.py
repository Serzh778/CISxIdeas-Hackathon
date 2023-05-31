class GoxipPersonalizationAlgorithm:
    def __init__(self):
        self.preferences = {}

    def update_preferences(self, user_id, activity):
        # track the activity from the website
        # update the database of user preferences based on the database

        # Split the activity string by the colon ":" separator
        activity_parts = activity.split(":")

        if len(activity_parts) >= 3:
            # Extract the key and value from the activity string
            key = activity_parts[1].strip()
            value = activity_parts[2].strip()

            # Update the user preferences dictionary
            if user_id not in self.preferences:
                self.preferences[user_id] = {}

            if key not in self.preferences[user_id]:
                self.preferences[user_id][key] = []

            self.preferences[user_id][key].append(value)


    def retrieve_preferences(self, user_id):
        # Retrieve user preferences for the given user_id
        return self.preferences.get(user_id, {})
