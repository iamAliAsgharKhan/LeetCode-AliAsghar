class Solution:
    def mySqrt(self, x: int) -> int:
        #Babylonian method
        
        # Initialize a variable to store the square root
        sqrt = 1
        # Set a small error tolerance
        tolerance = 0.000001
        # Iterate until the difference between the square of the current guess and the input number is less than the tolerance
        while abs(sqrt*sqrt - x) > tolerance:
            # Use Newton's method to update the guess for the square root
            sqrt = 0.5 * (sqrt + x/sqrt)
        return int(sqrt)