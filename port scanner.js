const net = require('net');
const readline = require('readline');

// Function to scan a single port
function scanPort(ip, port) {
    return new Promise((resolve) => {
        const socket = new net.Socket();
        let isOpen = false;

        // Set a timeout for the connection attempt
        socket.setTimeout(500); // 500ms timeout
        socket.on('connect', () => {
            isOpen = true;
            socket.destroy(); // Close the connection
        });

        socket.on('timeout', () => {
            socket.destroy(); // Close the connection on timeout
        });

        socket.on('error', () => {
            // Ignore errors (port is likely closed)
        });

        socket.on('close', () => {
            resolve({ port, isOpen });
        });

        // Attempt to connect to the port
        socket.connect(port, ip);
    });
}

// Function to scan a range of ports
async function scanPortRange(ip, startPort, endPort) {
    console.log(`Scanning ${ip} from port ${startPort} to ${endPort}...\n`);
    for (let port = startPort; port <= endPort; port++) {
        const { port: scannedPort, isOpen } = await scanPort(ip, port);
        if (isOpen) {
            console.log(`Port ${scannedPort} is open`);
        }
    }
    console.log("\nScan complete.");
}

// Function to get user input
function getUserInput() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });

    rl.question("Enter the target IP address: ", (ip) => {
        rl.question("Enter the starting port: ", (startPort) => {
            rl.question("Enter the ending port: ", (endPort) => {
                rl.close();
                scanPortRange(ip, parseInt(startPort), parseInt(endPort));
            });
        });
    });
}

// Main function
function main() {
    console.log("Port Scanner in JavaScript");
    console.log("-------------------------");
    getUserInput();
}

// Run the script
main();
