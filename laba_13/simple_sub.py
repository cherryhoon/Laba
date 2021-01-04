# bab ---> bzb
# bcb ---> bzb
# bxb ---> bzb
REGEXP_1 = r'[^b]'
REGEXP_1_REPL = 'z'

# abcXYZabc   ---> abcabc
# XaYbZcWaM   ---> abca
# abc XYZabc  ---> abc abc
REGEXP_2 = r'[A-Z]+'
REGEXP_2_REPL = ''

# abcABCabc  ---> abcABCabc
# DaEbFcAaB  ---> abcAaB
# abcXYZabc  ---> abcXYZabc
# bab ---> bzb
# bcb ---> bzb
# bxb ---> bzb
REGEXP_1 = r'[^b]'
REGEXP_1_REPL = 'z'

# abcXYZabc   ---> abcabc
# XaYbZcWaM   ---> abca
# abc XYZabc  ---> abc abc
REGEXP_2 = r'[A-Z]+'
REGEXP_2_REPL = ''

# abcABCabc  ---> abcABCabc
# DaEbFcAaB  ---> abcAaB
# abcXYZabc  ---> abcXYZabc
# XaYbZcZaY  ---> XaYbZcZaY
# DXEYFZabc  ---> XYZabc
# ADBECFXYZ  ---> ABCXYZ
REGEXP_3 = r'D|E|F'
REGEXP_3_REPL = ''

# abc0abc   ---> abcabc
# 1a2b3c4   ---> abc
# a123!@#bc ---> abc
REGEXP_4 = r'\d|@|#|!'
REGEXP_4_REPL = ''

# a,b,c d,e,f      ---> a_b_c_d_e_f
# abc!@#a          ---> abc___a
# abc!@#,./abc abc ---> abc______abc_abc
REGEXP_5 = r',|!|@|#|\/|\s|\.'
REGEXP_5_REPL = '_'

# a abc aa bb  ---> a aa bb
# a def dd fd  ---> a dd fd
# x xy xyz yz  ---> x xy yz
# x xyz xyz yz ---> x yz
REGEXP_6 = r'\w{3}\s'
REGEXP_6_REPL = ''

# AabcdZ ---> abcd
# BabcdC ---> BabcdC
# aAbZcd ---> aAbZcd
# AabcdY ---> abcdY
# BabcdZ ---> Babcd
REGEXP_7 = r'^A|Z$'
REGEXP_7_REPL = ''

# a b c  ---> a b c
# a  b c ---> a b c
# d    f ---> d f
REGEXP_8 = r'\s+'
REGEXP_8_REPL = r' '

# a ab abc abcd ab ---> a ab ab
# a xyz xyz a      ---> a a
# d xy xyza a      ---> d xy a
# a xyzzy b        ---> a xyzzy b
REGEXP_9 = r'\b\w{3,4}\s'
REGEXP_9_REPL = '' a ab ab
# a xyz xyz a      ---> a a
# d xy xyza a      ---> d xy a
# a xyzzy b        ---> a xyzzy b
REGEXP_9 = r'\b\w{3,4}\s'
REGEXP_9_REPL = ''