/* Scala immutability */
def calculate (amount: Int): Int = { amount = amount + 1; return amount; }
var balance = 100
val result = calculate(balance);