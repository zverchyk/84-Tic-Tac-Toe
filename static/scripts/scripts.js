
function makeMove(cell) {
    
    if (!localStorage.getItem('currentPlayer')) {
        localStorage.setItem('currentPlayer', 'O');
        }
    let currentPlayer = localStorage.getItem('currentPlayer');

    if (cell.innerHTML === '') {
        cell.innerHTML = currentPlayer; // Placeholder: Alternates between 'X' and 'O', checks for win conditions, etc.
        


    }


}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

var cleanList = dataFromServer['clean_list'];


if (!localStorage.getItem('pressedElements') || cleanList) {
    localStorage.setItem('pressedElements', JSON.stringify([]));
}

document.querySelectorAll('.cell').forEach(element => {
    element.addEventListener('click', function clickEventHandler() {
        console.log('Button clicked!')
        // sending data to python flask
        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                key: this.dataset.value,
                current_player: localStorage.getItem('currentPlayer'),
            })
            
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); // Process the response if it's in JSON format
        })
        .then(data => {
            console.log(data); // Handle the data from the response
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });

        sleep(100).then(() =>{
            fetch('/data')
            .then(responce=> responce.json())
            .then(data => {
                let currentPlayer = localStorage.getItem('currentPlayer')
                if (data.message === true){
                    console.log(data.message)
                    if (data.result === true){
                    document.getElementById('endGame').innerText = `Player ${currentPlayer} won!`;
                    }else{
                        document.getElementById('endGame').innerText = "It's a tie";
                    }
                    document.querySelectorAll('.cell').forEach(element =>{
                        element.classList.add('deactivated');
                    });
                }else{
                    // Toggle the currentPlayer and update localStorage
                    currentPlayer = (currentPlayer === 'X') ? 'O' : 'X';
                    localStorage.setItem('currentPlayer', currentPlayer);
                    console.log(data.message)
                }

            })
            .catch(error => console.error('Error fetching data:', error));
        })

        // Get the current list of pressed elements from local storage
        let pressedElements = JSON.parse(localStorage.getItem('pressedElements'));



        // Check if the element's data value is not already in the list
        if (!pressedElements.includes(this.dataset.value)) {
            // Add the element's dataset value to the list
            pressedElements.push(this.dataset.value);

            // Update local storage with the new list
            localStorage.setItem('pressedElements', JSON.stringify(pressedElements));

            // Deactivate the element (example: adding a class that styles it as inactive)
            this.classList.add('deactivated');
        }

        console.log(pressedElements)
        // Optionally, prevent further clicks on this element
        this.removeEventListener('click', clickEventHandler);
    });
});


