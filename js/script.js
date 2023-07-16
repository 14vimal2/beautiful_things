
// input box where user gives commands
const INPUT_BOX = document.getElementById('input-box');
const SCREEN = document.getElementById('screen');

// list of available terminal commands

const PATTERNS = [
    {
        name: "3n+1",
        desc: "description of pattern1",
        code: "code to generate pattern1",
        image: "3nplus1.png"
    },
    {
        name: "collatz",
        desc: "description of pattern2",
        code: "code to generate pattern2",
        image: "collatz.png"
    },
    {
        name: "sierpinski",
        desc: "description of pattern3",
        code: "code to generate pattern3",
        image: "sierpinski_triangle.png"
    },
    {
        name: "fibonacci",
        desc: "description of pattern4",
        code: "code to generate pattern4",
        image: "fibspiral.png"
    },
    {
        name: "ulam",
        desc: "description of pattern5",
        code: "code to generate pattern5",
        image: "prime_spiral.png"
    },
]

const COMMANDS = [
    {
        name: "help",
        desc: "displays all available commands",
        execute: function() {
            COMMANDS.forEach(command => {
                SCREEN.innerHTML += `<div><span class="command">${command.name}</span> &emsp; <span>${command.desc}</span> </div>`
            })
        }
    },
    {
        name: "ls",
        desc: "lists all available patterns",
        execute: function() {
            PATTERNS.forEach(pattern => {
                SCREEN.innerHTML += `<div>${pattern.name}</div>`
            })
        }
        
    },
    {
        name: "cat",
        desc: 
        `Usage: cat [OPTION]...  [PATTERN]...
        displays pattern

        when no options, it just displays the image.

        -D, --describe              shows description of the pattern
        -c, --code                  shows code to generate the pattern 
        `,
        execute: function(value) {
            var pattern_name = value[0];
            var pattern = PATTERNS.find(p => p.name === pattern_name)
            if (pattern) {
                addImage(pattern.image);
            } else {
                SCREEN.innerHTML += 'No such pattern exists.'
            }
        }
    },
    {
        name: "clear",
        desc: "clears the screen"
    }
]

function addImage(imagename) {
    SCREEN.innerHTML += `<img src="${imagename}" alt="pattern" width="600" height="600">`
}


INPUT_BOX.addEventListener('input',commandGiven);
INPUT_BOX.focus()

function commandGiven() {
    const inputWidth = INPUT_BOX.value;
    var width = inputWidth.length * 8;
    INPUT_BOX.style.width = width + "px";
    
}

function handleKeyPress(event) {
    var key = event.keyCode || event.which;
    if (key == 13) {
        event.preventDefault();
        console.log('Enter key pressed');
        submitInput();
    }
}

function submitInput() {
    // trim INPUT_BOX.value
    const input = INPUT_BOX.value.trim();
    if (input === 'clear') {
        SCREEN.innerHTML = '';
        INPUT_BOX.value = '';
        commandGiven();
        return;
    }
    var prevcommand =  `<div id="input-container">
<span class="username">guest@beautifulthings:</span>
<span class="current-path">~</span>$ ${input}
</div>`

    console.log('this was the input',input);
    // execute command
    SCREEN.innerHTML += prevcommand;

    executeCommand(input)

    INPUT_BOX.value = '';
    commandGiven();
    INPUT_BOX.focus();
    // add input to history
}

function executeCommand(command) {
    var commandname = command.split(' ')[0];
    var arguments = command.split(' ').slice(1);
    var command = COMMANDS.find(command => command.name == commandname);
    if (command) {
        // execute command with arguments
        command.execute(arguments);        
    }
}