#!/usr/bin/python3

"""
Generates personalized invitations
    
"""

import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitations
    
    """
    
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    """ Handle empty inputs """
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    """ Process each attendee """
    for index, attendee in enumerate(attendees, start=1):
        """ Copy attendee data to avoid modifying the original dictionary """
        attendee = attendee.copy()

        """ Check and replace missing data """
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            if key not in attendee or attendee[key] is None:
                print(f"Warning: Replacing missing data '{key}' with 'N/A'.")
                attendee[key] = "N/A"

        """ Replace placeholders in the template """
        try:
            invitation = template.format(**attendee)
        except KeyError as e:
            print(f"Warning: Unexpected missing data {e}")
            attendee[str(e)] = "N/A"
            invitation = template.format(**attendee)

        """ Write to file """
        output_file = f"output_{index}.txt"
        with open(output_file, "w") as file:
            file.write(invitation)

    print("Invitation files generated successfully.")

""" Example usage """
if __name__ == "__main__":
    """ Read the template from a file """
    with open('template.txt', 'r') as file:
        template_content = file.read()

    """ List of attendees """
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    """ Call the function with the template and attendees list """
    generate_invitations(template_content, attendees)