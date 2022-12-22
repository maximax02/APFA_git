function showAlertAndRedirect(mensaje) {
	msj = unescape(mensaje)
	alert(msj);
	location.href = '/apfa/micuenta';
}