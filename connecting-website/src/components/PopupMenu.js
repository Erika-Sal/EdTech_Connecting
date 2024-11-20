import React, { useState } from 'react';

function PopupMenu({ title, index, color, onSelectionChange }) {
  const [isOpen, setIsOpen] = useState(false);
  const [selectedButtons, setSelectedButtons] = useState({});

  const buttons = [
    ["Business", "Science", "Pre-Med", "Pre-Law", "Engineering", "Finance", "Entrepreneurship", "Consulting", "Marketing", "Communication", "Journalism", "Accounting", "Economics", "Human Resources", "Internal Relations"],
    ["Performing Arts", "Fine Arts", "Digital Arts", "Writing", "Architecture", "Fashion Design", "Music Production", "Literary Arts", "Film Studies"],
    ["Latino", "African American", "Asian American", "Native American/Indigenous", "Christian", "Muslim", "Hindu", "Buddhist", "Interfaith/Spiritual Groups", "LGBTQ+ Advocacy", "Gender Equality", "Language Exchange", "International Student"],
    ["Volunteering", "Environmental Sustainability", "Social Justice", "Hunger and Poverty Alleviation", "Mental Health Advocacy", "Health", "Community Outreach", "Nonprofit Fundraising", "Community Development"],
    ["Team Sports", "Individual Sports", "Adventure Sports", "Fitness", "Water Sports", "Dance", "Cycling", "Archery"],
    ["Robotics", "Artificial Intelligence", "App/Web Development", "Cybersecurity", "Data Science", "Bioinformatics", "Machine Learning", "UX/UI Design"],
    ["Debate", "Public Speaking", "Gaming", "Travel", "Photography", "Culinary Arts", "DIY & Crafting", "Film & TV Club", "Astronomy"],
    ["Voter Registration", "Climate Change Advocacy", "LGBTQ+ Rights", "Labor Rights", "Civil Liberties", "Human Rights", "Political Campaigning", "Youth Advocacy", "Immigration Rights"],
    ["Mindfulness & Meditation", "Mental Health Awareness", "Fitness & Nutrition", "Peer Counseling", "Sexual Health Advocacy", "Holistic Health", "Outdoor Recreation", "Wellness Education", "Addiction Support"],
    ["Engineering", "Biology", "Chemistry", "Physics", "Neuroscience", "Astronomy", "Geology", "Environmental Science", "Mathematics"],
    ["Journalism", "Podcasting", "Blogging", "Video Production", "Radio", "Photography", "Graphic Design", "Social Media Management", "Broadcasting"],
    ["Renewable Energy", "Climate Action", "Urban Planning", "Wildlife Conservation", "Marine Biology", "Environmental Policy", "Ecology", "Green Technology", "Waste Reduction"]
  ];

  const togglePopup = () => setIsOpen(!isOpen);

  const toggleButtonSelection = (buttonIndex) => {
    setSelectedButtons((prevState) => {
      const isSelected = !!prevState[buttonIndex];
      const updatedSelections = { ...prevState, [buttonIndex]: !isSelected };

      // Notify parent component
      const selectedSubcategories = Object.keys(updatedSelections)
        .filter((key) => updatedSelections[key])
        .map((key) => buttons[index][key]);
      onSelectionChange(selectedSubcategories);

      return updatedSelections;
    });
  };

  function hexToRgba(hex, opacity) {
    const r = parseInt(hex.slice(1, 3), 16);
    const g = parseInt(hex.slice(3, 5), 16);
    const b = parseInt(hex.slice(5, 7), 16);
    return `rgba(${r}, ${g}, ${b}, ${opacity})`;
  }

  return (
    <div>
      <button
        onClick={togglePopup}
        className="originalButton"
        style={{ backgroundColor: hexToRgba(color, 0.7)  }}
      >
        {title}
      </button>

      {isOpen && (
        <div style={styles.overlay}>
          <div style={styles.popup}>
            <button onClick={togglePopup} style={styles.closeButton}>
              X
            </button>
            <div className="groupSubButtons">
              {buttons[index]?.map((text, buttonIndex) => {
                const isSelected = selectedButtons[buttonIndex] || false;
                return (
                  <button
                    key={buttonIndex}
                    className='subButton'
                    onClick={() => toggleButtonSelection(buttonIndex)}
                    style={{
                      backgroundColor: isSelected ? '#015464' : '#6FBEBF',
                      color: isSelected ? '#fff' : '#000',
                    }}
                  >
                    {text}
                  </button>
                );
              })}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

const styles = {
  overlay: {
    position: 'fixed',
    top: 0,
    left: 0,
    width: '100vw',
    height: '100vh',
    backgroundColor: 'rgba(0, 0, 0, 0.8)', // Dark transparent background
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    zIndex: 1000,
  },
  popup: {
    backgroundColor: '#fff',
    padding: '20px',
    borderRadius: '8px',
    width: '90%',
    maxWidth: '500px',
    textAlign: 'center',
    position: 'relative',
  },
  closeButton: {
    position: 'absolute',
    top: '10px',
    right: '10px',
    padding: '5px 10px',
    fontSize: '17px',
    fontWeight: 'bold',
    cursor: 'pointer',
  },
};

export default PopupMenu;
