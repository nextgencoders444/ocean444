<?php

$conn = new mysqli("localhost","root","","mydb");

if($conn->connect_error){
die("Connection failed");
}

$location = $_POST['location'];
$temp = $_POST['temperature'];
$salinity = $_POST['salinity'];
$fish = $_POST['fish_count'];
$biodiversity = $_POST['biodiversity'];

$sql = "INSERT INTO ocean_data(location,temperature,salinity,fish_count,biodiversity)
VALUES('$location','$temp','$salinity','$fish','$biodiversity')";

$conn->query($sql);

echo "Data saved successfully";

$conn->close();

?>