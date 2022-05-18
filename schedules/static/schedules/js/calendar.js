let nav = 0;
let clicked = null;
let events = localStorage.getItem('events') ? JSON.parse(localStorage.getItem('EVENTS')) : [];


const calendar = document.getElementById('calendar');
const weekdays = ['Sabado', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado'];

function load() {
    const dt = new Date();
  
    if (nav !== 0) {
      dt.setMonth(new Date().getMonth() + nav);
    }
  
    const day = dt.getDate();
    const month = dt.getMonth();
    const year = dt.getFullYear();
  
    const firstDayOfMonth = new Date(year, month, 1);
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    
    const dateString = firstDayOfMonth.toLocaleDateString('en-us', {
      weekday: 'long',
      year: 'numeric',
      month: 'numeric',
      day: 'numeric',
    });
    const paddingDays = weekdays.indexOf(dateString.split(', ')[0]);
  
    document.getElementById('monthDisplay').innerText = 
      `${dt.toLocaleDateString('en-us', { month: 'long' })} ${year}`;
  
    calendar.innerHTML = '';
  
    for(let i = 1; i <= paddingDays + daysInMonth; i++) {
      const daySquare = document.createElement('div');
      daySquare.classList.add('day');
  
      const dayString = `${month + 1}/${i - paddingDays}/${year}`;
  
      if (i > paddingDays) {
        daySquare.innerText = i - paddingDays;
        const eventForDay = events.find(e => e.date === dayString);
  
        if (i - paddingDays === day && nav === 0) {
          daySquare.id = 'currentDay';
        }
  
        if (eventForDay) {
          const eventDiv = document.createElement('div');
          eventDiv.classList.add('event');
          eventDiv.innerText = eventForDay.title;
          daySquare.appendChild(eventDiv);
        }
  
        daySquare.addEventListener('click', () => openModal(dayString));
      } else {
        daySquare.classList.add('padding');
      }
  
      calendar.appendChild(daySquare);    
    }
  }
  load();
  