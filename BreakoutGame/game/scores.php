<html>
<head>
    <link rel="stylesheet" type="text/css" href="https://codepen.io/alassetter/pen/cyrfB.css"/>
	<meta charset="utf-8" />
	<title>Breakout Game Project Scores</title>
	<meta name="viewport" content="initial-scale=1.0; maximum-scale=1.0; width=device-width;">
</head>

<body>
<div class="table-title">
<h3>Breakout Game Project Scores</h3>
</div>
<table class="table-fill">
<thead>
<tr>
<th class="text-left">Player</th>
<th class="text-left">Score</th>
</tr>
</thead>
<tbody class="table-hover">

<?php
$score_string = file_get_contents("highscore.dat");
$scores = explode(PHP_EOL, $score_string);

foreach($scores as $line) {
    if(!ctype_alnum($line[0])) break;
    $name = substr($line, 0, strpos($line, "::"));
    $score = (int)substr($line, strpos($line, "::") + 2, strrpos($line, "::") - strpos($line, "::") - 1);
    echo "<tr>";
    echo '<td class="text-left">'.$name.'</td>';
    echo '<td class="text-left">'.$score.'</td>';
    echo "</tr>";
}
?>

</tbody>
</table>
</body>
</html>