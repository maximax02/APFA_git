function displayDiv(elementValue) {
	var x = document.getElementById('opcion').value;
	if (x == 0){
		document.getElementById('divEmail').style.display = 'block';
		document.getElementById('divSocio').style.display = 'none';
	}else{
		document.getElementById('divEmail').style.display = 'none';
		document.getElementById('divSocio').style.display = 'block';
	}
}
		