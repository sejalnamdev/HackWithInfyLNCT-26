def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    return sum(c << i for i, c in enumerate(calorie))