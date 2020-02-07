def func(s):
    """
    Args:
        s (str): String to check

    Returns:
        bool: The return value. True for success, False otherwise.
    """

    s = ''.join([c for c in s if c in '()[]{}'])
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return not s



class TestClass:

    def test_with_only_parentheses(self):
        string = "((5+3)*2+1)"
        assert(func(string)) == True

    def test_with_multiple_types_of_brackets(self):
        string = "{[(3+1)+2]+}"
        assert(func(string)) == True

    def test_wrong_sequence(self):
        string = "(3+{1-1)}"
        assert(func(string)) == False

    def test_longer_sequence(self):
        string = "[1+1]+(2*2)-{3/3}"
        assert(func(string)) == True

    def test_wrong_multiple_types_of_brackets(self):
        string = "(({[(((1)-2)+3)-3]/3}-3)"
        assert(func(string)) == False

    def test_without_any_brackets(self):
        string = "2+3"
        assert(func(string)) == True



if __name__ == '__main__':
    string = input("Enter a sequence to check: ")
    print(f'Result: {func(string)}')
