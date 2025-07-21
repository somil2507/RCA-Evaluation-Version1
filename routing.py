# def assign_team(root_cause, component, matrix):
#     try:
#         if component and component in matrix.get(root_cause, {}):
#             return matrix[root_cause][component]
#         return matrix[root_cause].get("default", "General Support Team")
#     except:
#         return "Unmapped - Needs Manual Review"
#
def assign_team(root_cause, matrix):
    try:
        return matrix.get(root_cause, {}).get("default", "General Support Team")
    except:
        return "Unmapped - Needs Manual Review"

