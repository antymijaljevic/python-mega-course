def sentance_maker(phrase):
    interrogatives = ('what', 'when', 'where', 'who', 'whom', 'which', 'whose', 'why', 'how')
    capitalized = phrase.capitalize()
    
    if phrase.lower().startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


results = []

while True:
    user_input = input("Say something: ")
    if user_input == "/end":
        break
    else:
        results.append(sentance_maker(user_input))


print(" ".join(results))