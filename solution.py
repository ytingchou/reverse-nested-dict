def reverse(input_dict, reversed_dict = None):
    [[key, value]] = input_dict.items()

    if not isinstance(value, dict):
        return {value: {key: reversed_dict}}
    else:
        return reverse(
            value,
            {key: reversed_dict} if reversed_dict is not None else key
        )
