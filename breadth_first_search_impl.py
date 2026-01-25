def gen_parentheses(pairs):
    if not isinstance(pairs, int):
        return 'The number of pairs should be an integer'
    if pairs < 1:
        return 'The number of pairs should be at least 1'
    # (current_string, open_count, close_count)
    queue = [('', 0, 0)]
    result = []
    while queue:
        # Processing logic will go here
        # Get the oldest state and unpack its values
        current, opens_used, closes_used = queue.pop(0)
        # If the string is the target length, it's finished!
        if len(current) == 2 * pairs:
            result.append(current)
        else:
            # Try adding an opening parenthesis
            if opens_used < pairs:
                queue.append((current + '(', opens_used + 1, closes_used))
            if closes_used < opens_used:
                queue.append((current + ')', opens_used, closes_used + 1))

    return result
print(gen_parentheses(1))
print("---")
print(gen_parentheses(2))
print("---")
print(gen_parentheses(3))
