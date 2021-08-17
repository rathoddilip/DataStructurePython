class CheckKeys:
    def multiple_keys(self):
        """
        checking multiple keys exists in a dictionary
        using comparison operator
        """
        person = {"good": 1, "bad": 2, "excellent": 3}
        print(person.keys() >= {"good", "bad"})
        print(person.keys() >= {"excellent", "calm"})


if __name__ == "__main__":
    check_keys = CheckKeys()
    check_keys.multiple_keys()
