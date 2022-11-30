def show_employee(name, salary="50000"):
    output= name+ " makes "+ "$"+str (salary)+ " a year."
    print(output)

show_employee('John Smith', 60000)
show_employee('Emily Currington')
show_employee('David Mcclain', 65000)


# Define shout_echo
def shout_echo(word1, echo="1"):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo('Hey')

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo =shout_echo('Hey', echo='5')

# Print no_echo and with_echo
print(no_echo)
print(with_echo)