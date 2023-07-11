def extract_phones(input):
    if input[0]:
        return [tel.replace("tel:",'') for tel in input]
    else:
        return input

