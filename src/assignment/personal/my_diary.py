# user_access_details = [
#     {"username": "jboy", "password": "pass0000"},
#     {"username": "maxim", "password": "king1111"},
#     {"username": "major", "password": "prince1234"}
# ]
#
#
# def lst_checker(username, password):
#     for user in user_access_details:
#         if user["username"] == username and user["password"] == password:
#             return True
#     return False


# user_access_details = {
#     "favourite_food": ["rice", "beans", "dodo"],
#     "favourite_player": {"Arsenal": "Bukayo", "Chelsea": "Lukaku", "Dekanorb": "Ladi"},
#     "favourite_ girl": "Deborah",
#     "favourite_music": ["last last", "buga", "kukere"],
#     "favourite_language": {"Programming": "Python", "Dialect": "Kalabari", "Slang": "Breakfast"}
# }
#
#
# def type_checker(types):
#     for value in user_access_details.values():
#         if type(value) == types:
#             print(value)


contact_details = {
    "Fullname": "Ernest Ehigiator",
    "address": ["Yaba", "Shomolu", "Ikeja"],
    "Phone_number": ["07081649157"],
    "School": {"semicolon", "alt_school"}
}


def update(phone_number):
    for key, value in contact_details.items():
        if key == str("address") and type(value) == list:
            return value.append(phone_number)


# print(lst_checker("jboy", "pass0000"))

if __name__ == '__main__':
    update("London")
    print(contact_details)
