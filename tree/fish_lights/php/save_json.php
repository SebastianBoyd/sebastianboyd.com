<?php
$myFile = "../json/light.json";
$fh = fopen($myFile, 'w') or die("cant open file");
$stringData = $_GET["data"];
fwrite($fh, $stringData);
fclose($fh)
?>
