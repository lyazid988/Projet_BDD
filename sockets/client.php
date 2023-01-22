<?php require_once('shelper.php');

$sockethelper = new sockethelper('localhost',8000);

$sockethelper->send_data('Hello World');

echo $sockethelper->read_data();

$sockethelper->close_socket();

?>