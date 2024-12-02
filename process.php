<?php
$user_input = isset($_GET['gifts']) ? $_GET['gifts'] : '';
$user_input = escapeshellarg($user_input);
$command = "python3 gift_selector.py $user_input";
$output = shell_exec($command);
echo "<pre>$output</pre>";
?>
