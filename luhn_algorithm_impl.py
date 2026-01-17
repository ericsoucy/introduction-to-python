def verify_card_number(card_number: str) -> bool:
    """
    Verify if the provided card number is valid using the Luhn algorithm.

    Args:
        card_number (str): The card number to verify.
    Returns:
        bool: True if the card number is valid, False otherwise.
    """    # Remove any non-digit characters (like spaces or dashes)
    card_number = ''.join(filter(str.isdigit, card_number))

    # Check if the card number is empty or contains non-digit characters
    if not card_number.isdigit() or len(card_number) == 0:
        return  "INVALID!"

    total_sum = 0
    num_digits = len(card_number)
    parity = num_digits % 2

    for i, digit in enumerate(card_number):
        n = int(digit)

        # Double every second digit from the right
        if i % 2 == parity:
            n *= 2
            # If doubling results in a number greater than 9, subtract 9
            if n > 9:
                n -= 9

        total_sum += n

    # A valid card number will have a total sum that is a multiple of 10
    if total_sum % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"

print(verify_card_number('453914889')) # should return VALID!
print(verify_card_number('4111-1111-1111-1111')) # should return VALID!
print(verify_card_number('453914881')) # should return INVALID!
