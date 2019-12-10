<?php
$dbh = new PDO("mysql:host=127.0.0.1;dbname=testdb","root","Matt@Wenliang0422");
$id = isset($_GET['id'])?$_GET['id'] : "";
$stat = $dbh->prepare("select * from myblog where id=?");
$stat->bindParam(1,$id);
$stat->execute();
$row = $stat->fetch();
header('Content-type:'.$row['mime']);
echo $row['data'];