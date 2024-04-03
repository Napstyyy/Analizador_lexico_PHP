<?php

// Define a multidimensional associative array
$student_info = array(
    array("name" => "John", "age" => 20, "grade" => "A"),
    array("name" => "Emily", "age" => 22, "grade" => "B"),
    array("name" => "Michael", "age" => 21, "grade" => "C")
);

// Iterate through the array and print student information
foreach ($student_info as $student) {
    echo "Name: " . $student["name"] . ", Age: " . $student["age"] . ", Grade: " . $student["grade"] . "\n";
}

// Define a function to calculate the average of an array of numbers
function calculate_average($numbers) {
    $sum = array_sum($numbers);
    $count = count($numbers);
    return $sum / $count;
}

// Test the function
$numbers = array(10, 20, 30, 40, 50);
echo "Average: " . calculate_average($numbers) . "\n";

// Define a string with escape characters
$escaped_string = "This is a \"quoted\" string.";

// Print the string
echo $escaped_string . "\n";

// Define a string with special characters
$special_string = "Hello\tworld\n";

// Print the string
echo $special_string;

?>

