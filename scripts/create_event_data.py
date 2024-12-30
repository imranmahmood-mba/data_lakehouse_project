"""Module providing function to write list of dictionary to JSON"""
import json
from scripts.create_user import User

NUM_OF_EVENTS = 1000
FILE_NAME = "imdb_event_data.json"


def create_events(num_of_events: int) -> list[dict]:
    """
    Create a list of event data.

    Args:
        num_of_events (int): Number of events to create.

    Returns:
        list[dict]: A list of dictionaries representing user events.
    """
    list_of_events = []
    for _ in range(num_of_events):
        new_user = User.create_random_user().to_dict()
        list_of_events.append(new_user)
    return list_of_events


def write_data_to_json(event_data: list[dict], file_name: str) -> None:
    """
    Write event data to a JSON file.

    Args:
        event_data (list[dict]): List of dictionaries representing event data.
        file_name (str): Path to the output JSON file.
    """
    with open(file_name, "w", encoding="utf-8") as final:
        json.dump(event_data, final)


def main() -> None:
    """
    Main function to create events and write them to a JSON file.
    """
    events = create_events(NUM_OF_EVENTS)
    write_data_to_json(events, FILE_NAME)


if __name__ == '__main__':
    main()
