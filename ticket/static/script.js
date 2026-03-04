document.getElementById('ticketBtn').addEventListener('click', function() {
    alert('Ticket Booking feature is coming soon!')
});



document.addEventListener("DOMContentLoaded", function() {
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl)
        });
    });


document.getElementById('searchForm').addEventListener('submit', function(event) {
        event.preventDefault();  // Prevent the default form submission behavior
        filterTable();
    });


function filterTable() {
        let input = document.getElementById('searchInput').value.toLowerCase();
        let table = document.getElementById('busTable');
        let rows = table.getElementsByTagName('tr');

        for (let i = 1; i < rows.length; i++) { // Start at 1 to skip the header row
            let row = rows[i];
            let columns = row.getElementsByTagName('td');
            let isMatch = false;

            // Check if any column matches the search input
            for (let j = 0; j < columns.length; j++) {
                if (columns[j].innerText.toLowerCase().includes(input)) {
                    isMatch = true;
                    break;
                }
            }

            // Show/hide rows based on the match
            if (isMatch) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        }
    }



    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this bus ticket?')) {
                e.preventDefault();
            }
        });
    }); 