<!doctype html PUBLIC "-//w3c//dtd xhtml 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang='en'>

<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Records Rarity</title>
    <link href="../css/bootstrap.min.css" rel="stylesheet">
    <link href="../css/mystyler.css" rel="stylesheet">
    <link href="signin.css" rel="stylesheet">
    <style type="text/css">

    </style>
</head>

<body bgcolor=096AA2>
<!-- -->
	<div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
		<div class="container">
			<table>
				<tr>
					<div class="navbar-header">
						<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
							<span class="sr-only">Toggle navigation</span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
						</button>
						<a class="navbar-brand" href="./login.php">Admins</a>
					</div>
					<div class="collapse navbar-collapse">
						<ul class="nav navbar-nav">
							<li class="active">
								<a href="index.html">Initial Project Page</a>
							</li>
							<li>
								<a href="/index.html">Mikita Yankouski</a>
							</li>
							<li>
								<a href="">Sean Rowe</a>
							</li>
							<li>
								<a href="">Cullen Satterfield</a>
							</li>
						</ul>
					</div>
					<!--/.nav-collapse -->
				</tr>
			</table>
		</div>
	</div>
	<div class="container" id="maincontainer">
		<hr />
		<table>
			<button><a href="/records/newuser">Register</a></button></br>
			% if iterate is "yes":
				<tr>{{vinyls}}</tr>
			% end
		</table>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
	<script src="../js/bootstrap.min.js"></script>
	</div>
    

</body>
</html>