/* Scala random numbers */
val r = new scala.util.Random
r.setSeed(113L)
val samples = 1000
var dice = new Array[Int](12)
for( i <- 1 to samples){
    var total = r.nextInt(6) + r.nextInt(6)
    dice(total) = dice(total) + 1
}
val max = dice.reduceLeft(_ max _)
for( i <- 0 to 11) {
    var str = ""
    for( j <- 1 to dice(i)/3) {
        str = str + "X"
    }
    print(i+1, str, "\n")
}