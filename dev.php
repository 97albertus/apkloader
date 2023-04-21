<?php

// Import any necessary libraries or classes here
if (isset($_GET['link'])) {
    $link = $_GET['link'];
    $encoded_link = urlencode($link);
    
    $url = "http://localhost:5000/get-link?input_string=/getapk/?app=$encoded_link";
    $result = file_get_contents($url);
    echo $result;
} else {
    echo "Error: Missing arguments";
}// Additional code can go here if needed

?>