<?php

// Define a function to calculate factorial
function factorial($n) {
    if ($n === 0) {
        return 1;
    } else {
        return $n * factorial($n - 1);
    }
}

// Calculate factorial of 5
$result = factorial(5);
echo "Factorial of 5 is: " . $result . "\n";

// Define a multi-dimensional array
$multi_array = array(
    "fruit" => array(
        "apple",
        "banana",
        "orange"
    ),
    "vegetable" => array(
        "carrot",
        "lettuce",
        "tomato"
    )
);

// Access elements of the multi-dimensional array
echo "Fruit: " . $multi_array["fruit"][0] . "\n";
echo "Vegetable: " . $multi_array["vegetable"][2] . "\n";

?>

