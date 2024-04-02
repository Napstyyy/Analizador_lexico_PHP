<?php
include('database.php');
include('functions.php');

$products = getProducts();

?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tienda en línea</title>
</head>
<body>

<h1>Tienda en línea</h1>

<div class="products">
    <?php foreach ($products as $product): ?>
        <div class="product">
            <h2><?php echo $product['name']; ?></h2>
            <p>Precio: $<?php echo $product['price']; ?></p>
            <a href="product.php?id=<?php echo $product['id']; ?>">Ver detalles</a>
            <form action="cart.php" method="post">
                <input type="hidden" name="product_id" value="<?php echo $product['id']; ?>">
                <input type="submit" value="Agregar al carrito">
            </form>
        </div>
    <?php endforeach; ?>
</div>

</body>
</html>
