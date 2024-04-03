<?php

// Define a class
class MyClass {
    // Properties
    public $prop1 = "I'm a class property!";

    // Methods
    public function __construct() {
        echo 'The class "', __CLASS__, '" was initiated!'."\n";
    }

    public function __destruct() {
        echo 'The class "', __CLASS__, '" was destroyed.'."\n";
    }

    public function setProperty($newval) {
        $this->prop1 = $newval;
    }

    public function getProperty() {
        return $this->prop1 . "\n";
    }
}

// Create an object
$obj = new MyClass;

// Output class property
echo $obj->getProperty();

// Set new property value
$obj->setProperty("I'm a new property value!");

// Output class property again
echo $obj->getProperty();

?>

