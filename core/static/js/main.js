(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");
    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Seguro de eliminar el Item?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
})();


function valForm(){
    console.log("Pagina Funcionando");
    var vNom = $('#nombre').val();
    var vMail = $('#correo').val();
    var vMensaje = $('#mensaje').val();

    //Validar campo nombre

    if(vNom=="" || vNom==null ) {
        Err_color("nombre")
        Err_Contenido("Campo Nombre")
        return false;
    }

    else{
        var expresion = /^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(vNom)){
            Err_color("nombre");
            Err_Contenido(" nombre, No se permiten caracteres especiales");
            return false;
        }
    }

    if(vMail=="" || vMail==null ) {
        Err_color("correo")
        Err_Contenido("correo")
        return false;
    }

    else{
        var expresion = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
        if(!expresion.test(vMail)){
            Err_color("correo");
            Err_Contenido(" formato de correo no admitido");
            return false;
        }
    }

    if(vMensaje=="" || vMensaje==null ) {
        Err_color("mensaje")
        Err_Contenido("mensaje")
        return false;
    }

    else{
        var expresion = /^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(vMensaje)){
            Err_color("mensaje");
            Err_Contenido(" mensaje no admitido");
            return false;
        }
    }

    $('form').submit();
    return true;
}