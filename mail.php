<!DOCTYPE html>
<html>
    
    <head>
          

<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
	<title>Mail</title>

  <style type="text/css">
    
  .body{width:100%;height:100%;border:5px solid red; } 
  </style>
</head>
<body>
<?php

        $BillNO=$_GET['BillNO'];
       $name=$_GET['name'];
        $email=$_GET['email'];
       $Mobile=$_GET['Mobile'];
       $Products=$_GET['Products'];
       $Date=$_GET['Date'];
       $Totalsamt=$_GET['Totalamt'];



       $myemail="www.armannakhwa99@gmail.com";
  	   $subject="Bill Management System";
  	   $msg="<div style='width:100%;height:100%;border:5px solid red; padding:12px;'>".nl2br($_GET['message'])."</div>";
       

  	  
$myfile = fopen("bills.txt", "a") or die("Unable to open file!");
$txt = $_GET['message'];
fwrite($myfile, $txt);
fclose($myfile);



//For Localhost Mail 
  	  if(mail($email,$subject,$msg,"Content-Type: text/html; charset=UTF-8\r\n"))
          {
          echo "send";
          }
          else
          {
          echo "not send";
          }



//for 000webhots mail
          /*
$fromname="Bill Management System@armannakhwa.cf";
$toemail=$email;
$usubject=$subject;
$umsg=$msg;
echo "<div style=display:none>";
include($_SERVER['DOCUMENT_ROOT']."/mail api/index.php");
echo "</div>";

*/



# Bill No,Customer Name,Email,Mobile No,Products,Date
$st = fopen("billdata.csv", "a");
$data=$BillNO.','.$name.','.$email.','.$Mobile.','.$Products.','.$Totalsamt.','.$Date."\n";

  fwrite($st,$data);
  fclose($st);

?>


<div id='bill'>
<?php echo $msg ?>
</div>

        