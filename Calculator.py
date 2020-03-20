class NegativeError(Exception): pass

class Calculator(object):
    @staticmethod

    def Add(string):
        is_negative = False
        replaced_string = ""
        
        if "\n" in string:
            replaced_string += string.replace("\n",",")
        elif "-" in string:
            is_negative = True
            replaced_string += string

        else:
            replaced_string += string

        if replaced_string == "":
            return 0

        elif replaced_string .isdigit():
            return int(replaced_string)

        elif len(replaced_string) > 1:
            replaced_string_list = replaced_string.split(",")
            int_list = [int(num) for num in replaced_string_list if int(num) <= 1000]

            if is_negative:
                negative_number = ""
                for num in int_list:
                    if num < 0:
                        negative_number += str(num) + " "

                raise NegativeError("Negatives not allowed: {}".format(negative_number))
                    
                        

            
            return sum(int_list)

if __name__ == "__main__":
    Calculator.Add("-1,2")