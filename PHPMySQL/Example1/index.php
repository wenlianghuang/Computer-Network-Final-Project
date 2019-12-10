<!DOCTYPE html>
<html>
    <meta charset="utf-8"/>
    <title>Blog File MySql</title>
<head>
<body>
    <?php
    $dbh = new PDO("mysql:host=127.0.0.1;dbname=testdb","root","Matt@Wenliang0422");
    if(isset($_POST['btn'])){
        $name = $_FILES['myfile']['name'];
        $type = $_FILES['myfile']['type'];
        $data = file_get_contents($_FILES['myfile']['tmp_name']);
        $stmt = $dbh->prepare("insert into myblog(name,mime,data) values(?,?,?)");
        $stmt->bindParam(1,$name);
        $stmt->bindParam(2,$type);
        $stmt->bindParam(3,$data);
        $stmt->execute();
    }
    ?>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="myfile"/>
        <button name="btn">Upload</button>
    </form>
    <p></p>
    <ol>
    <?php
    $stat = $dbh->prepare("select * from myblog");
    $stat->execute();
    while($row = $stat->fetch()){
        echo "<li><a target='_blank' href='view.php?id=".$row['id']."'>".$row['name']."</a><br/>
        <embed src='data:".$row['mime'].";base64,".base64_encode($row['data'])."' width='200'/></li>";        
    }
    ?>
    </ol>
</body>
</head>
</html>
