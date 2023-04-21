<?php

// Import any necessary libraries or classes here

$link = 'https://play.google.com/store/apps/details?id=com.kiloo.subwaysurf';
$encoded_link = urlencode($link);
$url = "http://localhost:5000/get-link?input_string=/getapk/?app=$encoded_link";
$result = file_get_contents($url);
echo $result;

// Additional code can go here if needed

?>
