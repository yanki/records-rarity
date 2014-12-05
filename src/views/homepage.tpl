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
    <div class="container" id="maincontainer">
        </br>
        <ol class="breadcrumb">
            <li><a href="/records/login">Home</a></li>
            % if type is "records":
                <li>Records</li>
            % end
            % if type is "wishlists":
                <li>Wishlists</li>
            % end
        </ol>
        <legend>{{details['username']}}</legend>
        <div class="media">
            <div class="row">
                <div class="col-xs-3">
                    <a class="media-left" href="#">
                        % if details['picture'] is None:
                            <img src="/default.jpg" alt="Profile" width="144" height="121">
                        % end
                    </a>
                </div>
                <div class="col-xs-4">
                    <h2><span class="label label-success">Rarity:</span> {{details['rarity']}}</h2>
                </div>
            </div>
            <div class="media-body">
                </br>
                <div class="row">
                    <div class="col-xs-3">
                        <h3 class="media-heading">
                            {{details['name']}}
                            <form role="form" name="recordsform" action="/records/editinfo" method="get">
                                <button type="submit" class="btn btn-default btn-sm">Edit Info</button>
                            </form>
                        </h3>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-2 mainbutton">
                        <form role="form" name="recordsform" action="/records/owned" method="get">
                            <button type="submit button" class="btn btn-primary">Records Owned</button>
                        </form>
                    </div>
                    <div class="col-md-2 mainbutton">
                        <form role="form" name="wishlistform" action="/records/wishlists" method="get">
                            <button type="submit button" class="btn btn-primary">Wish Lists</button>
                        </form>
                    </div>
                    
                        <form class="mainbutton" role="form" name="searchform" action="/records/search" method="post">
                            <div class="col-md-3">
                                <input class="form-control" type="text" name="items" id="items" placeholder="Find records...">
                            </div>
                            <div class="col-md-2">
                                <button type="submit" class="btn btn-info">Search</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
            % if type is "update":
                </br>
                <div class="alert alert-success" role="alert">
                    Your information is now updated!
                </div>
            % end
            % if contents is not None:
                <table class="table table-striped">
                    % if type is "records":
                        % if contents[1] is not None:
                            </br>
                            <div class="alert alert-success" role="alert">
                                Record deleted from your library.
                            </div>
                        % end
                        <legend>Owned Records</legend>
                        <thead>
                            <th>#</th>
                            <th>Artist</th>
                            <th>Album</th>
                            <th>Genre</th>
                            <th>Year</th>
                            <th>Rarity</th>
                            <th>Delete</th>
                        </thead>
                        <tbody>
                            % for index, item in enumerate(contents[0]):
                                <tr>
                                    <td>{{index+1}}</td>
                                    % for index, e in enumerate(item):
                                        % if index is not 0:
                                            <td>{{e}}</td>
                                        % end
                                    % end
                                    <td>
                                        <form role="form" action="/records/deleterecord" method="post">
                                            <input class="form-control" type="hidden" name="delete" id="delete" value="{{item[0]}}">
                                            <button type="submit" class="btn btn-danger">Delete</button>
                                        </form>
                                    </td>
                                </tr>
                            % end
                        </tbody>
                    % end
                    % if type is "owners":
                        <legend>Owners for {{contents[1]}}</legend>
                        <thead>
                            <th>Username</th>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Zip</th>
                            <th>City</th>
                            <th>State</th>
                            <th>Street</th>
                            <th>Quality</th>
                            <th>Price</th>
                            <th>Tradable</th>
                            <th>Sellable</th>
                        </thead>
                        <tbody>
                            % for item in contents[0]:
                                <tr>
                                    % for e in item:
                                        <td>{{e}}</td>
                                    % end
                                </tr>
                            % end
                            % if len(contents[0]) < 1:
                                <div class="alert alert-danger" role="alert">
                                    Nobody is willing to give up the album!
                                </div>
                            % end
                        </tbody>
                    % end
                    % if type is "wishlists":
                        <legend>Wishlists</legend>
                        <form role="form" action="/records/newwish" method="post">
                            <div class="createwish">
                                <div class="col-xs-4">
                                    <input class="form-control" type="text" name="wish" id="wish" required placeholder="Wishlist Name">
                                </div>
                                <div class="col-xs-2">
                                    <button type="submit" class="btn btn-warning">Create Wishlist</button>
                                </div>
                            </div>
                        </form>
                        <thead>
                            <th>#</th>
                            <th>Title</th>
                            <th>Remove</th>
                        </thead>
                        <tbody>
                            % for index, item in enumerate(contents[0]):
                                <tr>
                                    <td>{{index+1}}</td>
                                    % for e in item:
                                        <td>
                                            <form role="form" action="/records/getwish" method="post">
                                                <input class="form-control" type="hidden" name="wishname" id="wishname" value="{{e[0]}}">
                                                <button type="submit" class="btn btn-default">{{e[0]}}</button>
                                            </form>
                                        </td>
                                        <td>
                                            <form role="form" action="/records/removewishlist" method="post">
                                                <input class="form-control" type="hidden" name="wishname" id="wishname" value="{{e[0]}}">
                                                <button type="submit" class="btn btn-danger">Remove</button>
                                            </form>
                                        </td>
                                    % end
                                </tr>
                            % end
                        </tbody>
                    % end
                    % if type is "search":
                        <legend>{{contents[1]}}</legend>
                        <thead>
                            <th>#</th>
                            <th>Artist</th>
                            <th>Album</th>
                            <th>Genre</th>
                            <th>Year</th>
                            <th>Rarity</th>
                            <th>Ownership</th>
                        </thead>
                        <tbody>
                            % for index, item in enumerate(contents[0]):
                                <tr>
                                    <td>{{index+1}}</td>
                                    % for index, e in enumerate(item):
                                        % if index is not 0:
                                            <td>{{e}}</td>
                                        % end
                                    % end
                                    <td>
                                        <form role="form" action="/records/ownrecord" method="post">
                                            <input class="form-control" type="hidden" name="v_id" id="v_id" value="{{item[0]}}">
                                            <input class="form-control" type="hidden" name="type" id="type" value="details">
                                            <button type="submit" class="btn btn-success">Own</button>
                                        </form>
                                    </td>
                                </tr>
                            % end
                        </tbody>
                    %end
                </table>
                % if (contents[1] is not None) and type is "wishlists":
                    <table class="table table-striped">
                        <legend>{{contents[2]}}</legend>
                        <thead>
                            <th>#</th>
                            <th>Artist</th>
                            <th>Year</th>
                            <th>Album</th>
                            <th>Find</th>
                            <th>Remove</th>
                        </thead>
                        <tbody>
                            % for index, item in enumerate(contents[1]):
                                <tr>
                                    <td>{{index+1}}</td>
                                    <td>{{item[1]}}</td>
                                    <td>{{item[2]}}</td>
                                    <td>{{item[3]}}</td>
                                    <td>
                                        <form role="form" action="/records/findowners" method="post">
                                            <input class="form-control" type="hidden" name="albumname" id="albumname" value="{{item[3]}}">
                                            <button type="submit" class="btn btn-warning">Find</button>
                                        </form>
                                    </td>
                                    <td>
                                        <form role="form" action="/records/deletewish" method="post">
                                            <input class="form-control" type="hidden" name="delete" id="delete" value="{{item[0]}}">
                                            <button type="submit" class="btn btn-danger">Delete</button>
                                        </form>
                                    </td>
                                </tr>
                            % end
                        </tbody>
                    </table>
                % end
            % end
        </div>
    </div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>

</body>
</html>