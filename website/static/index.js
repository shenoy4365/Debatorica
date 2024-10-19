// function deleteNote(noteId) {
//   fetch("/delete-note", {
//     method: "POST",
//     body: JSON.stringify({ noteId: noteId }),
//   }).then((_res) => {
//     window.location.href = "/";
//   });
// }

<script>
document.querySelectorAll('.delete-note').forEach(button = {
    button.addEventListener('click', () => {
        const noteId = button.dataset.noteId;  // Get the note ID from a data attribute

        fetch('/delete-note', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ noteId: noteId }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Remove the note element from the DOM
                button.closest('.note-item').remove();  // Adjust selector based on your HTML structure
            } else {
                console.error('Failed to delete note');
            }
        })
        .catch(error => console.error('Error deleting note:', error));
    })
});
</script>
