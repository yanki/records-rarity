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
		<ol class="breadcrumb">
			<li><a href="/records/login">Home</a></li>
			% if info is None:
				<li>New User</li>
			% else:
				<li>Edit User</li>
			% end
		</ol>
		% if info is None:
			<form action="/records/insertuser" method="post">
				<div class="form-group">
					<label>Full Name:</label>
					<input type = "text" class="form-control" id="name" name="name" required>
					<br>
					<label>UserName:</label>
					<input type = "text" class="form-control" id="username" name="username" required>
					<br>
					<label>Password:</label>
					<input type = "text" class="form-control" id="password" name="password" required>
					<br>
					<label>E-Mail:</label>
					<input type = "text" class="form-control" id="email" name="email" required>
					<br>
					<label>Zipcode:</label>
					<input type = "text" class="form-control" id="zip" name="zip">
					<br>
					<label>Street:</label>
					<input type = "text" class="form-control" id="street" name="street">
					<br>
					<label>City:</label>
					<input type = "text" class="form-control" id="city" name="city">
					<br>
					<label>State:</label>
					<input type = "text" class="form-control" id="state" name="state">
					<br>
					<button type="submit" class="btn">Submit</button>
				</div>
			</form>
		% end
		% if info is not None:
			<form action="/records/updateuser" method="post">
				<div class="form-group">
					<label>Full Name:</label>
					<input type = "text" class="form-control" id="name" name="name" value="{{info['name']}}">
					<br>
					<label>UserName:</label>
					<input type = "text" class="form-control" id="username" name="username" value="{{info['username']}}" readonly>
					<br>
					<label>Password:</label>
					<input type = "text" class="form-control" id="password" name="password" value="{{info['password']}}">
					<br>
					<label>E-Mail:</label>
					<input type = "text" class="form-control" id="email" name="email" value="{{info['email']}}">
					<br>
					<label>Zipcode:</label>
					<input type = "text" class="form-control" id="zip" name="zip" value="{{info['zipcode']}}">
					<br>
					<label>Street:</label>
					<input type = "text" class="form-control" id="street" name="street" value="{{info['street']}}">
					<br>
					<label>City:</label>
					<input type = "text" class="form-control" id="city" name="city" value="{{info['city']}}">
					<br>
					<label>State:</label>
					<input type = "text" class="form-control" id="state" name="state" value="{{info['state']}}">
					<br>
					<button type="submit" class="btn">Submit</button>
				</div>
			</form>
		% end
		<br>	

	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
	<script src="../js/bootstrap.min.js"></script>
	</div>
    

</body>
</html>