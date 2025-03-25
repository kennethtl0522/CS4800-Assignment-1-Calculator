import { useState } from "react";
import "mathlive";
import "./App.css";

function App() {
    const [value, setValue] = useState("");
    const [solution, setSolution] = useState("");

    const handleSend = async () => {
        const response = await fetch("http://localhost:8001/api/solve", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ latex: value }),
        });

        const data = await response.json();
        setSolution(data);
    };

    return (
        <div className="App">
            <h1>AI-Powered Calculator</h1>
            <div className="LatexInputField">
                <math-field onInput={(evt) => setValue(evt.target.value)}>
                    {value}
                </math-field>
                <button className="SendBtn" onClick={handleSend}>Send</button>
            </div>
            <div className="SolutionContainer">
                <div className="Solution">
                    <h1>Solution</h1>
                    <math-field readOnly>{solution}</math-field>
                </div>
            </div>
        </div>
    );

}

export default App;
