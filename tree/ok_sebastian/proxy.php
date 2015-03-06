<?php
// File Name: proxy.php
if (!isset($_GET['url'])) {
    die(); // Don't do anything if we don't have a URL to work with
}
$url = urldecode($_GET['url']);
$url = 'http://' . str_replace('http://', '', $url); // Avoid accessing the file system
//echo file_get_contents($url); // You should probably use cURL. The concept is the same though
