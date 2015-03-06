<?php
$opts = array('http' =>
  array(
    'user_agent' => 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'
  )
);
$context = stream_context_create($opts);
$url = $_GET['url'];
echo (string)$url
//$url = 'http://en.wikipedia.org/w/api.php?action=opensearch&search=yolo';
echo file_get_contents($url);
?>
