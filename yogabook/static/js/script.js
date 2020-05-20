const radioboxes = document.querySelectorAll('.radio-group input[type=radio]')
for(let radiobox of radioboxes){
  radiobox.onchange = function (event){
    if(radiobox.checked){
      document.getElementById('form_picture').src =  radiobox.value;
    }
  }

}
