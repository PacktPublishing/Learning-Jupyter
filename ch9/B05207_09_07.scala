/* Scala pattern matching */
def matchTest(x: Any): Any = x match {
  case 7 => "seven"
  case "two" => 2
  case _ => "something"
}
val isItTwo = matchTest("two")
val isItTest = matchTest("test")
val isItSeven = matchTest(7)
