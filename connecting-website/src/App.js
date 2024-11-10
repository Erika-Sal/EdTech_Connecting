import React from 'react';
import PopupMenu from './components/PopupMenu'
import './App.css'

function App() {
  const quizzes = [
    "Academic & Professional", "Creative & Arts", "Cultural & Identity",
    "Community Service & Social Impact", "Sports & Recreation", "Technology & Innovation",
    "Social & Special Interests", "Political & Advocacy", "Health & Wellness",
    "STEM - Specific", "Media & Communication", "Environmental & Sustainability"
  ];

  return (
    <>
    <h1>Pick What You Are Interested In:</h1>
    <div className="Quiz">
      {quizzes.map((text, index) => (
        <PopupMenu key={index} title={text} index={index} className="originalButton"/>
      ))}
    </div>
    <button className='submitButton'>Submit</button>
    </>
  );

}

export default App;
