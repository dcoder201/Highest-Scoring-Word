def high(x):
    # Code here
    words = x.split()
    scores = [sum(ord(c) - ord('a') + 1 for c in w) for w in words]
    return words[scores.index(max(scores))]
  
def basic_test_cases():
        test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
        test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
        test.assert_equals(high('take me to semynak'), 'semynak')
        test.assert_equals(high('aa b'), 'aa')
        test.assert_equals(high('b aa'), 'b')
        test.assert_equals(high('bb d'), 'bb')
        test.assert_equals(high('d bb'), 'd')
        test.assert_equals(high("aaa b"), "aaa")
