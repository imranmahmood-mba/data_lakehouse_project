from random import randint, choice
import datetime
import time


class User:
    """
    Represents a user with an ID, action, and event timestamp.
    """
    def __init__(self, user_id: int, user_action: str,
                event_time: datetime.datetime):
        """
        Basic constructor for the User class.

        Args:
            user_id (int): Unique user ID.
            user_action (str): Action performed by the user.
            event_time (datetime.datetime): Timestamp of the event.
        """
        self.user_id = user_id
        self.user_action = user_action
        self.event_time = event_time

    @staticmethod
    def create_random_user(start_id=100000000, end_id=999999999,
                           actions=None, start_year=2010, end_year=2025):
        """
        Factory method to create a random user with default parameters.

        Args:
            start_id (int): Start range for generating user IDs.
            end_id (int): End range for generating user IDs.
            actions (List[str], optional): List of possible user actions.
            start_year (int): Start year for the timestamp range.
            end_year (int): End year for the timestamp range.

        Returns:
            User: object contains the randomly generated user data
        """
        actions = actions or ['signed up', 'started film', 'finished film']
        user_id = randint(start_id, end_id)
        user_action = choice(actions)
        start_timestamp = int(time.mktime(datetime.date(start_year, 1, 1).timetuple()))
        end_timestamp = int(time.mktime(datetime.date(end_year, 12, 31).timetuple()))
        random_timestamp = randint(start_timestamp, end_timestamp)
        event_time = datetime.datetime.fromtimestamp(random_timestamp)
        return User(user_id, user_action, event_time)

    def to_dict(self):
        """Saves user data to a dictionary
        Args:
            User: takes the class instance as argument
        Returns:
            dict: dictionary containing user data
        """
        return {
            'user_id': self.user_id,
            'user_action': self.user_action,
            'event_time': self.event_time
        }
