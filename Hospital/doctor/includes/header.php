<style type="text/css">
a {
    text-decoration: none !important;
    color: white;
}</style>
<div class="header">
	<div class="headerleft">
		<b><a href="index.php">eHospital</a></b>
	</div>
	<div class="headerright">
		<b>
			<?php
			require '../includes/connect.php';
			require '../includes/users.php';
			doctordetails();
			 ?>
		</b>
	</div>
</div>