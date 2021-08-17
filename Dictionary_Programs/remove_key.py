class Remove:
    def __init__(self):
        pass

    def remove_key_from_dictionary(self):
        """
        removing key from a dictionary
        """
        people = {1: {'name': 'berlin', 'age': '43', 'gender': 'Male'},
                  2: {'name': 'rachel', 'age': '22', 'gender': 'Female'}}

        print(people[1].pop("name"))
        print(people)


if __name__ == "__main__":
    remove = Remove()
    remove.remove_key_from_dictionary()
