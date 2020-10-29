"""
Module to validate the work flow and prepare execution plan and resolve deps and execure forward.
"""
import json


def lambda_handler(event, context):
    """

    :param event:
    :param context:
    :return:
    """

    for message in event["Records"]:
        print(message)
        # Parse body from message
        message_from_sns = json.loads(message["body"])

        instance_id = message_from_sns.get("Message")
        print(f"Processing Instance #{instance_id}")

        # TODO: Validate data from given instance_id Above!