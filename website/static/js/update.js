 
 // Get the textarea element
 var textarea = document.getElementById('editableTextarea');

 // Set the default text
 var defaultText = "{{note_to_update.data|escapejs}}";
 textarea.value = defaultText;

 // When the textarea is clicked, if it contains the default text, clear it for editing
 textarea.addEventListener('click', function() {
   if (textarea.value === defaultText) {
     textarea.value = defaultText;
   }
 });

