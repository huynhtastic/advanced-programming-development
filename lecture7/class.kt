data class Person(
  var firstname: String,
  var lastname: String,
  var age: Int)


fun maximum(first: Int = 3, second: Int = 4): Int {
    return if (first > second) {
        first
    } else {
        second
    }
}

var max = maximum(1, 2)

fun maximum(first: Int, second: Int): Int =
    if (first > second) {
        first
    } else {
        second
    }

fun maximum(first: Int, second: Int) =
    if (first > second) {
        first
    } else {
        second
    }

fun maximum(first: Int, second: Int) =
    if (first > second) first else second

public class Person{
    private final String name;

    public Person(String name) [
        this.name = name;
    }

    public String getName() {
        return name;
    }
}

// translates to this in kotlin:

class Person (val name: String)

// data gives you equals, hashcode, and toString
