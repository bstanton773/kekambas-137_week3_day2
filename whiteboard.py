# Given a word w 
# and some text t, find whether w is in t. 
# For example: 
#w="nest", t="I built a nest and tested it."
#output: "here"
#example 2:
#w="runs", t="The dog"
#output: "not here"
#Example 3: 
#w="April", t="april showers bring may flowers"
#output: "not here"


# eval the word (w) and see if its in text (t)

# value_if_true if condition else value_if_false
def solution(word, text):
    # if word in text:
    #     return 'here' 
    # else:
    #     return 'not here'
    return 'here' if word in text else 'not here'
