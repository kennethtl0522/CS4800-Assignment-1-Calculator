import { useState } from "react";
import "mathlive";
import "./App.css";
import { convertLatexToAsciiMath, convertLatexToMarkup, convertLatexToMathMl, convertLatexToSpeakableText } from "mathlive";

function App() {
    const [value, setValue] = useState("");

    return (
        <div className="App">
            <div className="LatexInputField">
                <math-field onInput={(evt) => setValue(evt.target.value)}>
                    {value}
                </math-field>
                <button className="SendBtn">Send</button>
            </div>
            <p>Value: {value}</p>
            <div className="SolutionContainer">
                <div className="Solution">
                    <h1>Solution</h1>
                    <p>{convertLatexToSpeakableText(value)}</p>
                </div>
            </div>
        </div>
    );
}

export default App;
