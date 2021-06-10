import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';


import fetchQuestions from "../util/fetchQuestions";

function Container(props) {

    const {type, page} = props;
    const [loading, setLoading] = useState(true);
    const [questions, setQuestions] = useState([])

    useEffect(() => {
        if(questions.length !== 0 ) return
        console.log('calling use effect')
        setLoading(true);
        async function getQuestions() {
            setQuestions(await fetchQuestions(type, page))
            // setQuestions();
            setLoading(false);

        }

        getQuestions();
    }, [questions]);

    return (
        <>
            {
                loading && <div>Loading</div>
            }
            {
                !loading
                && questions.map((question) => (
                        <div className="mln24">
                            <div className="question-summary" id="question-summary-712279">
                                <div className="statscontainer">
                                    <div className="stats">
                                        <div className="vote">
                                            <div className="votes"><span
                                                className="vote-count-post "><strong>{question[1]}</strong></span>
                                                <div className="viewcount">votes</div>
                                            </div>
                                        </div>
                                        <div className="status answered-accepted"><strong>{question[2]}</strong>answers
                                        </div>
                                    </div>
                                    <div className="views hot" title="98,194 views"> {question[3]} views</div>
                                </div>
                                <div className="summary">
                                    <h3><a href={`https://stackoverflow.com${question[5]}`}
                                           className="question-hyperlink">{question[4]}</a></h3>
                                    <div className="excerpt">{question[6]}</div>
                                    <div className="subcommunities float-left"></div>
                                    <div className="started fr">
                                        <div className="user-info ">
                                            <div className="user-action-time"> asked <span title="2009-04-03 01:46:07Z"
                                                                                           className="relativetime">{new Date(question[7] * 1000).toLocaleDateString("en-US", {
                                                month: 'short',
                                                day: 'numeric',
                                                year: '2-digit'
                                            })}</span>
                                            </div>
                                            <div className="user-gravatar32">
                                                <a href="/users/84842/fido">
                                                    <div className="gravatar-wrapper-32"><img
                                                        src={`${question[9]}`}
                                                        alt="" width="32" height="32" className="bar-sm"/></div>
                                                </a>
                                            </div>
                                            <div className="user-details"><a
                                                href={`https://stackoverflow.com${question[10]}`}>{question[8]}</a>

                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    ))
            }


        </>
    );
}

export default Container;