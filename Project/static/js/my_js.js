function create_href(carId,name_button) {
    button_id = event.target.id;
    var r = confirm("İşlemi gerçekleştirmekten emin misiniz?");
    if (r == true) {
        document.getElementById(button_id).onclick="";
        document.getElementById(button_id).href=name_button+"/"+carId;    
        document.getElementById(button_id).click();    
    } else {
    }   
}