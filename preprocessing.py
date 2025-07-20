import re

def preprocess_log(log):
    log = log.lower()
    log = re.sub(r"[\W_]+", " ", log)
    return log.strip()