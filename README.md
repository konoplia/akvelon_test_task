# akvelon_test_task

The NumberFormatter class has a parse_int method that takes a string as 
input. assuming all characters in the string are between 0 and 9, returns an integer. If an argument other than a string integer is passed to the method input, a warning is returned.

Sample: “123345” -> 123345, “-123345” -> -123345, “+1” -> 1
, 1 ->'The argument must only be a string', "12ef"-> 'Wrong symbol in string'