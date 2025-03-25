import { useState } from "react";
import "mathlive";
import "./App.css";
import { zoomies } from 'ldrs'

function App() {
    const [value, setValue] = useState("");
    const [solution, setSolution] = useState("");
    const [loading, setLoading] = useState(false);
    zoomies.register()

    const handleSend = async () => {
        setLoading(true);
        fetch("http://localhost:8001/api/solve", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ latex: value }),
        })
        .then((res) => res.json())
        .then((data) => setSolution(data))
        .catch((err) => {
            console.error(err);
            setSolution("Error: Could not fetch solution.");
        })
        .finally(() => { setLoading(false); });
    
    };

    return (
        <div className="App">
            <h1>AI-Powered Calculator</h1>
            <div className="LatexInputField">
                <math-field onInput={(evt) => setValue(evt.target.value)}>
                    {value}
                </math-field>
                <button className="SendBtn" onClick={handleSend} disabled={loading}>Send</button>
            </div>
            <div className="SolutionContainer">
                {loading && (<div className="LoadingOverlay">
                <l-zoomies 
                        size="400"
                        stroke="5"
                        bg-opacity="0.1"
                        speed="1.2" 
                        color="black" 
                ></l-zoomies>
                </div>)}

                <div className="Solution">
                <h1>Solution</h1>
                    <math-field readOnly>{solution}</math-field>
                </div>
            </div>
        </div>
    );

}

export default App;
