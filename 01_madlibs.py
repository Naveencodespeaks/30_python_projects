def get_inputs(word_type: str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input

noun1 = get_inputs("noun")
adj1 = get_inputs("adjctive")
verb = get_inputs("verb")
noun2 = get_inputs("noun")
verb2 = get_inputs("verb2")


story = f"""
print('\n')
Once upon a time, there was a {noun1} who loved to {verb} all day.
{noun2}: "what are you doing?"
{noun1}: "I'm just {verb}ing, what's the big deal?"
{noun1}:"I guess you're right. maybe I should take a break."
{noun2}: "That's probably a good idea. why don't we go {verb2} insted?"

And so,{noun2} and the {noun1} went off to {verb2} and had a great time
The end.

"""

print(story)