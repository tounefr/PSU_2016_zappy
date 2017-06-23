
class Util:

    @staticmethod
    def isNumeric(s):
        if len(s) == 0:
            return False
        for _ in range(0, len(s)):
            if not _ >= 0 and _ <= 9:
                return False
        return True