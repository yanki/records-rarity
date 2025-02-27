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
    <style type="text/css">

    </style>
</head>

<body>
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
	<div class="container login_cont" id="maincontainer">
		</br>
		<div class="text-center">
			% if error is "yes":
				<div class="alert alert-danger" role="alert">
				Wrong Username/Password Combination!
				</div>
			% end
			% if error is "success":
				<div class="alert alert-success" role="alert">
				User Created!
				</div>
			% end
			<div class="row">
				<form role="form-horizontal" name="loginForm" id="loginForm" action="/records/login" method="post" class="centered">
					<legend>Please Log In:</legend>
					<table>
						<tr>
							<div class="control-group col-xs-4 col-xs-offset-4">
								<label class="control-label">Name: </label>
								<div class="controls">
									<input class="form-control" type="text" placeholder="Username" id="username" name="username">
								</div>
							</div>
						</tr>
						<tr>
							<div class="control-group col-xs-4 col-xs-offset-4">
								<label class="control-label">Pass: </label>
								<div class="controls">
									<input class="form-control" type="text" placeholder="Password" id="password" name="password">
								</div>
							</div>
						</tr>
						<tr>
							<div class="col-xs-4 col-xs-offset-4">
								</br>
								<button type="submit" class="btn btn-primary" name="login" value="Log In">Log In</button>
							</div>
						</tr>
					</table>
				</form>
			</div>
			</br>
			<form action="/records/newuser" role="form" name="register" id="register" method="get">
				<button type="submit" class="btn btn-primary" name="register">Register</button>
			</form>
		</div>
	</div>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    

</body>
</html>