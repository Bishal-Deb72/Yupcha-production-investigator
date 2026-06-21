import re


def reconstruct_timeline(logs: str):

    timeline = []

    lines = logs.split("\n")

    for line in lines:

        match = re.search(
            r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})',
            line
        )

        if match:

            timestamp = match.group(1)

            event = line.replace(timestamp, "").strip()

            timeline.append(
                {
                    "time": timestamp,
                    "event": event
                }
            )

    timeline.sort(key=lambda x: x["time"])

    return timeline