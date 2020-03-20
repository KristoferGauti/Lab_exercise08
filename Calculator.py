class Calculator(object):
    def Add(string):
        if string == "":
            return 0
        elif string.isdigit():
            return int(string)
        elif len(string) > 1:
            string_list = string.split(",")
            int_list = [int(num) for num in string_list]
            return sum(int_list)