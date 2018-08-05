fun <T> Collection<T>.joinToString(collection: Collection<T>,
        separator: String=", ",
        prefix: String="",
        postfix: String=""
): String {
    var result = StringBuilder(prefix)
    for ((index, element) in collection.withIndex()) {
        if (index > 0) result.append(separator)
        result.append(element)
    result.append(postfix)
    }
    return result.toString()
}

// calling the extension function
println(listOf(1,2,3).joinToString()

// receiver type = this(receiver object)
fun String.lastChar(): Char = this.get(this.length-1)

// leave out this
package strings
fun String.lastChar(): Char = get(length-1)

import strings.lastChar
val c == "Kotlin".lastChar()


