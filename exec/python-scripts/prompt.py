def prompt_pattern():
    with open('./assets/default.pattern') as file:
        pattern = file.readline().strip()
    return pattern
