import calculating_with_functions


Test.describe('Basic Tests')
Test.assert_equals(seven(times(five())), 35)
Test.assert_equals(four(plus(nine())), 13)
Test.assert_equals(eight(minus(three())), 5)
Test.assert_equals(six(divided_by(two())), 3)