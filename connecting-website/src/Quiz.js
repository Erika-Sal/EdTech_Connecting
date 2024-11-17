import React from 'react';
import PopupMenu from './components/PopupMenu'
import './Quiz.css'

function Quiz() {
  const quizzes = [
    "Academic & Professional", "Creative & Arts", "Cultural & Identity",
    "Community Service & Social Impact", "Sports & Recreation", "Technology & Innovation",
    "Social & Special Interests", "Political & Advocacy", "Health & Wellness",
    "STEM - Specific", "Media & Communication", "Environmental & Sustainability"
  ];
  const colors = ["#6FBEBF", "#D32628", "#015464", "#821A0F", "#821A0F", "#015464", "#6FBEBF", "#D32628", "#6FBEBF", "#D32628", "#821A0F", "#015464"]

  return (
    <>
    <h1>Select the Categories You Are Interested In:</h1>
    <div className="Quiz">
      {quizzes.map((text, index) => (
        <PopupMenu key={index} title={text} index={index} color={colors[index]} className="originalButton"/>
      ))}
    </div>
    <button className='submitButton' style={{backgroundColor:"#FDD275"}}>Submit</button>
    </>
  );

}

export default Quiz;
