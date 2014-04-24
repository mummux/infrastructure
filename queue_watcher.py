import subprocess

import boto.sqs

import config
import textfiles

def start_watching(arguments):
    conn = boto.sqs.connect_to_region("us-east-1",
        aws_access_key_id=config.aws_access,
        aws_secret_access_key=config.aws_secret,
    )

    queue = conn.get_queue(config.aws_queue)
    
    while True:
        messages = queue.get_messages(wait_time_seconds=20)
        if not messages:
            continue

        print messages
        queue.clear()

        process = subprocess.Popen(["git", "pull"], cwd=config.textfiles)
        print process.communicate()

        textfiles.updated()

def main(arguments):
    if arguments.get("watch"):
        start_watching(arguments)
