<?php
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if ($socket === false) {
    echo "socket_create() failed: reason: " . socket_strerror(socket_last_error()) . "\n";
}

$result = socket_connect($socket, '127.0.0.1', 8000);
if ($result === false) {
    echo "socket_connect() failed.\nReason: ($result) " . socket_strerror(socket_last_error($socket)) . "\n";
}

$message = "Hello, Server!";
socket_write($socket, $message, strlen($message));

$result = socket_read($socket, 1024);
echo $result;

socket_close($socket);
?>