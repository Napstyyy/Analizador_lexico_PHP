<?php

// Variable declaration (identifier, assignment)
$name = "Bard";

// Conditional statement (if, else)
if (strlen($name) > 5) {
  echo "Your name, $name, is quite long! <br>";
} else {
  echo "Hello, $name! <br>";
}

// Function call (function identifier, arguments)
$greeting = say_hello($name);
echo $greeting;

// Function definition (function declaration, function body)
function say_hello($targetName) {
  return "Greetings, " . $targetName . "!";
}

// Loop (for loop, increment)
for ($i = 0; $i < 3; $i++) {
  echo "Looping for the $i th time! <br>";
}

// Array declaration and access (array literal, index)
$fruits = array("apple", "banana", "orange");
echo "The second fruit is: " . $fruits[1] . "<br>";

// Comments (single line, multi-line)
// This is a single line comment

/** This is a multi-line comment
that can span multiple lines */

?>
