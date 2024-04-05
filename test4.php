<?php
// Database connection settings
$host = 'localhost';
$dbname = 'cms';
$username = 'root';
$password = '';

// Establish database connection
try {
    $conn = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
    die();
}

// User authentication
function authenticateUser($username, $password) {
    global $conn;
    $query = "SELECT * FROM users WHERE username = :username AND password = :password";
    $stmt = $conn->prepare($query);
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':password', $password);
    $stmt->execute();
    return $stmt->fetch(PDO::FETCH_ASSOC);
}

// CRUD operations for articles
function createArticle($title, $content) {
    global $conn;
    $query = "INSERT INTO articles (title, content) VALUES (:title, :content)";
    $stmt = $conn->prepare($query);
    $stmt->bindParam(':title', $title);
    $stmt->bindParam(':content', $content);
    return $stmt->execute();
}

function getArticle($id) {
    global $conn;
    $query = "SELECT * FROM articles WHERE id = :id";
    $stmt = $conn->prepare($query);
    $stmt->bindParam(':id', $id);
    $stmt->execute();
    return $stmt->fetch(PDO::FETCH_ASSOC);
}

function updateArticle($id, $title, $content) {
    global $conn;
    $query = "UPDATE articles SET title = :title, content = :content WHERE id = :id";
    $stmt = $conn->prepare($query);
    $stmt->bindParam(':title', $title);
    $stmt->bindParam(':content', $content);
    $stmt->bindParam(':id', $id);
    return $stmt->execute();
}

function deleteArticle($id) {
    global $conn;
    $query = "DELETE FROM articles WHERE id = :id";
    $stmt = $conn->prepare($query);
    $stmt->bindParam(':id', $id);
    return $stmt->execute();
}

// Example usage
$user = authenticateUser('admin', 'password123');
if ($user) {
    // User authenticated, perform CRUD operations
    createArticle('Sample Article', 'This is a sample article content.');
    $article = getArticle(1);
    echo "Article Title: " . $article['title'] . "<br>";
    echo "Article Content: " . $article['content'] . "<br>";
    updateArticle(1, 'Updated Article', 'This article has been updated.');
    deleteArticle(1);
} else {
    echo "Authentication failed!";
}
?>
