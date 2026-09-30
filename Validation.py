def valid_name(name):
    if name.strip() == "":
        return False

    return True


def valid_age(age):

    try:
        age = int(age)

        if age > 0 and age <= 120:
            return True

        return False

    except:
        return False


def valid_text(text):

    if text.strip() == "":
        return False

    return True
