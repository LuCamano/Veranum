// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
  
        form.classList.add('was-validated')
      }, false)
    })
  })()

var modalEliminarHotel = $("#modalEliminar")[0];
if (modalEliminarHotel) {
  modalEliminarHotel.addEventListener('show.bs.modal', function (event) {
    var button = event.relatedTarget; // Button that triggered the modal
    var idHotel = button.dataset.id; // Extract info from data-* attributes
    var nombreHotel = button.dataset.name; // Extract info from data-* attributes
    var modalBodySpan = $('#mensajeBorrar')[0];
    var botonConfirmar = $('#btnConfirmarBorrar')[0];

    modalBodySpan.textContent = nombreHotel;
    botonConfirmar.href = '/hoteles/eliminar-hotel/' + idHotel +'/' ;
})};

var modalEliminarTipo = $("#modalEliminarTipo")[0];
if (modalEliminarTipo) {
  modalEliminarTipo.addEventListener('show.bs.modal', function (event) {
    var button = event.relatedTarget; // Button that triggered the modal
    var idHotel = button.dataset.hid; // Extract info from data-* attributes
    var idtipo = button.dataset.tid; // Extract info from data-* attributes
    var nombreTipo = button.dataset.name; // Extract info from data-* attributes
    var modalBodySpan = $('#mensajeBorrar')[0];
    var botonConfirmar = $('#btnConfirmarBorrar')[0];

    modalBodySpan.textContent = nombreTipo;
    botonConfirmar.href = '/hoteles/hotel/' + idHotel + '/tipos-habitaciones/eliminar/' + idtipo +'/';
})};

var modalEliminarHabitacion = $("#modalEliminarHabitacion")[0];
if (modalEliminarHabitacion) {
  modalEliminarHabitacion.addEventListener('show.bs.modal', function (event) {
    var button = event.relatedTarget; // Button that triggered the modal
    var idHotel = button.dataset.id; // Extract info from data-* attributes
    var idHabitacion = button.dataset.hid; // Extract info from data-* attributes
    var nroHabitacion = button.dataset.nro; // Extract info from data-* attributes
    var modalBodySpan = $('#mensajeBorrar')[0];
    var botonConfirmar = $('#btnConfirmarBorrar')[0];

    modalBodySpan.textContent = nroHabitacion;
    botonConfirmar.href = '/hoteles/hotel/' + idHotel + '/habitaciones/eliminar/' + idHabitacion + '/';
})};