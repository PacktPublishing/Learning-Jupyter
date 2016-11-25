/* Scala array operations */
import scala.io.Source;

val filename = "train.csv"
/* PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked */
/* 1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S */

var males = 0
var females = 0
var males_survived = 0
var females_survived = 0
for (line <- Source.fromFile(filename).getLines) {
    var cols = line.split(",").map(_.trim);
    var sex = cols(5);
    if (sex == "male") { 
        males = males + 1;
        if (cols(1).toInt == 1) {
            males_survived = males_survived + 1;
        }
    }
    if (sex == "female") { 
        females = females + 1; 
        if (cols(1).toInt == 1) {
            females_survived = females_survived + 1;
        }
    }    
}
val mens_survival_rate = males_survived.toFloat/males.toFloat
val womens_survival_rate = females_survived.toFloat/females.toFloat