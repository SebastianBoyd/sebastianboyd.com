<?php
	$ipaddress = $_SERVER['REMOTE_ADDR']."\r\n";

	$file = 'logfile.txt';

	$fp = fopen($file, 'a');

	fwrite($fp, $ipaddress);

	fclose($fp);
?>
<!doctype html>
<html>
        <head>
                <title>&#127843;</title>
                <script src="advert.js"></script>
		<script src="detect.js"></script>
		<script src="/Analytics.js">
        </head>
        <body>
        </body>
</html>
