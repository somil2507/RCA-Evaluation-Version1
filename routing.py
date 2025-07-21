def assign_team(root_cause, matrix):
    try:
        return matrix.get(root_cause, {}).get("default", "General Support Team")
    except:
        return "Unmapped - Needs Manual Review"

