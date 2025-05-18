<?php
// Simple Calculator in PHP

function calculate($a, $b, $operator) {
    switch ($operator) {
        case '+':
            return $a + $b;
        case '-':
            return $a - $b;
        case '*':
            return $a * $b;
        case '/':
            return $b != 0 ? $a / $b : 'Division by zero error';
        default:
            return 'Invalid operator';
    }
}

// Example usage:
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $a = floatval($_POST['a']);
    $b = floatval($_POST['b']);
    $operator = $_POST['operator'];
    $result = calculate($a, $b, $operator);
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Simple PHP Calculator</title>
</head>
<body>
    <h2>Simple Calculator</h2>
    <form method="post">
        <input type="number" name="a" step="any" required>
        <select name="operator">
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">*</option>
            <option value="/">/</option>
        </select>
        <input type="number" name="b" step="any" required>
        <button type="submit">Calculate</button>
    </form>
    <?php if (isset($result)): ?>
        <h3>Result: <?php echo htmlspecialchars($result); ?></h3>
    <?php endif; ?>
</body>
</html>