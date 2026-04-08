def grade(task_type, predicted, actual):
    predicted = predicted.lower()
    actual = actual.lower()

    # spam / category
    if task_type in ["spam", "category"]:
        return 1.0 if predicted == actual else 0.0

    # reply (partial match)
    elif task_type == "reply":
        if actual in predicted:
            return 1.0
        elif any(word in predicted for word in actual.split()):
            return 0.5
        else:
            return 0.0