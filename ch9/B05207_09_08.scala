/* Scala case classes */
def carType(car: Car) = car match {
  case Car("Honda", "Accord") => "sedan"
  case Car("GM", "Denali") => "suv"
  case Car("Mercedes", "300") => "luxury"
  case Car("Buick", "LeSabre") => "sedan"
  case _ => "Car: is of unknown type"
}
val typeOfBuick = carType(buickLeSabre)