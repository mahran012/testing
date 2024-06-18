<!DOCTYPE html>
<html>
<head>
    <title>House Robber Problem Test</title>
</head>
<body>
    <h1>House Robber Problem Test</h1>
    <div id="result"></div>
    <script>
        // Sample test cases
        const testCases = [
            {input: [], expected: 0},
            {input: [1], expected: 1},
            {input: [10], expected: 10},
            {input: [1, 2], expected: 2},
            {input: [2, 1], expected: 2},
            {input: [2, 3, 2], expected: 3},
            {input: [1, 2, 3, 1], expected: 4},
            {input: [2, 7, 9, 3, 1], expected: 11},
            {input: [5, 5, 10, 100, 10, 5], expected: 110},
            {input: [6, 7, 1, 30, 8, 2, 4], expected: 41},
            {input: [1, 3, 1, 3, 100], expected: 103},
        ];

        // Function to send test data to the server and get the result
        async function runTest() {
            const resultsDiv = document.getElementById('result');
            for (let testCase of testCases) {
                let response = await fetch('/run_test', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(testCase.input)
                });
                let result = await response.json();
                resultsDiv.innerHTML += `<p>Input: ${JSON.stringify(testCase.input)} - Expected: ${testCase.expected} - Got: ${result}</p>`;
            }
        }

        // Call the function to run the test
        runTest();
    </script>
</body>
</html>
