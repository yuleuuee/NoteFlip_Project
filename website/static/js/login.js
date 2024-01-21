
//showing the forgot password block :
const forgot_link =document.getElementById('forgot_link')
const hide_cross= document.getElementById('hide_cross');
const forgot_password =document.getElementById('forgot_password')


 //arrow function (() => { ... }). 
forgot_link.addEventListener("click", () => {      
  const computedStyle = window.getComputedStyle(forgot_password);
  
  if (computedStyle.display == 'none') { // if the (display = none), then
        forgot_password.style.display = 'flex';
        hide_cross.style.display = 'block';
      } else { // else make the (display = none)
        forgot_password.style.display = 'none';
        hide_cross.style.display = 'none';
      }
  });

//arrow function (() => { ... })
  hide_cross.addEventListener("click", () => { 
    forgot_password.style.display = 'none';
    hide_cross.style.display = 'none';

    
  });

