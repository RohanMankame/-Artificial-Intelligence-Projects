
from fractions import Fraction

########################################################
### 1. Sequences
########################################################

def list_add(l1, l2):
    #get union of list and return
    AddList = set(l1) | set(l2)
    return list(AddList)



def dict_extend(dict1, dict2):
    #Add key/value from first dictionary if key is also in dictionary2 combine its value it key
    Dict = {}
    for key, value in dict1.items():
        if key not in dict2:
            Dict[key] = [value]
        else:
            Dict[key] = [value, dict2[key]]
    #add remaining key/value from dictionary2
    for key, value in dict2.items():
        if key not in Dict:
            Dict[key] = value
    return Dict

def dict_invert(dct):
    #For every value in dct make new key in new Dict{} being the value and set its value as key. value is in Dict already as key edit its value to add the other key.
    Dict = {}
    for key, value in dct.items():
        if value in Dict:
            Dict[value] = [Dict[value], key]
        else:
            Dict[value] = key
    return Dict


def dict_nested(lst):
    #stop adding keys as values and return once no more keys
    if not lst:
        return {}
    # keep adding next key as value to previous from the first key
    return {lst[0]: dict_nested(lst[1:])}



########################################################
### 2. List Comprehension
########################################################


def list_product(l1, l2):
    productList = []
    for x in l1:
        for y in l2:
            productList.append([x,y])
    return productList


#NOT WORKING ALL CASES
def list_flatten(list_of_seqs):
    FList = []
    for sublist in list_of_seqs:
        for item in sublist:
            FList.append(item)
    return FList

#NOT WORKIN
def dict_to_table(dct):
    pass


def nlargest(dct, n):
    # If n is > number of items then return all
    items =list(dct.items())
    if n> len(items):
        return dct

    # go trough and add max items to result dictionary, use first item compared to second and replace if larger, next take out of current input dct and keep going for n items
    DICT = {}
    for x in range(n):
        # Start with the first item as the maximum
        max_item = items[0]
        for item in items:
            # compare values
            if item[1]> max_item[1]:
                max_item = item
        # Add the max to DICT and then remove the max item curr dct
        DICT[max_item[0]] =max_item[1]
        items.remove(max_item)

    return DICT

def unique_values(list_of_dicts):
    List =[]
    #find and add unique values to our new List
    for dct in list_of_dicts:
        for value in dct.values():
            # If value not currently in list then add it else leave it
            if value not in List:
                List.append(value)

    return List


########################################################
### 3. Other algorithms
########################################################

def encode(input):
    ENC =""
    num=1
    for i in range(len(input)):
        # if input[i] and input[i+1] equal then count how many char the same till unequal char in string
        if i < len(input) - 1 and input[i]== input[i +1]:
            num= num+ 1
        else:
            # Append num and char to encode string then reset num for next char
            ENC = ENC + f"{num}{input[i]}"
            num = 1
    return ENC

def decode(input):
    Dec =""
    num =""
    for char in input:
        # if digit note its value
        if char.isdigit():
            num = char
        else:
            # char * count and add to decode string, then reset num for next char
            Dec +=int(num)*char
            num =""
    return Dec

def camel_case(var_name):
    # Split words where _
    word = var_name.split('_')
    # No words
    if not word:
        return ""
    #first word starts in lower case
    StrC = word[0].lower()
    # all other words start with a capital latter
    for i in range(1, len(word)):
        StrC += word[i].capitalize()
    return StrC


########################################################
### 4. Fraction class
########################################################

class Fraction():
    
    def __init__(self, numerator, denominator=1):
        # error if div by 0
        if denominator == 0:
            raise ZeroDivisionError(f"{numerator}/{denominator}")
        self.numerator = numerator
        self.denominator = denominator

    def get_fraction(self):
        return (self.numerator, self.denominator)

    def __neg__(self):
        # - numerator, keep denominator same
        return Fraction(-self.numerator, self.denominator)

    def __add__(self, other):
        if isinstance(other, Fraction):
            # if same denominator just goto add numerators
            if self.denominator == other.denominator:
                NewNumerator = self.numerator + other.numerator
                NewDenominator = self.denominator
            else:
                # else recalc numerator & denominator, then +
                NewNumerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
                NewDenominator = self.denominator * other.denominator

            return Fraction(NewNumerator, NewDenominator)

    def __sub__(self, other):
        if isinstance(other, Fraction):
            #if same denominator just goto add numerators
            if self.denominator == other.denominator:
                NewNumerator = self.numerator - other.numerator
                NewDenominator = self.denominator
                # else recalc numerator & denominator, then -
            else:
                NewNumerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
                NewDenominator = self.denominator * other.denominator

            return Fraction(NewNumerator, NewDenominator)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            #numerator*numerator over denominator*denominator
            NewNumerator = self.numerator * other.numerator
            NewDenominator = self.denominator * other.denominator

            return Fraction(NewNumerator, NewDenominator)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            #swap 2nd fractions numerator and denominator then multiply
            NewNumerator = self.numerator * other.denominator
            NewDenominator = self.denominator * other.numerator


            if NewDenominator == 0:
                raise ZeroDivisionError(f"{NewNumerator}/{NewDenominator}")
            else:
                return Fraction(NewNumerator, NewDenominator)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            #if equal true, else false
            if (self.numerator == other.numerator) and (self.denominator == other.denominator):
                return True
            else:
                return False


    def __lt__(self, other):
        if isinstance(other, Fraction):
            # set denominator equal then compare numarators
            NewNumerator1 = self.numerator * other.denominator
            NewNumerator2 = other.numerator * self.denominator
            NewDenominator = self.denominator * other.denominator
            if NewNumerator1 < NewNumerator2:
                return True
            else:
                return False

    def __call__(self):
        return self.numerator / self.denominator



#printing memory address instead of string value
def __str__(self):
    return (self.numerator+"/"+self.denominator)



