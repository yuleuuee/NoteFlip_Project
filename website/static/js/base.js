

// ************ To remove the error message and cross : ******

const notify_msg = document.getElementById('notify_msg');

// Function to hide the message after 6 seconds
if (notify_msg) {
  setTimeout(() => {
    notify_msg.style.display = 'none';
  }, 6000); // 6000 milliseconds = 6 seconds

 
  const cross = document.getElementById('er_msg');
  
  if (cross) {
    cross.addEventListener("click", remove);
  }
  
  function remove() {
    // if (notify_msg && cross) {
      notify_msg.style.display = 'none';
      cross.style.display = 'none';
    // }
  }

}

// ************ To remove the success message and cross : ******
if (notify_msg) {
  setTimeout(() => {
    notify_msg.style.display = 'none';
  }, 6000); // 6000 milliseconds = 6 seconds

 
  const cross = document.getElementById('su_msg');
  
  if (cross) {
    cross.addEventListener("click", remove);
  }
  
  function remove() {
    // if (notify_msg && cross) {
      notify_msg.style.display = 'none';
      cross.style.display = 'none';
    // }
  }

}


