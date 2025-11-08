thonfrom datetime import datetime

def convert_timestamp(timestamp_str):
    """Converts a timestamp string to a datetime object."""
    return datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))

def format_timestamp(timestamp_str):
    """Formats timestamp to a human-readable string."""
    dt = convert_timestamp(timestamp_str)
    return dt.strftime("%Y-%m-%d %H:%M:%S")