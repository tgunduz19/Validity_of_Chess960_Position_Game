
def is_valid(positions):

    """

    # --two bishops must start on differently colored squares.
    # --the king must be placed on a square between the two rooks.

    """


    total = 0

    for i in range(len(positions)):
        if positions[i] == "K":
            if "R" not in positions[0:i]:
                return False
            elif "R" not in positions[i:len(positions)]:
                return False

        elif positions[i] == "B":
            total += i

    if total % 2 == 0:
        return False

    return True



import codewars_test as test
from solution import is_valid

@test.describe("Sample tests")
def sample_tests():
    @test.it("The normal positions")
    def it_1():
        test.assert_equals(is_valid("RNBQKBNR"), True)

    @test.it("Rooks right next to king")
    def it_2():
        test.assert_equals(is_valid("QNNBBRKR"), True)

    @test.it("King on an edge")
    def it_3():
        test.assert_equals(is_valid("QRNNBBRK"), False)

    @test.it("King on other edge")
    def it_4():
        test.assert_equals(is_valid("KQRNNBBR"), False)

    @test.it("Bishops on same colour")
    def it_5():
        test.assert_equals(is_valid("QNBNBRKR"), False)



