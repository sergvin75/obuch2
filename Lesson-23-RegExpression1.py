import re

mytext =    "Vasya aaaaaaaaa 1972, Kolya - 19872: Olesya 1981, aaaaaaa@intel.com, "\
            "bbbbbbbbb@intel.com, Petya gggggggggg, 1992, cccccccccc@yahoo.com,  "\
            "dddddddddd@intel.com, vasya@yandex.net, hello hello, Misha #43 1984, "\
            "Vladimir 1977, Irina , 2001, annnnnnn@intel.com, eeeeeeeee@yandex.com,"\
            "oooooooooo@hotmai.gov, ggggggggggg@gov.gov, tutututgiv.hot"

"""
\d = Any digit 0-9
\D = Any non DIGIT
\w = Any Alphabet symbol [A-Z a-z]
\W = Any non Alphabet symbol
\s = breakspace
\S = non breakspace

[0-9]{3} = ищем цифры от 0 до 9 и таких должно быть 3
\w{6} - слова из 6 алфавитных символа
\w{6}\s - слова из 6 алфавитных символа и в конце пробел
[A-Z][a-z]+ - первый символ [A-Z], [a-z]+ - сколько угодно маленьких символов
\w+\.\w+ - слово точка слово



"""


textlookfor = r"@\w+\.\w+"
allresults = re.findall(textlookfor, mytext)

print(allresults)


