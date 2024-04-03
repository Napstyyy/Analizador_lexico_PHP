<?php

// Define a simple array
$fruits = array("apple", "banana", "orange", "kiwi");

// Loop through the array and display each fruit
foreach ($fruits as $fruit) {
    echo "I like $fruit.\n";
}

// Define a function to calculate the square of a number
function square($num) {
    return $num * $num;
}

// Test the function
echo "Square of 5 is: " . square(5) . "\n";

// Define a string variable
$message = "Hello, world!";

// Print the message
echo $message . "\n";

// Demonstrate the use of heredoc syntax
$heredoc_example = <<<EOD
This is a heredoc string.
It can span multiple lines.
EOD;

echo $heredoc_example;

?>

