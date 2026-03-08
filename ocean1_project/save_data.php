<?php

$location = $_POST['location'];
$temperature = $_POST['temperature'];
$species = $_POST['species'];

$conn = new mysqli("localhost","root","","ocean_db");

if($conn->connect_error){
die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO ocean_data (location, temperature, species)
VALUES ('$location', '$temperature', '$species')";

if($conn->query($sql) === TRUE){
echo "Data Submitted Successfully";
}
else{
echo "Error: " . $conn->error;
}

$conn->close();

?>