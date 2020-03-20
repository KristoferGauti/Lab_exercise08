class NegativeError(Exception): pass

class Calculator(object):
    @staticmethod

    def Add(string):
        punctuations = ['!"#$%&\'(),./:;<=>?@[\\]^_`{|}~']
        is_negative = False
        replaced_string = ""

        if string == "":
            return 0
        
        if string[0] == "/":
            delimiter = string[2]
            if delimiter in punctuations or delimiter.isalpha() == True:
                replaced_string += ",".join(char for char in string if char.isdigit())

        if replaced_string == "":
            if "\n" in string:
                replaced_string += string.replace("\n",",")
            elif "-" in string:
                is_negative = True
                replaced_string += string
            else:
                replaced_string += string


        if replaced_string.isdigit():
            return int(replaced_string)

        elif len(replaced_string) > 1:
            replaced_string_list = replaced_string.split(",")
            int_list = [int(num) for num in replaced_string_list if int(num) <= 1000]

            if is_negative:
                negative_number = ""
                for num in int_list:
                    if num < 0:
                        negative_number += str(num) + ","

                raise NegativeError("Negatives not allowed: {}".format(negative_number[:-1]))
                    
                        

            
            return sum(int_list)

if __name__ == "__main__":
    calc = Calculator.Add("")
    