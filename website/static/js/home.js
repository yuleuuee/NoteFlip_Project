// ************ To remove the Account Deletion message and cross : ******

const acc_del_msg = document.getElementById('acc_del_msg');

// Function to hide the message after 4 seconds
if (acc_del_msg) {
  setTimeout(() => {
    acc_del_msg.style.display = 'none';
  }, 6000); // 6000 milliseconds = 6 seconds

  const cross = document.getElementById('cross');
  if (cross) {
    cross.addEventListener("click", remove);
  }

  function remove() {
    if (acc_del_msg && cross) {
      acc_del_msg.style.display = 'none';
      cross.style.display = 'none';
    }
  }
}




