spidy_tuple = ('Peter', 'Parker', 21)

spidy_dict = {
    'first_name': 'Peter',
    'last_name': 'Parker',
    'age': 21
}

print(spidy_dict)


def print_user(user: dict) -> None:
    expected_keys = ['first_name', 'last_name', 'age']
    for k in expected_keys:
        if k not in user:
            # Log the missing key.
            # Raise a proper error.
            # Or return None
            return None

    print(f'My name is {user["first_name"]} {user["last_name"]} and I am {user["age"]} years old')


print_user(spidy_dict)
