def average(dictionary:dict)->float:
    """
    Receives a dictionary with names and grades and returns the
    class average.
    """
    if not dictionary:
        return 0.0

    total_sum = sum(dictionary.values())
    count = len(dictionary)
    
    average = total_sum / count
    return (average)
