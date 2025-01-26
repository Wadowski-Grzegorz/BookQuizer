import { useState } from "react";

const questions = [
  {
    question: "Indeks, paragraf?",
    options: [
      { text: "Index", value: 1.2 },
      { text: "Paragraf", value: 0.8 },
      { text: "Żadne", value: 1.5 },
    ],
  },
  {
    question: "Czy foka lubi rozgwiady?",
    options: [
      { text: "Tak", value: 8 },
      { text: "Nie", value: 2 },
    ],
  },
  {
    question: "Miejsce do relaksu?",
    options: [
      { text: "Kanapa", value: 1.2 },
      { text: "Kawiarnia", value: 8.6 },
      { text: "Pijalnia wódki", value: 5 },
    ],
  },
];

export default function Quiz() {
  const [answers, setAnswers] = useState(Array(questions.length).fill(null));

  const handleChange = (questionIndex, value) => {
    const newAnswers = [...answers];
    newAnswers[questionIndex] = value;
    setAnswers(newAnswers);
  };

  const handleSubmit = async () => {
    const requestData = {
        answers: answers,
    };

    const response = await fetch("http://localhost:8000/recommendation/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(requestData),
    });

    const result = await response.json();
    console.log("Response from server:", result);
    alert(`Recommended book: ${result.title}`)
  };

  return (
    <div>
      <h2>Ankieta</h2>
      {questions.map((q, qIndex) => (
        <div key={qIndex}>
          <p>{q.question}</p>
          {q.options.map((option, oIndex) => (
            <label key={oIndex}>
              <input
                type="radio"
                name={`question-${qIndex}`}
                value={option.value}
                checked={answers[qIndex] === option.value}
                onChange={() => handleChange(qIndex, option.value)}
              />
              {option.text}
            </label>
          ))}
        </div>
      ))}
      <button onClick={handleSubmit}>Wyślij</button>
    </div>
  );
}
