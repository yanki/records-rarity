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
			% if type is "own":
				<li>Own Record</li>
			% end
		</ol>
		% if type is "own":
			<form action="/records/ownrecord" method="post">
				<div class="form-group">
					<div class="row">
						<div class="col-md-3">
							<label>Quality:</label>
							<input type = "text" class="form-control" id="quality" name="quality" required>
						</div>
						<div class="col-md-3">
							<label>Price:</label>
							<input type = "number" step="any" class="form-control" id="price" name="price" value="0.0" required>
						</div>
					</div>
					<div class="row">
						<div class="col-md-3">
							<label>Tradability:</label>
							<input type="checkbox" name="trade" id="trade">
						</div>
						<div class="col-md-3">
							<label>Sellable:</label>
							<input type="checkbox" name="sell" id="sell">
						</div>
					</div>
					<br>
					<input class="form-control" type="hidden" name="v_id" id="v_id" value="{{v_id}}">
					<input class="form-control" type="hidden" name="type" id="type" value="add">
					<button type="submit" class="btn btn-primary">Submit</button>
				</div>
			</form>
		% end
		% if type is "wish":
			% for list in wishlists:
				<form action="/records/ownwish" method="post">
					<div class="form-group">
						<input class="form-control" type="hidden" name="wishlist" id="wishlist" value="{{list[0][0]}}">
						<input class="form-control" type="hidden" name="v_id" id="v_id" value="{{v_id}}">
						<input class="form-control" type="hidden" name="type" id="type" value="add">
						<button type="submit" class="btn btn-info">{{list[0][0]}}</button>
					</div>
				</form>
				<br>
			% end
		% end
		<br>	

	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
	<script src="../js/bootstrap.min.js"></script>
	</div>
    

</body>
</html>