class Calculator(object):
    @staticmethod

    def Add(string):
        replaced_string = ""
        if "\n" in string:
            replaced_string += string.replace("\n",",")
        else:
            replaced_string += string

        if replaced_string == "":
            return 0

        elif replaced_string .isdigit():
            return int(replaced_string )

        elif len(replaced_string ) > 1:
            replaced_string_list = replaced_string.split(",")
            int_list = [int(num) for num in replaced_string_list]
            return sum(int_list)

if __name__ == "__main__":
    calc = Calculator()
    calc.Add("1\n2,3")

        