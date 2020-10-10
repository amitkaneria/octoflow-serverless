"""
A Trigger work flow module which triggers and generates instance according to the user's input
"""

import json
from typing import Tuple
from utils import Response


def lambda_handler(event, context):
    """

    :param event:
    :param context:
    :return:
    """
    # TODO: Update this stub and add Steps to execute user's input

    # Step 1: Parse JSON data into dict
    data = None
    try:
        data = json.loads(event.get("body"))
    except Exception as exc:
        print(f"Exception caught! :{exc}")
        return Response({"message": "Failed to parse Json data", "reason": f"{exc}"})

    # Step 2: Validate Json

    # Step 3: Persist data!

    # Step 4: Send to SNS Topic for further processing
    print(event)
    return Response({"message": "I've got your back!", "input_data": data})
