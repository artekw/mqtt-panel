
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="A layout example with a side menu that hides on mobile, just like the Pure website.">
    <title>mqtt-panel - {% block title %}{% end %}</title>
    
    <link rel="stylesheet" href="https://unpkg.com/purecss@0.6.2/build/pure-min.css" integrity="sha384-UQiGfs9ICog+LwheBSRCt1o5cbyKIHbwjWscjemyBMT9YCUMZffs6UqUTd0hObXD" crossorigin="anonymous">
    
    <link rel="stylesheet" href="https://code.cdn.mozilla.net/fonts/fira.css">
    
        <!--[if lte IE 8]>
            <link rel="stylesheet" href="/static/css/side-menu-old-ie.css">
        <![endif]-->
        <!--[if gt IE 8]><!-->
            <link rel="stylesheet" href="/static/css/side-menu.css">
        <!--<![endif]-->
    <!--[if lt IE 9]>
        <script src="http://cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7/html5shiv.js"></script>
    <![endif]-->

</head>
<body>

<div id="layout">
    <!-- Menu toggle -->
    <a href="#menu" id="menuLink" class="menu-link">
        <!-- Hamburger icon -->
        <span></span>
    </a>

    <div id="menu">
        <div class="pure-menu">
            <a class="pure-menu-heading" href="/">Panel</a>

            <ul class="pure-menu-list">
                <li class="pure-menu-item"><a href="/" class="pure-menu-link">Home</a></li>
                <li class="pure-menu-item"><a href="/message" class="pure-menu-link">Message</a></li>
                <li class="pure-menu-item"><a href="/settings" class="pure-menu-link">Settings</a></li>
            </ul>
        </div>
    </div>

    <div id="main">
        <div class="header">
            <h1>{% block page_title %}{% end %}</h1>
            <h2>{% block subtitle %}{% end %}</h2>
        </div>

        <div class="content">
            {% block content %}{% end %}
        </div>
    </div>
</div>




<script src="/static/js/ui.js"></script>

</body>
</html>
