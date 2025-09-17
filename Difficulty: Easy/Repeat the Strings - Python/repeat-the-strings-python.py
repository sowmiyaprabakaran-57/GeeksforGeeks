# Function to join given strings
def combo_string(a, b):

    # your code here
    if len(a)>len(b):
        longer=a
        short=b
    else:
        longer=b
        short=a
    return short + longer + short