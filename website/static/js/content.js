
//showing the forgot password block :
const change_pass_link =document.getElementById('change_pass_link')
const hide_cross= document.getElementById('hide_cross');
const change_password =document.getElementById('change_password')


 //arrow function (() => { ... }). 
 change_pass_link.addEventListener("click", () => {      
  const computedStyle = window.getComputedStyle(change_password);
  
  if (computedStyle.display == 'none') { // if the (display = none), then
        change_password.style.display = 'flex';
        hide_cross.style.display = 'block';
      } else { // else make the (display = none)
        change_password.style.display = 'none';
        hide_cross.style.display = 'none';
      }
  });

//arrow function (() => { ... })
  hide_cross.addEventListener("click", () => { 
    change_password.style.display = 'none';
    hide_cross.style.display = 'none';

    
  });


