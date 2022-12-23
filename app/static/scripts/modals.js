// Obtengo las imagenes y hago que muestre el modal cuando se le hace click
const imagenes = document.querySelectorAll('.imagen-lista');
imagenes.forEach(imagen => {
  imagen.addEventListener('click', event => {
	  const dataModal = imagen.getAttribute('data-modal');
	  const modal = document.getElementById(dataModal);
	  modal.style.display = "block";
  });
});

// Obtengo los botones de cancelar para que cierren el modal
const cancelbtns = document.querySelectorAll('.cancelbtn');
cancelbtns.forEach(button => {
  button.addEventListener('click', event => {
	const dataModal = button.getAttribute('data-modal');
	const modal = document.getElementById(dataModal);
	modal.style.display = "none";
  });
});

// Obtengo los botones de continuar para que vaya a la pagina de votar
const continuebtns = document.querySelectorAll('.continuebtn');
continuebtns.forEach(button => {
  button.addEventListener('click', event => {
	const link = button.getAttribute('data-link');
	window.location.href = link;
  });
});