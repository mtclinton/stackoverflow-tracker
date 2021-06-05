// import logo from './logo.svg';
// import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

function App() {
  const [getMessage, setGetMessage] = useState({})

  useEffect(()=>{
    axios.get('http://localhost:5000/').then(response => {
      console.log("SUCCESS", response)
      setGetMessage(response)

    }).catch(error => {
      console.log(error)
    })


  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <p>React + Flask Tutorial</p>
        <div>{getMessage.status === 200 ? 
          <div>
            {getMessage.data.message.map((question) => (

              <div className="question-summary" id="question-summary-67823057">
                <div className="statscontainer">
                  <div className="stats">
                    <div className="vote">
                      <div className="votes"><span className="vote-count-post "><strong>{question[1]}</strong></span>
                        <div className="viewcount">vote</div>
                      </div>
                    </div>
                    <div className="status answered-accepted"><strong>{question[2]}</strong>answer</div>
                  </div>
                  <div className="views " title="18 views"> {question[3]} views</div>
                </div>
                <div className="summary">
                  <h3>
                    <a href={`https://stackoverflow.com${question[5]}`} className="question-hyperlink">
                      {question[4]}
                    </a>
                  </h3>
                  <div className="excerpt">{question[6]}</div>
                  <div className="subcommunities float-left"></div>
                  <div className="started fr">
                    <div className="user-info ">
                      <div className="user-action-time"> asked <span title="2021-06-03 14:10:35Z"
                                                                     className="relativetime">2 days ago</span></div>
                      <div className="user-gravatar32">
                        <a href="/users/9363996/sergey-kolesnik">
                          <div className="gravatar-wrapper-32"><img
                              src="https://i.stack.imgur.com/9Ttto.jpg?s=32&amp;g=1" alt="" width="32" height="32"
                              className="bar-sm" /></div>
                        </a>
                      </div>
                      <div className="user-details"><a href="/users/9363996/sergey-kolesnik">Sergey Kolesnik</a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              ))}
          </div>
          :
          <h3>LOADING</h3>}</div>
      </header>
    </div>
  );
}

export default App;