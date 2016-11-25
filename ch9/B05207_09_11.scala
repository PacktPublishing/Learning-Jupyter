/* Scala traits */
trait Color {
    def isRed(): Boolean
}
class Red extends Color {
    def isRed() = true
}
class Blue extends Color {
    def isRed() = false
}
var red = new Red();
var blue = new Blue();
red.isRed()
blue.isRed()