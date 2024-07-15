<!DOCTYPE html>
<html>
<head>
    <title>Customer Segmentation</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="container">
        <h1>Customer Segmentation</h1>
        <form action="/segmentation" method="post">
            <input type="submit" value="Segment Customers">
        </form>
    </div>
</body>
</html>
