def countDog(a_string):
    a_string_smallcase = a_string.lower()
    dog_count = 0
    while (len(a_string_smallcase)> 0) and (a_string_smallcase.find('dog') > -1):
        dog_pos = a_string_smallcase.find('dog')
        if dog_pos >= 0:
            dog_count += 1
            a_string_smallcase = a_string_smallcase[dog_pos+3:]
    return dog_count
countDog('This dog runs faster than the other dog dude!')