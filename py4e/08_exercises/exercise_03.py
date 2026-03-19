# Rewrite the guardian code, in the above example, without two `if` statements.
# Instead, use a compound, logical, expression, using the `or` logical operator,
# with a single `if` statement.

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    words = line.split()
    # guardian in a compound statement - left side of the `or` operator; this is an example of 'short-circuit evaluation'
    if len(words) < 3 or words[0] != 'From': continue
    print(words[2])
